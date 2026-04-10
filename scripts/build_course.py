#!/usr/bin/env python3
"""Build the Git Fundamentals course from Markdown source files into interactive HTML pages."""

import argparse
import base64
import os
import re
import sys
from pathlib import Path

import markdown
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.toc import TocExtension
from markdown.extensions.md_in_html import MarkdownInHtmlExtension

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
SOURCE_DIR = PROJECT_ROOT / "source"
IMAGES_DIR = PROJECT_ROOT / "images"
AUDIO_DIR = PROJECT_ROOT / "audio"
HTML_DIR = PROJECT_ROOT / "html"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
QUIZ_DIR = PROJECT_ROOT / "Quiz"
TEMPLATE_PATH = SCRIPTS_DIR / "module_template.html"

# Module registry
MODULES = [
    {
        "file": "module-00-intro.md",
        "short": "Module 0",
        "title": "Welcome to Git Fundamentals",
        "tier": "Start Here",
        "tier_css": "tier-start-here",
    },
    {
        "file": "module-01-what-is-git.md",
        "short": "Module 1",
        "title": "What Is Git?",
        "tier": "Start Here",
        "tier_css": "tier-start-here",
    },
    {
        "file": "module-02-workflow-basics.md",
        "short": "Module 2",
        "title": "The Edit-Stage-Commit Workflow",
        "tier": "Start Here",
        "tier_css": "tier-start-here",
    },
    {
        "file": "module-03-repos-and-ignoring.md",
        "short": "Module 3",
        "title": "Repositories and Ignoring Files",
        "tier": "Start Here",
        "tier_css": "tier-start-here",
    },
    {
        "file": "module-04-staging-and-commits.md",
        "short": "Module 4",
        "title": "Advanced Staging and Commit Messages",
        "tier": "Start Here",
        "tier_css": "tier-start-here",
    },
    {
        "file": "module-05-viewing-history.md",
        "short": "Module 5",
        "title": "Exploring Git History",
        "tier": "Useful Soon",
        "tier_css": "tier-useful-soon",
    },
    {
        "file": "module-06-branching-basics.md",
        "short": "Module 6",
        "title": "Branching Basics",
        "tier": "Useful Soon",
        "tier_css": "tier-useful-soon",
    },
    {
        "file": "module-07-merging.md",
        "short": "Module 7",
        "title": "Merging Branches",
        "tier": "Useful Soon",
        "tier_css": "tier-useful-soon",
    },
    {
        "file": "module-08-remote-repos.md",
        "short": "Module 8",
        "title": "Working with Remote Repositories",
        "tier": "Useful Soon",
        "tier_css": "tier-useful-soon",
    },
    {
        "file": "module-09-clone-fetch-pull.md",
        "short": "Module 9",
        "title": "Clone, Fetch, and Pull",
        "tier": "Useful Soon",
        "tier_css": "tier-useful-soon",
    },
    {
        "file": "module-10-push-pull-workflow.md",
        "short": "Module 10",
        "title": "The Feature Branch Workflow",
        "tier": "When You're Ready",
        "tier_css": "tier-when-youre-ready",
    },
    {
        "file": "module-11-merge-conflicts.md",
        "short": "Module 11",
        "title": "Merge Conflicts",
        "tier": "When You're Ready",
        "tier_css": "tier-when-youre-ready",
    },
    {
        "file": "module-12-rebasing.md",
        "short": "Module 12",
        "title": "Rebasing",
        "tier": "When You're Ready",
        "tier_css": "tier-when-youre-ready",
    },
    {
        "file": "module-13-stashing.md",
        "short": "Module 13",
        "title": "Git Stash",
        "tier": "When You're Ready",
        "tier_css": "tier-when-youre-ready",
    },
    {
        "file": "module-14-tagging.md",
        "short": "Module 14",
        "title": "Tags and Releases",
        "tier": "Advanced",
        "tier_css": "tier-advanced",
    },
    {
        "file": "module-15-collaboration.md",
        "short": "Module 15",
        "title": "Git Collaboration Workflows",
        "tier": "Advanced",
        "tier_css": "tier-advanced",
    },
]


def read_template():
    """Read the HTML template."""
    return TEMPLATE_PATH.read_text(encoding="utf-8")


def read_source(filename):
    """Read a markdown source file."""
    path = SOURCE_DIR / filename
    if not path.exists():
        print(f"  WARNING: Source file not found: {path}")
        return None
    return path.read_text(encoding="utf-8")


def process_special_blocks(md_text):
    """Process emoji-prefixed blockquotes into styled HTML blocks before markdown conversion."""

    lines = md_text.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check for blockquote start
        if line.startswith("> "):
            content = line[2:]

            # Collect multi-line blockquote
            block_lines = [content]
            j = i + 1
            while j < len(lines) and lines[j].startswith("> "):
                block_lines.append(lines[j][2:])
                j += 1

            full_content = "\n".join(block_lines)

            # Narration block (🎙️)
            if full_content.startswith("🎙️"):
                text = full_content[len("🎙️"):].strip()
                # Check for audio file
                module_match = re.search(r"module-(\d+)", md_text[:200])
                audio_html = ""
                result.append(f'<div class="narration-block"><span class="narration-icon">🎙️</span><div class="narration-text">{text}{audio_html}</div></div>\n')
                i = j
                continue

            # Tier badge (🏷️)
            if full_content.startswith("🏷️"):
                tier = full_content[len("🏷️"):].strip()
                tier_css = tier.lower().replace(" ", "-").replace("'", "")
                result.append(f'<span class="tier-badge tier-{tier_css}">{tier}</span>\n')
                i = j
                continue

            # Teaching intent (🎯)
            if full_content.startswith("🎯"):
                text = full_content[len("🎯"):].strip()
                result.append(f'<div class="teach-block">{text}</div>\n')
                i = j
                continue

            # Key takeaway (💡)
            if full_content.startswith("💡"):
                text = full_content[len("💡"):].strip()
                result.append(f'<div class="callout-block"><span class="callout-icon">💡</span> {text}</div>\n')
                i = j
                continue

            # Cycle anchor (🔄)
            if full_content.startswith("🔄"):
                text = full_content[len("🔄"):].strip()
                result.append(f'<div class="cycle-block">🔄 {text}</div>\n')
                i = j
                continue

        result.append(line)
        i += 1

    return "\n".join(result)


def convert_markdown(md_text):
    """Convert markdown to HTML with extensions."""
    md = markdown.Markdown(
        extensions=[
            FencedCodeExtension(),
            CodeHiliteExtension(css_class="highlight", guess_lang=False),
            TableExtension(),
            TocExtension(permalink=False, toc_depth="2-3"),
            MarkdownInHtmlExtension(),
        ]
    )
    html = md.convert(md_text)
    toc = md.toc
    return html, toc


def embed_images(html, no_embed=False):
    """Replace image src paths with base64 data URIs."""
    if no_embed:
        return html

    def replace_img(match):
        src = match.group(1)
        # Resolve relative to images dir
        if src.startswith("../images/"):
            img_path = IMAGES_DIR / src[len("../images/"):]
        elif src.startswith("images/"):
            img_path = IMAGES_DIR / src[len("images/"):]
        else:
            img_path = PROJECT_ROOT / src

        if img_path.exists():
            ext = img_path.suffix.lower()
            mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
                    "gif": "image/gif", "svg": "image/svg+xml", "webp": "image/webp"}.get(ext.lstrip("."), "image/png")
            data = base64.b64encode(img_path.read_bytes()).decode("utf-8")
            return f'src="data:{mime};base64,{data}"'
        return match.group(0)

    return re.sub(r'src="([^"]+\.(png|jpg|jpeg|gif|svg|webp))"', replace_img, html, flags=re.IGNORECASE)


def embed_audio(html, module_file):
    """Embed audio files as base64 if they exist."""
    module_name = Path(module_file).stem
    audio_dir = AUDIO_DIR / module_name

    if not audio_dir.exists():
        return html

    # Look for manifest
    manifest_path = audio_dir / "manifest.json"
    if manifest_path.exists():
        import json
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        # Manifest is a list of entries (reference format)
        entries = manifest if isinstance(manifest, list) else manifest.get("narrations", [])
        for entry in entries:
            audio_filename = entry.get("audio_file", entry.get("file", ""))
            audio_file = audio_dir / audio_filename
            if audio_file.exists():
                data = base64.b64encode(audio_file.read_bytes()).decode("utf-8")
                audio_tag = f'<audio controls preload="none"><source src="data:audio/mpeg;base64,{data}" type="audio/mpeg"></audio>'
                # Insert audio into the next narration block that doesn't already have audio
                html = html.replace("</div></div>", f"{audio_tag}</div></div>", 1)

    return html


def paginate(html):
    """Split HTML at H2 boundaries into pages."""
    # Split on <h2> tags
    parts = re.split(r"(<h2[^>]*>)", html)

    pages = []
    current = ""

    for part in parts:
        if part.startswith("<h2"):
            if current.strip():
                pages.append(current)
            current = part
        else:
            current += part

    if current.strip():
        pages.append(current)

    if not pages:
        pages = [html]

    return pages


def extract_toc_from_pages(pages):
    """Build TOC entries from page content."""
    toc_entries = []
    for i, page in enumerate(pages):
        # Extract h2
        h2_match = re.search(r"<h2[^>]*>(.*?)</h2>", page, re.DOTALL)
        if h2_match:
            title = re.sub(r"<[^>]+>", "", h2_match.group(1)).strip()
            toc_entries.append({"title": title, "page": i, "level": 2})

        # Extract h3s
        for h3_match in re.finditer(r"<h3[^>]*>(.*?)</h3>", page, re.DOTALL):
            title = re.sub(r"<[^>]+>", "", h3_match.group(1)).strip()
            toc_entries.append({"title": title, "page": i, "level": 3})

    return toc_entries


def build_toc_html(toc_entries):
    """Build sidebar TOC HTML grouped by page."""
    html = '<ul class="toc-list">\n'
    current_group_open = False

    for entry in toc_entries:
        if entry["level"] == 2:
            # Close previous group if open
            if current_group_open:
                html += '  </ul>\n</li>\n'
            html += f'<li class="toc-page-group" data-toc-page="{entry["page"]}">\n'
            html += f'  <a href="#" data-page="{entry["page"]}" class="toc-h2-link">{entry["title"]}</a>\n'
            html += '  <ul class="toc-subsections">\n'
            current_group_open = True
        elif entry["level"] == 3 and current_group_open:
            html += f'    <li><a href="#" data-page="{entry["page"]}" class="toc-h3-link">{entry["title"]}</a></li>\n'

    if current_group_open:
        html += '  </ul>\n</li>\n'

    html += '</ul>\n'
    return html


def split_merged_blockquotes(html):
    """Split <blockquote> elements containing multiple <p> tags when any paragraph
    starts with a recognized emoji marker. Python-Markdown merges adjacent > lines
    into a single blockquote, which prevents the emoji processors from matching."""
    marker_re = re.compile(
        r"[\U0001F3F7\uFE0F\U0001F3AF\U0001F399\uFE0F\U0001F504\U0001F4A1]"
    )

    def split_one(match):
        inner = match.group(1)
        # Split on paragraph boundaries
        paragraphs = re.split(r"</p>\s*<p>", inner)
        if len(paragraphs) <= 1:
            return match.group(0)
        # Check if any paragraph contains a marker emoji
        has_marker = any(marker_re.search(p) for p in paragraphs)
        if not has_marker:
            return match.group(0)
        # Rewrap each paragraph in its own blockquote
        result = []
        for p in paragraphs:
            # Ensure proper <p> wrapping
            text = p.strip()
            if not text.startswith("<p>"):
                text = "<p>" + text
            if not text.endswith("</p>"):
                text = text + "</p>"
            result.append(f"<blockquote>\n{text}\n</blockquote>")
        return "\n".join(result)

    return re.sub(
        r"<blockquote>\s*(.*?)\s*</blockquote>",
        split_one,
        html,
        flags=re.DOTALL,
    )


def generate_quiz_html(module_num, module_slug):
    """Generate interactive quiz HTML from a quiz JSON file."""
    import json as _json

    quiz_dir = QUIZ_DIR / f"Day_{module_num:02d}_Quiz_File"
    quiz_path = quiz_dir / f"day_{module_num:02d}_quiz.json"

    if not quiz_path.exists():
        return ""

    quiz_data = _json.loads(quiz_path.read_text(encoding="utf-8"))
    title = quiz_data.get("quiz_title", f"Day {module_num} Quiz")
    passing = quiz_data.get("passing_score", 20)
    total = quiz_data.get("total_questions", 25)
    questions = quiz_data.get("questions", [])

    if not questions:
        return ""

    html = f'<h2 id="quiz">Knowledge Check: {title}</h2>\n'
    html += '<div class="quiz-container">\n'
    html += f'<p class="quiz-meta">{total} questions &middot; {passing} to pass &middot; 45 seconds per question</p>\n'

    # Status bar
    html += '<div class="quiz-status-bar">\n'
    html += '  <span id="quizStatusScore">Score: 0 / 0</span>\n'
    html += '  <span id="quizStatusProgress">0 of ' + str(total) + ' answered</span>\n'
    html += '  <span class="quiz-timer" id="quizTimer">45s</span>\n'
    html += '</div>\n'

    # Progress bar
    html += '<div class="quiz-progress-track"><div class="quiz-progress-fill" id="quizProgressFill" style="width:0%"></div></div>\n'

    html += f'<script type="application/json" id="quizData">{{"moduleSlug":"{module_slug}","passingScore":{passing},"totalQuestions":{total}}}</script>\n'
    html += '<div id="quizForm">\n'

    for q in questions:
        qid = q["id"]
        answer = q["answer"]
        html += f'<div class="quiz-question" data-answer="{answer}" style="display:none">\n'
        html += f'  <div class="quiz-question-number">Question {qid}</div>\n'
        html += f'  <div class="quiz-question-text">{q["question"]}</div>\n'
        html += '  <ul class="quiz-options">\n'
        for opt in q["options"]:
            html += f'    <li><label><input type="radio" name="q{qid}" value="{opt}"> {opt}</label></li>\n'
        html += '  </ul>\n'
        html += '  <div class="quiz-feedback-text"></div>\n'
        html += '</div>\n'

    html += '</div>\n'
    html += '<button type="button" class="quiz-action-btn" id="quizActionBtn" disabled>Submit Answer</button>\n'
    html += '<div id="quizResults" class="quiz-results">\n'
    html += '  <div class="quiz-score" id="quizScore"></div>\n'
    html += '  <div class="quiz-pct" id="quizScorePct"></div>\n'
    html += '  <div class="quiz-label" id="quizLabel"></div>\n'
    html += '  <div class="quiz-detail" id="quizDetail"></div>\n'
    html += '  <button type="button" id="quizRetryBtn" class="quiz-retry-btn">Retake Quiz</button>\n'
    html += '</div>\n'
    html += '</div>\n'

    return html


def build_module(module_info, module_index, all_modules, template, no_embed=False):
    """Build a single module HTML file."""
    filename = module_info["file"]
    print(f"  Building {filename}...")

    md_text = read_source(filename)
    if md_text is None:
        return False

    # Process special blocks first
    processed = process_special_blocks(md_text)

    # Convert markdown to HTML
    html_content, _ = convert_markdown(processed)

    # Split merged blockquotes so emoji processors can match each marker
    html_content = split_merged_blockquotes(html_content)

    # Embed images
    html_content = embed_images(html_content, no_embed)

    # Embed audio
    html_content = embed_audio(html_content, filename)

    # Append quiz if available
    module_slug = Path(filename).stem
    module_num_match = re.search(r"module-(\d+)", module_slug)
    if module_num_match:
        module_num = int(module_num_match.group(1))
        quiz_html = generate_quiz_html(module_num, module_slug)
        if quiz_html:
            html_content += quiz_html

    # Paginate at H2 boundaries
    pages = paginate(html_content)

    # Build page HTML
    pages_html = ""
    for i, page in enumerate(pages):
        active = " active" if i == 0 else ""
        pages_html += f'<div class="page{active}" id="page-{i}">\n{page}\n</div>\n'

    # Build TOC
    toc_entries = extract_toc_from_pages(pages)
    toc_html = build_toc_html(toc_entries)

    # Module navigation
    prev_html = ""
    next_html = ""
    if module_index > 0:
        prev_mod = all_modules[module_index - 1]
        prev_file = Path(prev_mod["file"]).stem + ".html"
        prev_html = f'<a href="{prev_file}">← {prev_mod["short"]}: {prev_mod["title"]}</a>'
    else:
        prev_html = '<a href="../index.html">← Course Home</a>'

    if module_index < len(all_modules) - 1:
        next_mod = all_modules[module_index + 1]
        next_file = Path(next_mod["file"]).stem + ".html"
        next_html = f'<a href="{next_file}">{next_mod["short"]}: {next_mod["title"]} →</a>'
    else:
        next_html = '<a href="../index.html">Course Home →</a>'

    # Fill template
    module_id = Path(filename).stem
    output = template.replace("{{MODULE_TITLE}}", f'{module_info["short"]}: {module_info["title"]}')
    output = output.replace("{{TOC}}", toc_html)
    output = output.replace("{{CONTENT}}", pages_html)
    output = output.replace("{{PREV_MODULE}}", prev_html)
    output = output.replace("{{NEXT_MODULE}}", next_html)
    output = output.replace("{{MODULE_ID}}", module_id)

    # Write output
    HTML_DIR.mkdir(parents=True, exist_ok=True)
    output_path = HTML_DIR / f"{module_id}.html"
    output_path.write_text(output, encoding="utf-8")
    print(f"    → {output_path}")
    return True


def build_index(modules):
    """Build the landing page (index.html)."""
    print("  Building index.html...")

    # Group modules by tier
    tiers = {}
    for m in modules:
        tier = m["tier"]
        if tier not in tiers:
            tiers[tier] = []
        tiers[tier].append(m)

    tier_order = ["Start Here", "Useful Soon", "When You're Ready", "Advanced"]

    cards_html = ""
    for tier in tier_order:
        if tier not in tiers:
            continue
        cards_html += f'<h2 class="tier-section-title"><span class="tier-badge tier-{tier.lower().replace(" ", "-").replace(chr(39), "")}">{tier}</span></h2>\n'
        cards_html += '<div class="module-grid">\n'
        for m in tiers[tier]:
            slug = Path(m["file"]).stem
            href = f'html/{slug}.html'
            cards_html += f"""<a href="{href}" class="module-card" data-module-slug="{slug}">
    <div class="module-card-title">{m['short']}</div>
    <div class="module-card-desc">{m['title']}</div>
    <span class="quiz-badge not-taken" data-quiz-badge>Quiz</span>
    <div class="quiz-score-line" data-quiz-score></div>
</a>\n"""
        cards_html += "</div>\n"

    index_html = f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Git Fundamentals — Course Home</title>
    <style>
        :root {{
            --bg: #ffffff;
            --bg-secondary: #f8f9fa;
            --text: #1a1a2e;
            --text-secondary: #555;
            --accent: #2563eb;
            --accent-light: #dbeafe;
            --border: #e2e8f0;
            --card-shadow: 0 2px 8px rgba(0,0,0,0.08);
            --tier-start: #22c55e;
            --tier-useful: #3b82f6;
            --tier-ready: #f59e0b;
            --tier-advanced: #ef4444;
        }}
        [data-theme="dark"] {{
            --bg: #0f172a;
            --bg-secondary: #1e293b;
            --text: #e2e8f0;
            --text-secondary: #94a3b8;
            --accent: #60a5fa;
            --accent-light: #1e3a5f;
            --border: #334155;
            --card-shadow: 0 2px 8px rgba(0,0,0,0.3);
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.7;
        }}
        .header {{
            text-align: center;
            padding: 3rem 2rem 2rem;
            background: var(--bg-secondary);
            border-bottom: 1px solid var(--border);
        }}
        .header h1 {{
            font-size: 2.5rem;
            color: var(--accent);
            margin-bottom: 0.5rem;
        }}
        .header p {{
            font-size: 1.1rem;
            color: var(--text-secondary);
            max-width: 600px;
            margin: 0 auto;
        }}
        .header-controls {{
            margin-top: 1rem;
        }}
        .header-controls button {{
            padding: 0.4rem 1rem;
            border: 1px solid var(--border);
            border-radius: 6px;
            background: var(--bg);
            color: var(--text);
            cursor: pointer;
            font-size: 0.85rem;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
        }}
        .tier-section-title {{
            margin: 2rem 0 1rem;
        }}
        .tier-badge {{
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            color: white;
        }}
        .tier-start-here {{ background: var(--tier-start); }}
        .tier-useful-soon {{ background: var(--tier-useful); }}
        .tier-when-youre-ready {{ background: var(--tier-ready); }}
        .tier-advanced {{ background: var(--tier-advanced); }}
        .module-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 1rem;
            margin-bottom: 1rem;
        }}
        .module-card {{
            display: block;
            padding: 1.25rem;
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            border-radius: 10px;
            text-decoration: none;
            color: var(--text);
            transition: all 0.2s;
            box-shadow: var(--card-shadow);
        }}
        .module-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(0,0,0,0.12);
            border-color: var(--accent);
        }}
        .module-card-title {{
            font-weight: 700;
            font-size: 1rem;
            color: var(--accent);
            margin-bottom: 0.3rem;
        }}
        .module-card-desc {{
            font-size: 0.9rem;
            color: var(--text-secondary);
        }}
        .quiz-badge {{
            display: inline-block;
            padding: 0.15rem 0.5rem;
            border-radius: 12px;
            font-size: 0.7rem;
            font-weight: 600;
            margin-top: 0.5rem;
        }}
        .quiz-badge.not-taken {{
            background: var(--border);
            color: var(--text-secondary);
        }}
        .quiz-badge.passed {{
            background: #22c55e;
            color: white;
        }}
        .quiz-badge.failed {{
            background: #ef4444;
            color: white;
        }}
        [data-theme="dark"] .quiz-badge.not-taken {{
            background: #334155;
            color: #94a3b8;
        }}
        .quiz-score-line {{
            font-size: 0.75rem;
            color: var(--text-secondary);
            margin-top: 0.2rem;
        }}
        .footer {{
            text-align: center;
            padding: 2rem;
            color: var(--text-secondary);
            font-size: 0.85rem;
            border-top: 1px solid var(--border);
            margin-top: 2rem;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Git Fundamentals</h1>
        <p>A 15-day hands-on course taking you from zero to confident with Git.</p>
        <div class="header-controls">
            <button onclick="toggleTheme()" id="themeBtn">🌙 Dark Mode</button>
        </div>
    </div>
    <div class="container">
        {cards_html}
    </div>
    <div class="footer">
        Git Fundamentals — Stonewaters Consulting Internship Curriculum
    </div>
    <script>
        function toggleTheme() {{
            const html = document.documentElement;
            const isDark = html.getAttribute('data-theme') === 'dark';
            html.setAttribute('data-theme', isDark ? 'light' : 'dark');
            document.getElementById('themeBtn').textContent = isDark ? '🌙 Dark Mode' : '☀️ Light Mode';
            localStorage.setItem('git-fundamentals-theme', isDark ? 'light' : 'dark');
        }}
        const savedTheme = localStorage.getItem('git-fundamentals-theme');
        if (savedTheme) {{
            document.documentElement.setAttribute('data-theme', savedTheme);
            document.getElementById('themeBtn').textContent = savedTheme === 'dark' ? '☀️ Light Mode' : '🌙 Dark Mode';
        }}

        // Update quiz badges from localStorage
        (function() {{
            var results = JSON.parse(localStorage.getItem('git-fundamentals-quiz-results') || '{{}}');
            document.querySelectorAll('.module-card[data-module-slug]').forEach(function(card) {{
                var slug = card.getAttribute('data-module-slug');
                var badge = card.querySelector('[data-quiz-badge]');
                var scoreLine = card.querySelector('[data-quiz-score]');
                if (!badge || !results[slug]) return;
                var r = results[slug];
                if (r.passed) {{
                    badge.className = 'quiz-badge passed';
                    badge.textContent = 'Passed';
                }} else {{
                    badge.className = 'quiz-badge failed';
                    badge.textContent = 'Retry';
                }}
                if (scoreLine) {{
                    scoreLine.textContent = r.score + '/' + r.total + ' correct';
                }}
            }});
        }})();
    </script>
</body>
</html>"""

    index_path = PROJECT_ROOT / "index.html"
    index_path.write_text(index_html, encoding="utf-8")
    print(f"    → {index_path}")


def main():
    parser = argparse.ArgumentParser(description="Build the Git Fundamentals course")
    parser.add_argument("--module", help="Build only this module (e.g., module-01-what-is-git)")
    parser.add_argument("--no-embed", action="store_true", help="Don't embed images as base64")
    args = parser.parse_args()

    print("Git Fundamentals Course Builder")
    print("=" * 40)

    template = read_template()

    all_modules = MODULES

    if args.module:
        # Build single module
        target = [m for m in all_modules if Path(m["file"]).stem == args.module]
        if not target:
            print(f"Module not found: {args.module}")
            sys.exit(1)
        idx = all_modules.index(target[0])
        build_module(target[0], idx, all_modules, template, args.no_embed)
    else:
        # Build all modules
        success = 0
        for i, mod in enumerate(all_modules):
            if build_module(mod, i, all_modules, template, args.no_embed):
                success += 1

        print(f"\nBuilt {success}/{len(all_modules)} modules")

        # Build index
        build_index(all_modules)

    print("\nDone!")


if __name__ == "__main__":
    main()
