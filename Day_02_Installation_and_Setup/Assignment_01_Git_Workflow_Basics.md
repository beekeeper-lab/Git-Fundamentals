# Day 2 Assignment: Git Workflow Basics

## Overview

- **Topic:** The Edit-Stage-Commit Workflow
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

The core Git workflow has three stages:

```
Working Directory  →  Staging Area  →  Repository
   (edit files)       (git add)       (git commit)
```

- **Working directory:** Where you edit files normally
- **Staging area (index):** Where you prepare exactly which changes go into the next commit
- **Repository (.git):** Where committed snapshots are permanently stored

The staging area is what makes Git powerful — you can choose exactly which changes to include in a commit, even if you've modified multiple files.

Key commands:
| Command | Purpose |
|---------|---------|
| `git status` | See what's changed |
| `git add <file>` | Stage a file |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Commit staged changes |
| `git diff` | See unstaged changes |
| `git diff --staged` | See staged changes |

---

## Part 1: Tracking Multiple Files

Use the `git-practice` repository you created on Day 1.

### Task A: Create Multiple Files

```bash
cd ~/git-practice
echo "This is file one." > file1.txt
echo "This is file two." > file2.txt
echo "This is file three." > file3.txt
git status
```

All three files should show as **untracked**. Notice they appear in red.

### Task B: Stage Files Selectively

Stage only `file1.txt` and `file2.txt`:

```bash
git add file1.txt file2.txt
git status
```

Notice that `file1.txt` and `file2.txt` are now under "Changes to be committed" (green), while `file3.txt` is still "Untracked" (red). This is the staging area in action — you control what goes into each commit.

### Task C: Commit the Staged Files

```bash
git commit -m "Add file1 and file2"
git status
```

After the commit, only `file3.txt` remains untracked. The other two are now safely stored in Git's history.

### Task D: Stage and Commit the Remaining File

```bash
git add file3.txt
git commit -m "Add file3"
git status
```

The working tree should now be clean.

---

## Part 2: Modifying and Diffing

### Task E: Modify a Tracked File

```bash
echo "Adding a second line to file one." >> file1.txt
git status
```

The file now shows as **modified** — Git knows it changed because it's already tracked.

### Task F: View the Diff

```bash
git diff
```

This shows exactly what changed — lines starting with `+` are additions, `-` are deletions. This is one of Git's most useful features.

### Task G: Stage and Diff Again

```bash
git add file1.txt
git diff
git diff --staged
```

After staging:
- `git diff` shows **nothing** (no unstaged changes)
- `git diff --staged` shows the changes that **will** be committed

### Task H: Commit the Modification

```bash
git commit -m "Update file1 with second line"
```

---

## Part 3: Staging Partial Changes

### Task I: Make Multiple Changes, Commit Separately

Modify two files:

```bash
echo "Updated file two." >> file2.txt
echo "Updated file three." >> file3.txt
git status
```

Now stage and commit them **separately** to create two distinct commits:

```bash
git add file2.txt
git commit -m "Update file2"

git add file3.txt
git commit -m "Update file3"
```

### Task J: View the Full History

```bash
git log
```

You should see 5 commits total. Each one has a unique hash, your name, and a message.

Try a more compact format:

```bash
git log --oneline
```

This shows one line per commit — hash and message only.

---

## Submission

Save a file named `Day_02_Output.md` in this folder containing the terminal output from each task.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Multiple files created and selectively staged | 15 |
| Separate commits for different files | 15 |
| File modified, diff viewed before and after staging | 25 |
| `git diff` vs `git diff --staged` difference demonstrated | 20 |
| Multiple changes committed separately | 15 |
| `git log` and `git log --oneline` output shown | 10 |
| **Total** | **100** |
