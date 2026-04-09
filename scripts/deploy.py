#!/usr/bin/env python3
"""Package the Git Fundamentals course for distribution."""

import argparse
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
HTML_DIR = PROJECT_ROOT / "html"
DIST_DIR = PROJECT_ROOT / "dist"
INDEX_PATH = PROJECT_ROOT / "index.html"


def get_version(explicit=None):
    """Generate a version string."""
    if explicit:
        return explicit

    # Try git hash + date
    date_str = datetime.now().strftime("%Y%m%d")
    try:
        git_hash = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=PROJECT_ROOT,
            stderr=subprocess.DEVNULL
        ).decode().strip()
        return f"{date_str}-{git_hash}"
    except (subprocess.CalledProcessError, FileNotFoundError):
        return date_str


def build_course():
    """Run the build script."""
    print("Building course...")
    result = subprocess.run(
        [sys.executable, str(PROJECT_ROOT / "scripts" / "build_course.py")],
        cwd=PROJECT_ROOT
    )
    if result.returncode != 0:
        print("Build failed!")
        sys.exit(1)


def package(version, out_dir=None):
    """Create a zip package."""
    if out_dir:
        dist = Path(out_dir)
    else:
        dist = DIST_DIR

    dist.mkdir(parents=True, exist_ok=True)

    folder_name = f"git-fundamentals-v{version}"
    staging = dist / folder_name

    # Clean staging
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir()

    # Copy index
    if INDEX_PATH.exists():
        shutil.copy2(INDEX_PATH, staging / "index.html")
    else:
        print("WARNING: index.html not found")

    # Copy HTML modules
    if HTML_DIR.exists():
        shutil.copytree(HTML_DIR, staging / "html")
    else:
        print("WARNING: html/ directory not found")

    # Write VERSION file
    (staging / "VERSION").write_text(
        f"Git Fundamentals\n"
        f"Version: {version}\n"
        f"Built: {datetime.now().isoformat()}\n"
    )

    # Create zip
    zip_path = dist / folder_name
    shutil.make_archive(str(zip_path), "zip", dist, folder_name)
    print(f"Package created: {zip_path}.zip")

    # Clean staging
    shutil.rmtree(staging)

    return f"{zip_path}.zip"


def main():
    parser = argparse.ArgumentParser(description="Package Git Fundamentals course")
    parser.add_argument("--version", help="Explicit version string")
    parser.add_argument("--skip-build", action="store_true", help="Skip rebuilding")
    parser.add_argument("--out", help="Output directory for zip")
    args = parser.parse_args()

    version = get_version(args.version)
    print(f"Packaging version: {version}")

    if not args.skip_build:
        build_course()

    zip_file = package(version, args.out)
    print(f"\nReady for distribution: {zip_file}")


if __name__ == "__main__":
    main()
