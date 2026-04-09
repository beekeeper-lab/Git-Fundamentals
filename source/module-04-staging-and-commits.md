# Module 4: Advanced Staging and Commit Messages

## Introduction

> 🎙️ You know the basics of staging and committing. Today we level up — you'll learn precise staging techniques, how to unstage files, how to write professional commit messages, and how to fix mistakes with amend. By the end of today, you'll be in full control of what goes into each commit.

> 🏷️ Start Here

> 🎯 **Teach:** Advanced staging techniques and how to write good commit messages.
> **See:** Files staged by directory, by pattern, unstaged, and commits amended.
> **Feel:** In full control of what goes into each commit.

## Staging Strategies

> 🎯 **Teach:** Beyond single-file staging — you can stage by directory, by wildcard pattern, or stage everything at once.
> **See:** A command reference table showing `git add <file>`, `git add <dir>/`, `git add .`, `git add *.txt`, and `git restore --staged`.
> **Feel:** Equipped with a full toolkit for any staging scenario.

> 🎙️ So far you've been staging files one at a time. That works, but when you have a project with dozens of files organized into directories, you need faster tools. Here's your toolkit — staging by file, by directory, by pattern, and even unstaging when you change your mind.

| Command | What It Does |
|---------|-------------|
| `git add <file>` | Stage one file |
| `git add <dir>/` | Stage all changes in a directory |
| `git add .` | Stage everything in the current directory and below |
| `git add *.txt` | Stage all `.txt` files |
| `git reset HEAD <file>` | Unstage a file (keep the changes) |

> 🔄 **Where this fits:** These staging and commit techniques are daily tools. The better your commits, the more useful your history becomes for your future self and your teammates.

## Stage by Directory

> 🎯 **Teach:** Staging an entire directory at once groups related files into a single, focused commit.
> **See:** Adding files to `src/` and `docs/`, then staging and committing each directory separately.
> **Feel:** Efficient — you can handle batches of related files in one move.

> 🎙️ When you have a directory full of related files, you can stage the entire directory at once. This is great for when you've added several source files that belong together in one commit. Let's try it with the `src/` and `docs/` directories.

Use your `git-project` repository from Day 3.

```bash
cd ~/git-project
echo "package main;" > src/Helper.java
echo "package main;" > src/Utils.java
echo "Setup guide" > docs/setup.md
git status
git add src/
git status
git commit -m "Add Helper and Utils source files"
git add docs/
git commit -m "Add setup documentation"
```

## Stage by Pattern

> 🎯 **Teach:** Wildcard patterns like `*.txt` let you stage files that share a naming convention.
> **See:** `git add test_results_*.txt` staging matching files while leaving `meeting_notes.txt` unstaged.
> **Feel:** Precise — pattern staging gives you surgical control over large batches of files.

> 🎙️ Wildcard patterns let you stage files that share a naming convention. For example, `git add test_results_*.txt` stages all files that start with "test_results_" and end with ".txt". This is handy when you have a batch of related files with predictable names.

```bash
echo "test output 1" > test_results_unit.txt
echo "test output 2" > test_results_integration.txt
echo "notes" > meeting_notes.txt
git add test_results_*.txt
git status
git commit -m "Add test result files"
git add meeting_notes.txt
git commit -m "Add meeting notes"
```

## Unstage a Single File

> 🎯 **Teach:** `git restore --staged <file>` removes a file from staging without losing your changes.
> **See:** Staging two files, unstaging one, and committing only the file you intended.
> **Feel:** Safe — you can always undo a staging mistake without losing any work.

> 🎙️ Sometimes you stage something by accident. No problem — you can unstage files without losing any work. The changes stay in your working directory; they're just no longer queued for the next commit. Think of it as taking something out of the box before you seal it.

```bash
echo "line 1" > temp1.txt
echo "line 2" > temp2.txt
git add temp1.txt temp2.txt
git status
git restore --staged temp2.txt
git status
git commit -m "Add temp1 only"
```

## Unstage Everything

> 🎯 **Teach:** `git restore --staged .` unstages all files at once — a clean reset of the staging area.
> **See:** Staging three files, then unstaging them all in one command with `git status` before and after.
> **Feel:** Relieved — even a bulk staging mistake is one command away from being undone.

> 🎙️ What if you staged a bunch of files and want to start over? You can unstage everything at once with `git restore --staged .` — the dot means "everything." Your files are still there, still modified, just no longer staged. Nothing is lost.

```bash
echo "a" > alpha.txt
echo "b" > beta.txt
echo "c" > gamma.txt
git add .
git restore --staged .
git status
```

All files are back to untracked. Nothing was lost.

> 💡 **Remember this one thing:** `git restore --staged <file>` removes a file from the staging area without deleting it. Your work is safe — it just won't be in the next commit.

## What Makes a Good Commit Message?

> 🎯 **Teach:** A good commit message explains *why* a change was made, with a short summary line under 50 characters.
> **See:** Side-by-side examples of good vs. bad commit messages and the recommended format.
> **Feel:** Motivated to write messages your future self will thank you for.

> 🎙️ Let's talk about commit messages. A good commit message explains why a change was made, not just what was changed. The first line is like a subject line in an email — short and clear. Think of your commit messages as notes to your future self. Six months from now, "fix bug" tells you nothing, but "Fix off-by-one error in loop boundary check" tells you everything.

A good commit message explains **why** a change was made:

```
Short summary (50 characters or less)

Optional longer description wrapped at 72 characters.
Explains the motivation and context for the change.
```

**Good:** `Fix off-by-one error in loop boundary check`
**Bad:** `fix bug`

## Write a Multi-Line Commit Message

> 🎯 **Teach:** Multi-line messages let you add context below the summary — great for complex changes.
> **See:** Writing a commit with a summary line, blank line, and detailed description paragraph.
> **Feel:** Professional — your commits now carry the context that teams rely on.

> 🎙️ When a single line isn't enough, Git supports multi-line messages. The first line is the summary — keep it under 50 characters. Then leave a blank line and add as much detail as you need. This is common in professional projects where context matters.

```bash
git add temp2.txt alpha.txt beta.txt gamma.txt
git commit -m "Add remaining scratch files

These files were created during staging practice.
They include temp2, alpha, beta, and gamma text files
used to demonstrate selective staging and unstaging."
```

## View the Full Message

> 🎯 **Teach:** `git log -1` shows the full message while `git log --oneline` shows only the summary line.
> **See:** The same commit displayed in full format and in compact one-line format.
> **Feel:** Clear on why the first line of your commit message matters most.

> 🎙️ Let's see how that multi-line message looks in the log. The regular `git log` shows the full message, while `git log --oneline` only shows the first line. That's why the first line matters most — it's what people see in the compact view.

```bash
git log -1
git log --oneline -5
```

The one-line format only shows the first line — that's why the first line matters most.

## Fix a Commit Message with Amend

> 🎯 **Teach:** `git commit --amend -m "new message"` replaces the most recent commit's message.
> **See:** Committing with a typo ("critcal"), then amending it to the correct spelling ("critical").
> **Feel:** Relieved — typos in commit messages are a quick fix, not permanent mistakes.

> 🎙️ Made a typo in your commit message? The `--amend` flag lets you fix the most recent commit's message. Watch — we'll intentionally misspell "critical" and then fix it. The old commit is replaced with a corrected one.

```bash
echo "important file" > critical.txt
git add critical.txt
git commit -m "Add critcal file"
git commit --amend -m "Add critical file"
git log --oneline -3
```

## Add a Forgotten File with Amend

> 🎯 **Teach:** `--amend` can also add forgotten files to the previous commit, as if they were always there.
> **See:** Staging `critical2.txt` and amending it into the last commit with `--no-edit`.
> **Feel:** Resourceful — amend saves you from cluttering your history with "oops, forgot this file" commits.

> 🎙️ Amend isn't just for fixing messages. If you forgot to include a file in your last commit, you can stage it and then amend. Git combines the new staged changes with the previous commit, as if the file was always there. Very handy.

```bash
echo "also important" > critical2.txt
git add critical2.txt
git commit --amend --no-edit
```

## The Amend Warning

> 🎯 **Teach:** Amending rewrites history — only use it on commits that haven't been pushed to a shared remote.
> **See:** The safety warning about amend replacing commits with new hashes.
> **Feel:** Cautious and informed — you know when amend is safe and when it's not.

> 🎙️ One important safety note about amend: only use it on commits that haven't been pushed to a shared remote. Amending rewrites history — it replaces the old commit with a new one that has a different hash. If others have already pulled the original commit, amending it will cause confusion. We'll cover this more when we get to remote repositories.

> **Warning:** Only amend commits that haven't been pushed to a shared remote. Amending rewrites history.

## Submission

> 🎯 **Teach:** How to save your work as proof of completion and what the grading rubric expects.
> **See:** The rubric covering directory staging, pattern staging, unstaging, multi-line messages, and amending.
> **Feel:** Prepared and clear on exactly what to submit.

> 🎙️ Excellent work today! You now have precise control over staging and professional-grade commit messages. Save your terminal output and check each item against the rubric below.

Save a file named `Day_04_Output.md` containing the terminal output from each task.

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
