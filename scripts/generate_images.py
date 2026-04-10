#!/usr/bin/env python3
"""Generate all course illustrations from IMAGE-PLAN.md using Google Gemini image generation."""

import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
IMAGE_PLAN = PROJECT_ROOT / "IMAGE-PLAN.md"
IMAGES_DIR = PROJECT_ROOT / "images"

# Cost per image token (Gemini 2.0 Flash pricing as approximation)
# Actual: ~$0.14 per image at final quality based on reference project
COST_PER_IMAGE_ESTIMATE = 0.14


def parse_image_plan():
    """Parse IMAGE-PLAN.md to extract all image entries."""
    text = IMAGE_PLAN.read_text(encoding="utf-8")
    images = []

    # Split by ### Image headers
    current_module = ""
    for line in text.split("\n"):
        if line.startswith("## Module"):
            current_module = line.strip("# ").strip()

    # More robust parsing: find each image block
    blocks = re.split(r"### Image \d+:", text)
    current_module = ""

    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("## Module"):
            current_module = line.lstrip("# ").strip()
            # Extract module number
            m = re.search(r"Module (\d+)", current_module)
            current_module_num = int(m.group(1)) if m else -1

        if line.startswith("### Image"):
            image_name = line.split(":", 1)[1].strip() if ":" in line else ""
            file_path = ""
            prompt_lines = []
            in_prompt = False
            description = ""

            j = i + 1
            while j < len(lines) and not lines[j].startswith("### Image") and not lines[j].startswith("## Module") and not lines[j].startswith("---"):
                l = lines[j]
                if l.startswith("- **File**:"):
                    file_path = l.split("`")[1] if "`" in l else ""
                if l.startswith("- **Description**:"):
                    description = l.split(":", 1)[1].strip()
                if in_prompt:
                    if l.strip() and (l.startswith("  ") or l.startswith("\t")):
                        prompt_lines.append(l.strip())
                    elif not l.strip():
                        pass  # blank line in prompt
                    else:
                        in_prompt = False
                if l.startswith("- **Prompt**:"):
                    in_prompt = True
                j += 1

            if file_path and prompt_lines:
                # Parse prompt fields
                prompt_data = {}
                for pl in prompt_lines:
                    if ":" in pl:
                        key, val = pl.split(":", 1)
                        prompt_data[key.strip()] = val.strip()

                images.append({
                    "module": current_module,
                    "name": image_name,
                    "file": file_path,
                    "description": description,
                    "prompt_data": prompt_data,
                })

            i = j
            continue
        i += 1

    return images


def build_assembled_prompt(prompt_data):
    """Build the full prompt string from parsed fields."""
    goal = prompt_data.get("Goal", "editorial illustration for a programming textbook")
    scene = prompt_data.get("Scene", "")
    style = prompt_data.get("Style", "Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational")
    aspect = prompt_data.get("Aspect ratio", "16:9")
    bg = prompt_data.get("Background", "white")
    text_img = prompt_data.get("Text in image", "minimal or none")
    avoid = prompt_data.get("Avoid", "photorealistic, dark, scary, complex UI screenshots")

    return (
        f"Create a {goal}. {scene} "
        f"Style: {style}. "
        f"Aspect ratio: {aspect}. "
        f"Background: {bg}. "
        f"Text in image: {text_img}. "
        f"Avoid: {avoid}."
    )


def generate_image(prompt, output_path, api_key):
    """Generate an image using Gemini API. Returns metadata dict."""
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)

    start = time.time()
    response = client.models.generate_content(
        model="gemini-3-pro-image-preview",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
        ),
    )

    elapsed_ms = int((time.time() - start) * 1000)

    # Extract image from response
    image_saved = False
    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(part.inline_data.data)
            image_saved = True
            break

    if not image_saved:
        print(f"    WARNING: No image in response")
        return None

    # Build metadata
    usage = {}
    if response.usage_metadata:
        usage = {
            "prompt_tokens": response.usage_metadata.prompt_token_count,
            "candidates_tokens": response.usage_metadata.candidates_token_count,
            "total_tokens": response.usage_metadata.total_token_count,
        }

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model_requested": "nanobanana-pro",
        "model_resolved": "gemini-3-pro-image-preview",
        "model_friendly": "nanobanana-pro",
        "quality_mode": "final",
        "prompt": prompt,
        "output_file": output_path.name,
        "generation_time_ms": elapsed_ms,
        "usage": usage,
    }


def get_api_key():
    """Get Gemini API key from environment or .env file."""
    key = os.environ.get("GEMINI_API_KEY")
    if key:
        return key
    env_path = PROJECT_ROOT / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if line.startswith("GEMINI_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate course illustrations from IMAGE-PLAN.md")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be generated")
    parser.add_argument("--force", action="store_true", help="Regenerate existing images")
    parser.add_argument("--module", help="Only generate for this module (e.g., 'Module 01')")
    args = parser.parse_args()

    api_key = get_api_key()
    if not api_key and not args.dry_run:
        print("ERROR: GEMINI_API_KEY not set")
        sys.exit(1)

    images = parse_image_plan()
    print(f"Found {len(images)} images in IMAGE-PLAN.md")

    if args.module:
        images = [img for img in images if args.module.lower() in img["module"].lower()]
        print(f"Filtered to {len(images)} images for '{args.module}'")

    generated = 0
    skipped = 0
    failed = 0
    total_tokens = 0
    total_time_ms = 0

    for img in images:
        output_path = IMAGES_DIR / img["file"].replace("images/", "")
        prompt = build_assembled_prompt(img["prompt_data"])

        if output_path.exists() and not args.force:
            print(f"  SKIP (exists): {img['file']}")
            skipped += 1
            continue

        if args.dry_run:
            print(f"  WOULD GENERATE: {img['file']}")
            print(f"    Module: {img['module']}")
            print(f"    Prompt: {prompt[:100]}...")
            continue

        print(f"  Generating: {img['file']}...")
        try:
            meta = generate_image(prompt, output_path, api_key)
            if meta:
                # Save metadata JSON
                json_path = output_path.with_suffix(".json")
                json_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
                generated += 1
                tokens = meta.get("usage", {}).get("total_tokens", 0)
                total_tokens += tokens
                total_time_ms += meta.get("generation_time_ms", 0)
                print(f"    → {output_path.name} ({meta['generation_time_ms']}ms, {tokens} tokens)")
            else:
                failed += 1
        except Exception as e:
            print(f"    ERROR: {e}")
            failed += 1
            # Brief pause on error
            time.sleep(2)

        # Rate limit: brief pause between requests
        time.sleep(1)

    print(f"\n{'='*50}")
    print(f"Results:")
    print(f"  Generated: {generated}")
    print(f"  Skipped:   {skipped}")
    print(f"  Failed:    {failed}")
    print(f"  Total tokens: {total_tokens}")
    print(f"  Total time: {total_time_ms / 1000:.1f}s")
    est_cost = generated * COST_PER_IMAGE_ESTIMATE
    print(f"  Estimated cost: ${est_cost:.2f} ({generated} images × ${COST_PER_IMAGE_ESTIMATE}/image)")


if __name__ == "__main__":
    main()
