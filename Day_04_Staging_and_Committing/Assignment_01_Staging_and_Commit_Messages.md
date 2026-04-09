# Day 4 Assignment: Staging and Commit Messages

## Overview

- **Topic:** Advanced Staging Techniques and Writing Good Commit Messages
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

### Staging Strategies

You've used `git add <file>` and `git add .`, but there are more precise ways to stage:

| Command | What It Does |
|---------|-------------|
| `git add <file>` | Stage one file |
| `git add <dir>/` | Stage all changes in a directory |
| `git add .` | Stage everything in the current directory and below |
| `git add *.txt` | Stage all `.txt` files |
| `git add -p` | Interactively choose which hunks to stage |
| `git reset HEAD <file>` | Unstage a file (keep the changes in working directory) |

### Good Commit Messages

A good commit message explains **why** a change was made, not just what was changed. The convention is:

```
Short summary (50 characters or less)

Optional longer description wrapped at 72 characters.
Explains the motivation and context for the change.
```

**Good messages:**
- `Fix off-by-one error in loop boundary check`
- `Add input validation to user registration form`
- `Remove deprecated API endpoint /v1/users`

**Bad messages:**
- `fix bug` (which bug?)
- `update files` (which files? why?)
- `asdf` (meaningless)

---

## Part 1: Precise Staging

Use your `git-project` repository from Day 3.

### Task A: Stage by Directory

```bash
cd ~/git-project
echo "package main;" > src/Helper.java
echo "package main;" > src/Utils.java
echo "Setup guide" > docs/setup.md
git status
```

Stage only the `src/` directory:

```bash
git add src/
git status
```

Notice `docs/setup.md` is still unstaged. Commit just the source files:

```bash
git commit -m "Add Helper and Utils source files"
```

Then stage and commit the docs separately:

```bash
git add docs/
git commit -m "Add setup documentation"
```

### Task B: Stage by Pattern

```bash
echo "test output 1" > test_results_unit.txt
echo "test output 2" > test_results_integration.txt
echo "notes" > meeting_notes.txt
git status
```

Stage only the test result files using a wildcard:

```bash
git add test_results_*.txt
git status
```

Only the two test files should be staged. `meeting_notes.txt` remains untracked.

```bash
git commit -m "Add test result files"
git add meeting_notes.txt
git commit -m "Add meeting notes"
```

---

## Part 2: Unstaging Files

### Task C: Unstage a File

```bash
echo "line 1" > temp1.txt
echo "line 2" > temp2.txt
git add temp1.txt temp2.txt
git status
```

Both files are staged. Now unstage `temp2.txt`:

```bash
git restore --staged temp2.txt
git status
```

`temp1.txt` should still be staged, but `temp2.txt` is back to untracked.

```bash
git commit -m "Add temp1 only"
```

### Task D: Unstage Everything

```bash
echo "a" > alpha.txt
echo "b" > beta.txt
echo "c" > gamma.txt
git add .
git status
```

Unstage everything:

```bash
git restore --staged .
git status
```

All files are back to untracked. Nothing was lost — the files still exist, they're just not staged.

---

## Part 3: Multi-Line Commit Messages

### Task E: Write a Detailed Commit Message

Stage the remaining files and write a multi-line commit message:

```bash
git add temp2.txt alpha.txt beta.txt gamma.txt
git commit -m "Add remaining scratch files

These files were created during staging practice.
They include temp2, alpha, beta, and gamma text files
used to demonstrate selective staging and unstaging."
```

### Task F: View the Full Message

```bash
git log -1
```

You should see the full multi-line message. Compare with the compact view:

```bash
git log --oneline -5
```

The one-line format only shows the first line — that's why the first line matters most.

---

## Part 4: Amending Commits

### Task G: Fix a Commit Message

Sometimes you make a typo in a commit message. You can fix the most recent commit:

```bash
echo "important file" > critical.txt
git add critical.txt
git commit -m "Add critcal file"
```

Oops — typo! Fix it:

```bash
git commit --amend -m "Add critical file"
git log --oneline -3
```

The old message is replaced. The commit hash also changes.

### Task H: Add a Forgotten File to the Last Commit

```bash
echo "also important" > critical2.txt
git add critical2.txt
git commit --amend --no-edit
git log --oneline -3
```

The `--no-edit` flag keeps the same message. Now the last commit includes both `critical.txt` and `critical2.txt`.

> **Warning:** Only amend commits that haven't been pushed to a shared remote. Amending rewrites history, which causes problems for collaborators.

---

## Submission

Save a file named `Day_04_Output.md` in this folder containing the terminal output from each task.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Files staged by directory | 15 |
| Files staged by wildcard pattern | 15 |
| File unstaged with `git restore --staged` | 15 |
| All files unstaged at once | 10 |
| Multi-line commit message written and viewed | 15 |
| Commit message amended to fix typo | 15 |
| Forgotten file added to last commit with `--amend` | 15 |
| **Total** | **100** |
