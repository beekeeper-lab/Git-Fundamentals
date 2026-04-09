# Day 8 Assignment: Working with Remotes

## Overview

- **Topic:** Remote Repositories, GitHub, and `git remote`
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

A **remote** is a copy of your repository hosted on a server (like GitHub, GitLab, or Bitbucket). Remotes enable collaboration — multiple people can push and pull changes to/from the same remote.

Key concepts:
- **`origin`** — The default name for the remote you cloned from (or first added)
- **`git remote`** — Manage remote connections
- **`git push`** — Upload your commits to a remote
- **`git pull`** — Download and merge new commits from a remote
- **`git fetch`** — Download new commits WITHOUT merging

Remote-tracking branches like `origin/main` represent the state of branches on the remote the last time you communicated with it.

---

## Part 1: Create a Repository on GitHub

### Task A: Create a New GitHub Repository

1. Go to [github.com](https://github.com) and log in
2. Click the **+** button → **New repository**
3. Name it `git-fundamentals-practice`
4. Set it to **Public** (or Private if you prefer)
5. Do NOT initialize with a README (you already have a local repo)
6. Click **Create repository**

GitHub will show you setup instructions. Follow the ones for "push an existing repository."

### Task B: Connect Your Local Repo to GitHub

Use your `merge-practice` repository:

```bash
cd ~/merge-practice
git remote add origin https://github.com/YOUR-USERNAME/git-fundamentals-practice.git
```

Replace `YOUR-USERNAME` with your actual GitHub username.

Verify the remote:

```bash
git remote -v
```

You should see `origin` listed twice (once for fetch, once for push).

---

## Part 2: Pushing to a Remote

### Task C: Push Your Commits

```bash
git push -u origin main
```

The `-u` flag sets `origin/main` as the **upstream** (tracking) branch for your local `main`. You only need `-u` the first time. After this, you can just use `git push`.

Go to your GitHub repository in a browser and verify your files are there.

### Task D: Make a Change and Push Again

```bash
echo "Updated with remote practice." >> README.md
git add README.md
git commit -m "Update README with remote practice note"
git push
```

Refresh the GitHub page — the change should appear.

---

## Part 3: Managing Remotes

### Task E: Inspect Remote Details

```bash
git remote show origin
```

This shows detailed information about the remote: URLs, tracked branches, and push/pull configuration.

### Task F: Add a Second Remote

You can have multiple remotes. This is common in open-source (your fork + the original repo):

```bash
git remote add backup https://github.com/YOUR-USERNAME/git-fundamentals-practice.git
git remote -v
```

You'll see both `origin` and `backup` listed.

Remove the extra remote (it was just for demonstration):

```bash
git remote remove backup
git remote -v
```

### Task G: Rename a Remote

```bash
git remote rename origin github
git remote -v
```

Now it's called `github` instead of `origin`. Rename it back:

```bash
git remote rename github origin
git remote -v
```

---

## Part 4: Checking Remote State

### Task H: Fetch Without Merging

```bash
git fetch origin
```

This downloads any new commits from the remote but does NOT merge them. It updates your `origin/main` tracking branch.

```bash
git log --oneline --all --graph
```

You can see where `origin/main` is relative to your local `main`.

### Task I: View Remote-Tracking Branches

```bash
git branch -a
```

The `-a` flag shows all branches, including remote-tracking branches (prefixed with `remotes/origin/`).

---

## Submission

Save a file named `Day_08_Output.md` in this folder containing the terminal output from each task (you may redact your GitHub URL if desired).

## Grading Criteria

| Criteria | Points |
|----------|--------|
| GitHub repository created | 10 |
| Remote added and verified with `git remote -v` | 15 |
| First push with `-u` flag successful | 20 |
| Follow-up commit pushed to remote | 15 |
| `git remote show origin` output captured | 10 |
| Second remote added and removed | 10 |
| `git fetch` run and remote state inspected | 10 |
| Remote-tracking branches listed with `git branch -a` | 10 |
| **Total** | **100** |
