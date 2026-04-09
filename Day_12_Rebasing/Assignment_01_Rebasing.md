# Day 12 Assignment: Rebasing

## Overview

- **Topic:** `git rebase` — Replaying Commits for a Clean History
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

**Rebasing** moves your branch's commits on top of another branch, creating a linear history instead of a merge commit.

### Merge vs. Rebase

**Merge** preserves the full branching history:
```
main:    A --- B --- E --- M
                  \       /
feature:           C --- D
```

**Rebase** replays your commits on top of main, creating a straight line:
```
Before:  main:    A --- B --- E
                           \
         feature:           C --- D

After:   main:    A --- B --- E
                               \
         feature:               C' --- D'
```

The commits `C'` and `D'` have different hashes than `C` and `D` because they now have different parent commits. The **content** is the same, but the **history** is rewritten.

### The Golden Rule

> **Never rebase commits that have been pushed to a shared remote.** Rebasing rewrites history, which causes problems for anyone else who has those commits.

Rebase is safe for local branches that haven't been pushed yet, or for personal branches that only you use.

---

## Part 1: Basic Rebase

### Task A: Set Up the Scenario

```bash
mkdir ~/rebase-practice
cd ~/rebase-practice
git init

echo "Version 1" > app.txt
git add app.txt
git commit -m "Initial commit"

echo "Version 2" >> app.txt
git add app.txt
git commit -m "Update to version 2"
```

Create a feature branch and add commits:

```bash
git switch -c feature-x
echo "Feature X - part 1" > feature-x.txt
git add feature-x.txt
git commit -m "Feature X: part 1"

echo "Feature X - part 2" >> feature-x.txt
git add feature-x.txt
git commit -m "Feature X: part 2"
```

Go back to `main` and add a commit (to create divergence):

```bash
git switch main
echo "Version 3 - hotfix" >> app.txt
git add app.txt
git commit -m "Hotfix: update to version 3"
```

### Task B: View the Divergence

```bash
git log --oneline --graph --all
```

You should see `main` and `feature-x` diverging from a common ancestor.

### Task C: Rebase the Feature Branch

```bash
git switch feature-x
git rebase main
git log --oneline --graph --all
```

After the rebase:
- The feature branch commits are now **on top of** main's latest commit
- The history is a straight line
- No merge commit was created

### Task D: Fast-Forward Merge

Since `feature-x` is now directly ahead of `main`, merging is a simple fast-forward:

```bash
git switch main
git merge feature-x
git log --oneline --graph --all
```

The result is a perfectly linear history.

```bash
git branch -d feature-x
```

---

## Part 2: Rebase with Conflicts

### Task E: Create a Rebase Conflict

```bash
git switch -c feature-y
echo "Feature Y changes this line" > conflict-file.txt
git add conflict-file.txt
git commit -m "Feature Y: add conflict-file"

git switch main
echo "Main changes this line" > conflict-file.txt
git add conflict-file.txt
git commit -m "Main: add conflict-file"
```

### Task F: Rebase and Resolve

```bash
git switch feature-y
git rebase main
```

Git will pause with a conflict. Resolve it:

```bash
git status
cat conflict-file.txt
```

Edit `conflict-file.txt` to resolve the conflict (remove the markers, choose the content). Then:

```bash
git add conflict-file.txt
git rebase --continue
```

### Task G: Verify the Result

```bash
git log --oneline --graph --all
```

The rebase completed with a clean, linear history.

---

## Part 3: Aborting a Rebase

### Task H: Start and Abort a Rebase

```bash
git switch -c feature-z
echo "Z content" > z-file.txt
git add z-file.txt
git commit -m "Feature Z: add z-file"

git switch main
echo "Main Z content" > z-file.txt
git add z-file.txt
git commit -m "Main: add z-file"

git switch feature-z
git rebase main
```

Instead of resolving, abort:

```bash
git rebase --abort
git status
git log --oneline --graph --all
```

The branch is back to its pre-rebase state. Nothing was lost.

---

## Part 4: Merge vs. Rebase Comparison

### Task I: Side-by-Side Comparison

Create two identical branches and merge one, rebase the other:

```bash
git switch main

git switch -c demo-merge
echo "Merge demo" > merge-demo.txt
git add merge-demo.txt
git commit -m "Demo merge commit"

git switch main
echo "Main progress" >> app.txt
git add app.txt
git commit -m "Main: more progress"

# Merge approach
git merge demo-merge
git log --oneline --graph -6
```

Note the merge commit. Now compare what rebase would look like:

```bash
git switch -c demo-rebase
echo "Rebase demo" > rebase-demo.txt
git add rebase-demo.txt
git commit -m "Demo rebase commit"

git switch main
echo "Even more progress" >> app.txt
git add app.txt
git commit -m "Main: even more progress"

git switch demo-rebase
git rebase main
git switch main
git merge demo-rebase
git log --oneline --graph -8
```

Compare the two sections of the graph — the rebased one has no merge commit.

---

## Submission

Save a file named `Day_12_Output.md` in this folder containing the terminal output from each task.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Diverging branches created for rebase | 10 |
| Basic rebase completed (linear history shown) | 20 |
| Fast-forward merge after rebase | 10 |
| Rebase conflict resolved with `--continue` | 20 |
| Rebase aborted with `--abort` | 10 |
| Merge vs. rebase compared side by side | 20 |
| Graph output shown at each step | 10 |
| **Total** | **100** |
