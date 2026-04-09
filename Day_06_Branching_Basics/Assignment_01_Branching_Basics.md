# Day 6 Assignment: Branching Basics

## Overview

- **Topic:** Creating, Switching, and Managing Branches
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

Branches are one of Git's most important features. A branch is simply a movable pointer to a commit. When you create a branch, Git creates a new pointer — it doesn't copy any files.

```
main:       A --- B --- C
                         \
feature:                  D --- E
```

In this diagram, `feature` branched off from `main` at commit C, then added commits D and E independently.

Key commands:

| Command | Purpose |
|---------|---------|
| `git branch` | List all local branches |
| `git branch <name>` | Create a new branch |
| `git switch <name>` | Switch to a branch |
| `git switch -c <name>` | Create and switch in one step |
| `git branch -d <name>` | Delete a branch (safe — won't delete unmerged work) |
| `git branch -m <old> <new>` | Rename a branch |

> **Note:** `git switch` is the modern replacement for `git checkout` when switching branches. You may see `checkout` in older tutorials.

---

## Part 1: Creating and Switching Branches

Use your `git-project` repository.

### Task A: See Your Current Branch

```bash
cd ~/git-project
git branch
```

The branch with the `*` next to it is your current branch (should be `main`).

### Task B: Create a New Branch

```bash
git branch feature-greeting
git branch
```

You now have two branches, but you're still on `main`. The new branch points to the same commit as `main`.

### Task C: Switch to the New Branch

```bash
git switch feature-greeting
git branch
```

The `*` should now be next to `feature-greeting`.

### Task D: Make Commits on the Branch

```bash
echo "Hello from the feature branch!" > greeting.txt
git add greeting.txt
git commit -m "Add greeting.txt on feature branch"

echo "Another feature file." > feature-notes.txt
git add feature-notes.txt
git commit -m "Add feature-notes.txt on feature branch"
```

### Task E: Switch Back to Main

```bash
git switch main
ls
```

Notice that `greeting.txt` and `feature-notes.txt` are **gone**. They only exist on the `feature-greeting` branch. Your files literally change when you switch branches.

```bash
git switch feature-greeting
ls
```

They're back. This is Git swapping your working directory to match the branch.

---

## Part 2: Multiple Branches

### Task F: Create a Second Branch from Main

```bash
git switch main
git switch -c feature-about
```

The `-c` flag creates and switches in one step. This branch starts from `main`, so it doesn't have the greeting files.

```bash
echo "About this project." > about.txt
git add about.txt
git commit -m "Add about.txt on feature-about branch"
```

### Task G: Visualize the Branches

```bash
git log --oneline --graph --all
```

You should see three branches diverging from a common point. This is how parallel development works — each branch is independent.

### Task H: List All Branches with Details

```bash
git branch -v
```

This shows each branch with its latest commit hash and message.

---

## Part 3: Renaming and Deleting Branches

### Task I: Rename a Branch

```bash
git switch main
git branch -m feature-about feature-about-page
git branch -v
```

The branch is renamed. History is unchanged.

### Task J: Attempt to Delete a Branch

```bash
git branch -d feature-about-page
```

Git will warn you that the branch has changes not yet merged into `main`. This is a safety feature.

Try force-deleting it (since this is practice):

```bash
git branch -D feature-about-page
git branch -v
```

> **Important:** `-d` is safe (refuses to delete unmerged branches). `-D` is forced deletion — use with caution.

---

## Submission

Save a file named `Day_06_Output.md` in this folder containing the terminal output from each task.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Branch created and listed | 10 |
| Switched between branches | 15 |
| Commits made on feature branch | 15 |
| Files appear/disappear when switching branches | 15 |
| Second branch created with `-c` shorthand | 10 |
| Branch graph visualized with `--graph --all` | 15 |
| Branch renamed | 10 |
| Branch deletion (safe and forced) demonstrated | 10 |
| **Total** | **100** |
