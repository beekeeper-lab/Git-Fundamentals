# Day 9 Assignment: Clone, Fetch, and Pull

## Overview

- **Topic:** Cloning Repositories, Fetching Updates, and Pulling Changes
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

### Clone vs. Fork

- **`git clone`** — Makes a local copy of a remote repository on your machine
- **Fork** — A GitHub feature that creates a copy of someone else's repo under your own GitHub account

### Fetch vs. Pull

- **`git fetch`** — Downloads new data from the remote but does NOT modify your working files. Safe to run anytime.
- **`git pull`** — Does a `git fetch` PLUS a `git merge`. It updates your local branch with remote changes.

```
git pull = git fetch + git merge
```

The safer workflow is to `fetch` first, inspect the changes, then `merge` manually. But `git pull` is convenient for simple cases.

---

## Part 1: Cloning

### Task A: Clone Your Own Repository

Clone the repository you pushed to GitHub on Day 8 into a second location to simulate a second developer:

```bash
cd ~
git clone https://github.com/YOUR-USERNAME/git-fundamentals-practice.git git-practice-clone
cd git-practice-clone
```

### Task B: Inspect the Clone

```bash
git log --oneline
git remote -v
git branch -a
```

The clone has the full history, `origin` is already configured, and you can see remote-tracking branches.

---

## Part 2: Simulating Collaboration

You'll use your two local copies (`merge-practice` and `git-practice-clone`) to simulate two developers working on the same repo.

### Task C: Make a Change in the Original Repo

```bash
cd ~/merge-practice
echo "New feature from developer A." > feature-a.txt
git add feature-a.txt
git commit -m "Developer A: add feature-a.txt"
git push
```

### Task D: Fetch from the Clone

```bash
cd ~/git-practice-clone
git fetch origin
git log --oneline --all
```

You should see `origin/main` has moved ahead of your local `main`. The new commit is downloaded but not yet applied to your working directory.

```bash
ls
```

`feature-a.txt` is NOT in your working directory yet — `fetch` only downloaded the data.

### Task E: Merge the Fetched Changes

```bash
git merge origin/main
ls
cat feature-a.txt
```

Now the file appears. This is the explicit fetch-then-merge workflow.

---

## Part 3: Using `git pull`

### Task F: Make Another Change from the Original

```bash
cd ~/merge-practice
echo "Another feature from developer A." > feature-a2.txt
git add feature-a2.txt
git commit -m "Developer A: add feature-a2.txt"
git push
```

### Task G: Pull from the Clone

```bash
cd ~/git-practice-clone
git pull
ls
```

`git pull` fetched and merged in one step. `feature-a2.txt` should now be in your working directory.

### Task H: Push a Change Back from the Clone

```bash
echo "Work from developer B." > feature-b.txt
git add feature-b.txt
git commit -m "Developer B: add feature-b.txt"
git push
```

### Task I: Pull into the Original

```bash
cd ~/merge-practice
git pull
ls
cat feature-b.txt
```

The change from "Developer B" is now in the original repo. This is the basic collaboration cycle: push from one side, pull from the other.

---

## Part 4: Inspect the Shared History

### Task J: View the Unified History

From either directory:

```bash
git log --oneline --graph --all
```

Both developers' commits are interleaved in the history. This is how Git enables collaboration.

---

## Submission

Save a file named `Day_09_Output.md` in this folder containing the terminal output from each task.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Repository cloned to a second location | 10 |
| Clone inspected (log, remote, branches) | 10 |
| Change pushed from original repo | 10 |
| `git fetch` run and inspected (file not yet in working dir) | 15 |
| `git merge origin/main` used to apply fetched changes | 15 |
| `git pull` used as shortcut for fetch+merge | 15 |
| Change pushed from clone back to remote | 15 |
| Shared history viewed with `git log --graph` | 10 |
| **Total** | **100** |
