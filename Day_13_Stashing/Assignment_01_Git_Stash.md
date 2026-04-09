# Day 13 Assignment: Git Stash

## Overview

- **Topic:** Saving Work in Progress with `git stash`
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

Sometimes you're in the middle of work and need to switch branches — but your changes aren't ready to commit. **`git stash`** saves your uncommitted changes to a temporary storage area and restores a clean working directory.

Key commands:

| Command | Purpose |
|---------|---------|
| `git stash` | Save all uncommitted changes |
| `git stash push -m "message"` | Save with a descriptive message |
| `git stash list` | Show all stashes |
| `git stash pop` | Apply the most recent stash and remove it from the list |
| `git stash apply` | Apply the most recent stash but keep it in the list |
| `git stash drop` | Delete the most recent stash |
| `git stash clear` | Delete ALL stashes |
| `git stash show` | Show a summary of what's in the stash |
| `git stash show -p` | Show the full diff of the stash |

Stashes are stored in a stack (LIFO — last in, first out). The most recent stash is `stash@{0}`.

---

## Part 1: Basic Stashing

### Task A: Set Up

```bash
mkdir ~/stash-practice
cd ~/stash-practice
git init
echo "# Stash Practice" > README.md
git add README.md
git commit -m "Initial commit"
```

### Task B: Stash Uncommitted Work

Start making changes but don't commit:

```bash
echo "Work in progress..." > wip.txt
echo "Modified readme" >> README.md
git status
```

You have an untracked file and a modified tracked file. Stash everything:

```bash
git stash push -m "WIP: working on new feature" --include-untracked
git status
```

The working directory is clean again. Your changes are safely saved.

> **Note:** `--include-untracked` (or `-u`) is needed to stash untracked files too. Without it, only tracked modified files are stashed.

### Task C: View the Stash

```bash
git stash list
git stash show
git stash show -p
```

- `list` shows all stashes with their messages
- `show` shows a summary (files changed, insertions, deletions)
- `show -p` shows the full diff

---

## Part 2: Restoring Stashed Work

### Task D: Pop the Stash

```bash
git stash pop
git status
ls
```

Your changes are back. `pop` applies the stash AND removes it from the list:

```bash
git stash list
```

The list should be empty.

### Task E: Stash and Apply (Without Removing)

```bash
git stash push -m "Same WIP again" --include-untracked
git stash apply
git status
git stash list
```

Unlike `pop`, `apply` keeps the stash in the list. This is useful if you want to apply the same stash to multiple branches.

Clean up:

```bash
git stash drop
git stash list
```

---

## Part 3: Multiple Stashes

### Task F: Create Multiple Stashes

Commit current work first, then create several stashes:

```bash
git add .
git commit -m "Add WIP files"

echo "Change set A" > changes-a.txt
git stash push -m "Feature A changes" --include-untracked

echo "Change set B" > changes-b.txt
git stash push -m "Feature B changes" --include-untracked

echo "Change set C" > changes-c.txt
git stash push -m "Feature C changes" --include-untracked
```

### Task G: List and Apply Specific Stashes

```bash
git stash list
```

You should see three stashes numbered `stash@{0}` through `stash@{2}`. Apply a specific one:

```bash
git stash apply stash@{1}
ls
git status
```

This applies "Feature B changes" without removing it from the list.

Clean up:

```bash
git checkout -- .
rm -f changes-b.txt
git stash clear
git stash list
```

---

## Part 4: Stashing for Branch Switching

### Task H: The Real-World Use Case

This is the most common reason to stash — you're working on something and need to switch branches:

```bash
git switch -c feature-new
echo "Started a new feature" > new-feature.txt
echo "Additional modifications" >> README.md
git status
```

Suddenly you need to fix a bug on `main`. You can't switch branches with uncommitted changes that conflict:

```bash
git stash push -m "Pausing feature-new work" --include-untracked
git switch main
```

Fix the "bug":

```bash
echo "Bug fix applied" > bugfix.txt
git add bugfix.txt
git commit -m "Fix critical bug"
```

Go back to your feature and restore:

```bash
git switch feature-new
git stash pop
git status
ls
```

Your work in progress is exactly where you left it. Commit and finish:

```bash
git add .
git commit -m "Complete new feature"
git log --oneline --all --graph
```

---

## Submission

Save a file named `Day_13_Output.md` in this folder containing the terminal output from each task.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Changes stashed with a descriptive message | 10 |
| Stash inspected with `list`, `show`, and `show -p` | 15 |
| Stash restored with `pop` (removed from list) | 15 |
| Stash restored with `apply` (kept in list) | 10 |
| Multiple stashes created and specific one applied | 20 |
| Stash used to switch branches mid-work | 20 |
| Stash list cleaned up | 10 |
| **Total** | **100** |
