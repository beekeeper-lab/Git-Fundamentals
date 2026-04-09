# Day 5 Assignment: Exploring Git History

## Overview

- **Topic:** Using `git log`, `git show`, `git diff`, and `git blame`
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

One of Git's most powerful features is its history. Every commit is permanently recorded and can be inspected at any time.

Key history commands:

| Command | Purpose |
|---------|---------|
| `git log` | Show commit history |
| `git log --oneline` | Compact one-line-per-commit view |
| `git log --graph` | Show branch/merge structure visually |
| `git log -n 5` | Show only the last 5 commits |
| `git log --stat` | Show which files changed in each commit |
| `git show <hash>` | Show the full details of a specific commit |
| `git diff <hash1> <hash2>` | Compare two commits |
| `git blame <file>` | Show who last modified each line of a file |

Commit hashes are 40-character hex strings, but you only need the first 7 characters to identify a commit uniquely. For example: `a1b2c3d`.

---

## Part 1: Navigating the Log

Use your `git-project` repository.

### Task A: Basic Log Formats

```bash
cd ~/git-project
git log
```

Notice each commit shows: hash, author, date, and message. Now try different formats:

```bash
git log --oneline
git log --oneline --graph
git log --stat
```

The `--stat` flag shows which files were added, modified, or deleted in each commit and how many lines changed.

### Task B: Filtering the Log

```bash
git log -3
git log --oneline -5
```

Limit output to the most recent N commits.

Search for commits by message content:

```bash
git log --grep="Add"
```

This shows only commits whose message contains "Add."

Search for commits that changed a specific file:

```bash
git log -- src/Main.java
git log --oneline -- src/Main.java
```

---

## Part 2: Inspecting Individual Commits

### Task C: Use `git show`

Pick a commit hash from your log and inspect it:

```bash
git log --oneline -5
git show <paste-a-hash-here>
```

`git show` displays the commit metadata AND the full diff of what changed. You can also use shorthand:

```bash
git show HEAD
```

`HEAD` always refers to the most recent commit on the current branch.

### Task D: Compare Commits with `git diff`

Compare your first commit with your latest:

```bash
git log --oneline
git diff <oldest-hash> <newest-hash>
```

This shows every change that happened between those two commits. Try also:

```bash
git diff HEAD~3 HEAD
```

`HEAD~3` means "3 commits before HEAD."

---

## Part 3: Using `git blame`

### Task E: Build a File with Multiple Commits

Create a file and modify it across several commits so `blame` has something interesting to show:

```bash
echo "Line 1: Created in first commit" > history.txt
git add history.txt
git commit -m "Create history.txt with line 1"

echo "Line 2: Added in second commit" >> history.txt
git add history.txt
git commit -m "Add line 2 to history.txt"

echo "Line 3: Added in third commit" >> history.txt
git add history.txt
git commit -m "Add line 3 to history.txt"
```

### Task F: Run `git blame`

```bash
git blame history.txt
```

Each line shows:
- The commit hash that last modified that line
- The author
- The date
- The line content

This is invaluable for understanding **who** changed **what** and **when**.

---

## Part 4: Pretty Formats

### Task G: Custom Log Formatting

Git supports custom log formats:

```bash
git log --pretty=format:"%h - %an, %ar : %s"
```

Format placeholders:
- `%h` — abbreviated hash
- `%an` — author name
- `%ar` — relative date ("2 hours ago")
- `%s` — subject (first line of message)
- `%ae` — author email

Try this decorated format to see branch labels:

```bash
git log --oneline --graph --decorate --all
```

This will become very useful once you start working with branches.

---

## Submission

Save a file named `Day_05_Output.md` in this folder containing the terminal output from each task.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Basic log formats demonstrated (`--oneline`, `--graph`, `--stat`) | 15 |
| Log filtered by count, message, and file | 15 |
| `git show` used on a specific commit and `HEAD` | 15 |
| `git diff` used to compare two commits | 15 |
| `history.txt` built across multiple commits | 10 |
| `git blame` output shown and understood | 15 |
| Custom log format used | 15 |
| **Total** | **100** |
