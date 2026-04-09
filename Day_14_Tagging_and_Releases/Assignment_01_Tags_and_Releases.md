# Day 14 Assignment: Tags and Releases

## Overview

- **Topic:** Git Tags, Semantic Versioning, and GitHub Releases
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

**Tags** are permanent markers for specific commits — typically used to mark releases (v1.0.0, v2.1.3, etc.).

### Two Types of Tags

| Type | Created With | Contains |
|------|-------------|----------|
| **Lightweight** | `git tag v1.0` | Just a name pointing to a commit |
| **Annotated** | `git tag -a v1.0 -m "message"` | Name + tagger + date + message (recommended) |

Annotated tags are preferred because they contain metadata about who created the tag and why.

### Semantic Versioning (SemVer)

Most projects follow the `MAJOR.MINOR.PATCH` convention:

```
v1.0.0 → v1.0.1 → v1.1.0 → v2.0.0
```

- **PATCH** (1.0.0 → 1.0.1) — Bug fixes, no new features
- **MINOR** (1.0.0 → 1.1.0) — New features, backwards compatible
- **MAJOR** (1.0.0 → 2.0.0) — Breaking changes

---

## Part 1: Creating Tags

### Task A: Set Up a Repo with History

```bash
mkdir ~/tag-practice
cd ~/tag-practice
git init

echo "v1 code" > app.txt
git add app.txt
git commit -m "Initial release"

echo "v1 bugfix" >> app.txt
git add app.txt
git commit -m "Fix startup bug"

echo "v1.1 feature" >> app.txt
git add app.txt
git commit -m "Add user profiles feature"

echo "v2 breaking change" >> app.txt
git add app.txt
git commit -m "Redesign API (breaking change)"
```

### Task B: Create Annotated Tags

Tag specific commits to mark releases:

```bash
git log --oneline
```

Tag the current commit (HEAD) as v2.0.0:

```bash
git tag -a v2.0.0 -m "Version 2.0.0: API redesign"
```

Tag a past commit. Get the hash of the "Add user profiles" commit and tag it:

```bash
git tag -a v1.1.0 -m "Version 1.1.0: user profiles" HEAD~1
git tag -a v1.0.1 -m "Version 1.0.1: startup bugfix" HEAD~2
git tag -a v1.0.0 -m "Version 1.0.0: initial release" HEAD~3
```

### Task C: Create a Lightweight Tag

```bash
git tag beta-test
```

No `-a` or `-m` — this creates a simple pointer with no metadata.

---

## Part 2: Working with Tags

### Task D: List and Inspect Tags

```bash
git tag
git tag -l "v1.*"
```

The `-l` flag filters tags by pattern.

Inspect an annotated tag:

```bash
git show v1.0.0
```

This shows the tag metadata AND the commit it points to. Compare with the lightweight tag:

```bash
git show beta-test
```

No tag metadata — just the commit.

### Task E: View the Log with Tags

```bash
git log --oneline --decorate
```

Tags appear in the log next to their commits.

### Task F: Check Out a Tag

```bash
git checkout v1.0.0
```

Git puts you in **detached HEAD** state — you're looking at historical code, not a branch. Look around:

```bash
cat app.txt
git log --oneline
```

Go back to your branch:

```bash
git switch main
```

---

## Part 3: Pushing Tags to a Remote

### Task G: Set Up a Remote (or Use Your Existing One)

If you still have the GitHub repo from Day 8, connect this repo:

```bash
git remote add origin https://github.com/YOUR-USERNAME/git-fundamentals-practice.git
```

Or create a new GitHub repository and connect it.

### Task H: Push Tags

Tags are NOT pushed by default with `git push`. Push them explicitly:

```bash
# Push a single tag
git push origin v1.0.0

# Push all tags at once
git push origin --tags
```

Check GitHub — the tags should appear under the "Tags" section of your repository.

### Task I: Delete a Tag

Delete locally:

```bash
git tag -d beta-test
git tag
```

Delete from the remote:

```bash
git push origin --delete beta-test
```

---

## Part 4: GitHub Releases

### Task J: Create a Release on GitHub

1. Go to your repository on GitHub
2. Click **"Releases"** on the right sidebar (or go to the Tags tab)
3. Click **"Create a new release"**
4. Choose the tag `v2.0.0`
5. Title: `Version 2.0.0`
6. Description: Write a brief changelog (what changed since v1.1.0)
7. Click **"Publish release"**

Releases are GitHub's way of packaging a tagged version with release notes, changelogs, and downloadable archives.

---

## Submission

Save a file named `Day_14_Output.md` in this folder containing the terminal output from each task and a screenshot of your GitHub release.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Annotated tags created for multiple versions | 20 |
| Lightweight tag created for comparison | 5 |
| Tags listed and filtered | 10 |
| `git show` used on annotated vs. lightweight tag | 10 |
| Tag checked out (detached HEAD) and returned to branch | 10 |
| Tags pushed to remote | 15 |
| Tag deleted locally and remotely | 10 |
| GitHub release created from a tag | 20 |
| **Total** | **100** |
