# Module 1: What Is Git?

## Introduction

> 🎙️ Today is day one — and by the end of it, you'll have Git installed, configured, and you'll have made your very first commit. That's a real milestone. Every Git expert started exactly where you are right now.

> 🏷️ Start Here

> 🎯 **Teach:** What version control is, what Git does, and the basic workflow.
> **See:** Git being installed, configured, and used to create a first commit.
> **Feel:** Confident that Git is approachable and that you can do this.

## What Is Version Control?

> 🎯 **Teach:** Version control tracks changes to files over time so you can revisit any previous version.
> **See:** The analogy of saving `essay_v1`, `essay_v2`, `essay_final_FINAL` — and how Git eliminates that mess.
> **Feel:** Relieved that there's a better way to manage file versions.

> 🎙️ Imagine writing an essay and saving it as `essay_v1.doc`, `essay_v2.doc`, `essay_final.doc`, `essay_final_FINAL.doc`. That's version control the hard way. Git does the same thing — but automatically, efficiently, and without cluttering your folder with duplicate files.

**Git** is a distributed version control system. It tracks changes to files over time, letting you revisit any previous version, collaborate with others, and work on multiple features simultaneously without breaking things.

## Key Concepts

> 🎯 **Teach:** The five core terms you'll use every day — repository, commit, working directory, staging area, and branch.
> **See:** Clear definitions of each term and the Edit-Stage-Commit workflow summary.
> **Feel:** Grounded in the vocabulary so nothing in today's exercises feels mysterious.

> 🎙️ Before you touch the terminal, let's build a mental model. There are five terms you'll see over and over again in Git. Don't worry about memorizing them now — you'll understand them deeply by the end of today just by using them.

- **Repository (repo):** A project tracked by Git — it contains your files plus a hidden `.git` folder with the entire history
- **Commit:** A snapshot of your project at a point in time, with a message describing what changed
- **Working directory:** The files you see and edit on disk
- **Staging area (index):** A holding area where you prepare changes before committing them
- **Branch:** An independent line of development — the default branch is usually called `main`

> 💡 **Remember this one thing:** The basic Git workflow is three steps: **Edit → Stage → Commit**. Everything else builds on this.

## Verify Your Installation

> 🎯 **Teach:** Git is installed and working on your machine.
> **See:** The `git --version` output confirming a successful installation.
> **Feel:** Ready to start — the tooling is in place and you're good to go.

> 🎙️ Before we do anything else, let's make sure Git is installed and working. Open your terminal and run this command. If Git isn't installed, you'll need to install it before continuing.

> 🔄 **Where this fits:** Installation is a one-time setup step. Once Git is on your machine, you won't need to do this again.

### Check Git Version

```bash
git --version
```

You should see something like `git version 2.x.x`.

## Explore Git Help

> 🎯 **Teach:** Git has a built-in help system you can use anytime you forget a command or want details.
> **See:** The output of `git help` and `git help init` showing command summaries and manual pages.
> **Feel:** Resourceful — you always have a reference right in your terminal.

> 🎙️ Git has a built-in help system that's actually really useful. Get in the habit of using it — when you forget a command or want to know what options are available, `git help` is your friend.

```bash
git help
```

This prints a summary of the most common Git commands. You'll be using many of these over the next 15 days.

Try getting help for a specific command:

```bash
git help init
```

Press `q` to quit the manual page.

## Configure Your Identity

> 🎯 **Teach:** Git needs your name and email attached to every commit so collaborators know who made each change.
> **See:** The `git config --global` commands setting and verifying your identity.
> **Feel:** Professional — your commits will carry your name from the very start.

> 🎙️ Before you can make commits, Git needs to know who you are. These identity settings get attached to every commit you make, so your collaborators can see who changed what. This is a one-time global setup — do it once, and you're set for every project on this machine.

### Set Your Name and Email

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Verify Your Settings

```bash
git config --global user.name
git config --global user.email
```

### View All Configuration

```bash
git config --list
```

## Set Your Editor and Default Branch

> 🎯 **Teach:** Setting your preferred editor and default branch name avoids surprises later.
> **See:** The `git config` commands for `core.editor` and `init.defaultBranch`.
> **Feel:** In control of your environment — Git is configured exactly how you want it.

> 🎙️ Two more quick settings. Git sometimes opens a text editor — for example, when you write a multi-line commit message. And the default branch name convention has changed from "master" to "main" in recent years. Let's set both of these now so you don't run into surprises later.

### Set Your Default Editor

```bash
git config --global core.editor "nano"
```

> **Note:** You can substitute `nano` with `vim`, `code --wait` (VS Code), or any editor you prefer.

### Set Default Branch Name

Modern convention uses `main` instead of `master`:

```bash
git config --global init.defaultBranch main
```

## Create Your First Repository

> 🎯 **Teach:** `git init` creates a hidden `.git` folder that turns any directory into a Git repository.
> **See:** The initialization message confirming your first repo exists.
> **Feel:** Excited — you have your very first Git repository.

> 🎙️ Now for the exciting part — creating your first Git repository. A repository is just a folder that Git is tracking. When you run `git init`, Git creates a hidden `.git` folder inside that stores all the history and metadata. This is the moment it becomes a Git project.

### Initialize a Repo

```bash
mkdir ~/git-practice
cd ~/git-practice
git init
```

You should see: `Initialized empty Git repository in .../git-practice/.git/`

## Explore the .git Directory

> 🎯 **Teach:** The `.git` folder is where Git stores your entire project history and configuration.
> **See:** The contents of `.git` — folders like `objects`, `refs`, `hooks`, and files like `HEAD`.
> **Feel:** Curious about what's under the hood, knowing you don't need to touch it yet.

> 🎙️ Let's peek behind the curtain. That `.git` folder is where Git stores everything — the entire history of your project, all the configuration, everything. You don't need to understand every file in there yet, but it's good to know it exists and what it looks like.

```bash
ls -la
ls .git
```

You should see folders like `objects`, `refs`, `hooks`, and files like `HEAD` and `config`.

> **Important:** Never manually edit or delete files inside `.git` unless you know exactly what you're doing.

## Check Repository Status

> 🎯 **Teach:** `git status` is your most-used command — it tells you the state of every file in your repo.
> **See:** The output of `git status` on a fresh, empty repository.
> **Feel:** Oriented — like having a compass that always shows where you stand.

> 🎙️ Here's the command you'll use more than any other in Git: `git status`. It tells you what branch you're on, what files are staged, what's modified, and what's untracked. Think of it as your compass — when in doubt, check status.

```bash
git status
```

> 💡 **Remember this one thing:** `git status` is the most important Git command. It tells you what branch you're on, what's staged, what's modified, and what's untracked. Use it constantly.

## Create a File

> 🎯 **Teach:** New files start as "untracked" — Git sees them but isn't managing them yet.
> **See:** Creating a `README.md` and watching `git status` report it as untracked.
> **Feel:** The start of the edit-stage-commit workflow clicking into place.

> 🎙️ Time to create your first file. We'll make a simple README and then watch how `git status` reacts. Pay close attention — this is where you'll start to see the edit-stage-commit workflow in action.

```bash
echo "# Git Practice" > README.md
git status
```

The file shows as **untracked** — Git sees it exists but isn't tracking it yet.

## Stage and Commit

> 🎯 **Teach:** The edit-stage-commit workflow — `git add` stages changes, `git commit` saves them permanently.
> **See:** `git status` changing at each step: untracked (red), staged (green), clean.
> **Feel:** The rhythm of Git clicking into place as you complete your first full cycle.

> 🎙️ This is the moment — your first commit. You're going to stage the file with `git add`, then commit it with `git commit`. Pay close attention to how `git status` changes at each step, because that's the edit-stage-commit workflow in action.

```bash
git add README.md
git status
git commit -m "Initial commit: add README"
git status
```

Pay attention to how `git status` changes at each step:
1. Before `git add` — the file is **untracked** (red)
2. After `git add` — the file is **staged** (green)
3. After `git commit` — the working tree is **clean**

## View Your First Commit

> 🎯 **Teach:** `git log` shows your commit history — the hash, author, date, and message.
> **See:** Your first commit displayed in the log with all its metadata.
> **Feel:** Proud — you just made history, literally. Your first commit is in the books.

> 🎙️ You just made history — literally. Let's look at the log to see your commit. You'll see the commit hash (a long string of letters and numbers), your name and email, the date, and the message you wrote. Every commit you ever make will have this same structure.

```bash
git log
```

You should see your commit with its hash, author, date, and message. Congratulations — you've made history (literally).

## Submission

> 🎯 **Teach:** How to save your work as proof of completion and what the grading rubric expects.
> **See:** The rubric with point values for each task you completed today.
> **Feel:** Prepared and clear on exactly what to submit.

> 🎙️ That's a wrap for Day 1! Save your terminal output to a file so you have proof of everything you did. The rubric below tells you exactly what's being graded — make sure you have output for each item.

Save a file named `Day_01_Output.md` containing the terminal output from each task.

| Criteria | Points |
|----------|--------|
| Git installed and version confirmed | 10 |
| Global config set (name, email, editor, default branch) | 20 |
| Repository initialized successfully | 15 |
| `.git` directory explored and contents listed | 15 |
| File created, staged, and committed | 25 |
| `git log` output shows the commit | 15 |
| **Total** | **100** |
