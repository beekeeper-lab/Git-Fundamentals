# Day 1 Assignment: What Is Git

## Overview

- **Topic:** Understanding Version Control and Git Fundamentals
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

**Git** is a distributed version control system (VCS). It tracks changes to files over time, letting you revisit any previous version, collaborate with others, and work on multiple features simultaneously without breaking things.

Key concepts:
- **Repository (repo):** A project tracked by Git — it contains your files plus a hidden `.git` folder with the entire history
- **Commit:** A snapshot of your project at a point in time, with a message describing what changed
- **Working directory:** The files you see and edit on disk
- **Staging area (index):** A holding area where you prepare changes before committing them
- **Branch:** An independent line of development — the default branch is usually called `main`

The basic Git workflow:
```
Edit files → Stage changes → Commit snapshot
```

---

## Part 1: Verify Your Git Installation

Open a terminal and run each of these commands. Record the output.

### Task A: Check Git Version

```bash
git --version
```

You should see something like `git version 2.x.x`. If Git is not installed, install it before continuing.

### Task B: Explore Git Help

```bash
git help
```

This prints a summary of the most common Git commands. Read through the list — you'll be using many of these over the next 15 days.

Now try getting help for a specific command:

```bash
git help init
```

This opens the manual page for `git init`. Scroll through it briefly to see how Git documents its commands, then press `q` to quit.

---

## Part 2: Configure Git

Before you can make commits, Git needs to know who you are. These settings are stored globally on your machine.

### Task C: Set Your Identity

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Replace with your actual name and email. Then verify your settings:

```bash
git config --global user.name
git config --global user.email
```

### Task D: View All Configuration

```bash
git config --list
```

This shows every Git configuration value on your machine. Look for your `user.name` and `user.email` in the output.

### Task E: Set Your Default Editor

Git sometimes opens a text editor (for commit messages, merge conflict resolution, etc.). Set it to something you're comfortable with:

```bash
git config --global core.editor "nano"
```

> **Note:** You can substitute `nano` with `vim`, `code --wait` (VS Code), or any editor you prefer.

### Task F: Set Default Branch Name

Modern convention uses `main` instead of `master` as the default branch name:

```bash
git config --global init.defaultBranch main
```

---

## Part 3: Create Your First Repository

### Task G: Initialize a Repo

Create a new directory and initialize it as a Git repository:

```bash
mkdir ~/git-practice
cd ~/git-practice
git init
```

You should see: `Initialized empty Git repository in .../git-practice/.git/`

### Task H: Explore the `.git` Directory

```bash
ls -la
ls .git
```

The `.git` folder is where Git stores everything — history, branches, configuration. You should see folders like `objects`, `refs`, `hooks`, and files like `HEAD` and `config`.

> **Important:** Never manually edit or delete files inside `.git` unless you know exactly what you're doing.

### Task I: Check Repository Status

```bash
git status
```

This is the most important Git command. It tells you what branch you're on, what's staged, what's modified, and what's untracked. Right now the repo is empty, so it should say "No commits yet" and "nothing to commit."

---

## Part 4: Your First Commit

### Task J: Create and Commit a File

Create a file, stage it, and commit it:

```bash
echo "# Git Practice" > README.md
git status
git add README.md
git status
git commit -m "Initial commit: add README"
git status
```

Pay attention to how `git status` changes at each step:
1. Before `git add` — the file is **untracked** (red)
2. After `git add` — the file is **staged** (green)
3. After `git commit` — the working tree is **clean**

### Task K: View Your Commit

```bash
git log
```

You should see your commit with its hash, author, date, and message.

---

## Submission

Save a file named `Day_01_Output.md` in this folder containing the terminal output from each task (copy and paste from your terminal).

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Git installed and version confirmed | 10 |
| Global config set (name, email, editor, default branch) | 20 |
| Repository initialized successfully | 15 |
| `.git` directory explored and contents listed | 15 |
| File created, staged, and committed | 25 |
| `git log` output shows the commit | 15 |
| **Total** | **100** |
