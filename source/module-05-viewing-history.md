# Module 5: Exploring Git History

## Introduction

> 🏷️ Useful Soon

> 🎯 **Teach:** How to navigate, filter, and inspect Git's commit history.
> **See:** Multiple log formats, commit comparison, and line-by-line blame output.
> **Feel:** Confident that you can always find what changed, when, and why.

> 🎙️ One of the most powerful things about Git is that nothing is lost. Every commit you've ever made is permanently recorded, and today you'll learn how to explore that history. You'll search through commits, compare versions, and even find out who wrote each line of a file and when. These are the tools that make version control truly useful.

![Git as a time machine](../images/module-05/time-machine-hero.png)

Every commit in Git is a snapshot with a unique hash, author, date, and message. The history commands let you slice through that record in different ways depending on what you need.

### Key Commands

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

> 🔄 **Where this fits:** You've been making commits for several days now. Today you learn to look back at everything you've built. These history tools become essential once your project grows beyond a handful of commits.

## Basic Log Formats

> 🎯 **Teach:** That `git log` has multiple output formats, each revealing different information about your history.
> **See:** The same commit history displayed in full, oneline, graph, and stat formats.
> **Feel:** Comfortable choosing the right log format for what you need to know.

> 🎙️ The git log command is your window into the past. By default it shows everything in full detail, but there are several flags that change how the output looks. Let's start by looking at the same history in three different formats so you can see what each one highlights.

![Log format comparison](../images/module-05/log-format-comparison.png)

Use your `git-project` repository.

```bash
cd ~/git-project
git log
```

Notice each commit shows: hash, author, date, and message. Now try different formats:

```bash
git log --oneline
```

The `--oneline` flag compresses each commit to a single line with an abbreviated hash and the message. This is great for getting a quick overview.

```bash
git log --oneline --graph
```

The `--graph` flag draws an ASCII art diagram of branch structure. You'll appreciate this more once you start working with branches.

```bash
git log --stat
```

The `--stat` flag shows which files were added, modified, or deleted in each commit and how many lines changed.

## Filtering by Count

> 🎯 **Teach:** How to limit log output to only the most recent commits using the `-n` flag.
> **See:** The same history trimmed to just the last 3 or 5 commits with `-3` and `--oneline -5`.
> **Feel:** Relief that you don't have to scroll through hundreds of commits to see recent work.

> 🎙️ When your project has hundreds of commits, you don't want to scroll through all of them. The dash-n flag lets you limit the output to just the most recent commits. This is one of the flags you'll use most often with git log.

Limit output to the most recent N commits:

```bash
git log -3
```

This shows only the last 3 commits. You can combine this with other flags:

```bash
git log --oneline -5
```

This gives you a compact view of the last 5 commits -- perfect for a quick check of recent work.

## Filtering by Message and File

> 🎯 **Teach:** How to search commit history by message content with `--grep` and by file path with `--`.
> **See:** Filtered log output showing only commits matching a keyword or touching a specific file.
> **Feel:** Empowered to track down any change in the history without manually scanning every commit.

> 🎙️ Sometimes you need to find a specific commit but you don't remember the hash. Git lets you search through commit messages with grep, or narrow the log to only commits that touched a particular file. Both of these are essential for tracking down when a change was made.

Search for commits by message content:

```bash
git log --grep="Add"
```

This shows only commits whose message contains "Add." The search is case-sensitive by default.

Search for commits that changed a specific file:

```bash
git log -- src/Main.java
git log --oneline -- src/Main.java
```

The `--` separator tells Git that what follows is a file path, not a branch name. This is important because branch names and file names can sometimes overlap.

## Inspecting a Specific Commit with git show

> 🎯 **Teach:** How to examine a single commit's full details -- metadata, message, and diff -- using `git show`.
> **See:** The complete diff output for a specific commit hash, showing exactly what changed.
> **Feel:** Confident that you can always drill into any commit to understand precisely what happened.

> 🎙️ Sometimes you need to look at one specific commit in detail -- what exactly changed, who did it, and what was the full diff. The git show command gives you all of that in one shot. Pick a commit hash from your log and let's take a closer look.

Pick a commit hash from your log and inspect it:

```bash
git log --oneline -5
git show <paste-a-hash-here>
```

`git show` displays the commit metadata AND the full diff of what changed. You can see exactly which lines were added, removed, or modified in that commit.

## Showing the Latest Commit with HEAD

> 🎯 **Teach:** That `HEAD` is a built-in reference that always points to the most recent commit on your current branch.
> **See:** `git show HEAD` displaying the latest commit without needing to look up a hash.
> **Feel:** That Git's shortcuts make everyday tasks faster and more convenient.

> 🎙️ You don't always need to look up a specific hash. Git has a built-in shorthand called HEAD that always points to the most recent commit on your current branch. It's one of the most commonly used references in Git.

```bash
git show HEAD
```

`HEAD` always refers to the most recent commit on the current branch. This is a quick way to review what you just committed without needing to copy a hash.

## Comparing Commits with git diff

> 🎯 **Teach:** How `git diff` compares any two points in your commit history to show what changed between them.
> **See:** A diff output between your oldest and newest commits, with `+` and `-` lines showing additions and removals.
> **Feel:** That you can always answer the question "what changed between these two points?"

> 🎙️ While git show looks at a single commit, git diff lets you compare any two points in your history. You give it two commit hashes, and it shows you every change that happened between them. This is incredibly useful when you're trying to understand how your code evolved over time.

Compare your first commit with your latest:

```bash
git log --oneline
git diff <oldest-hash> <newest-hash>
```

This shows every change that happened between those two commits. Lines prefixed with `+` were added, lines with `-` were removed.

## The HEAD~N Notation

> 🎯 **Teach:** How the tilde notation (`HEAD~N`) lets you reference commits relative to HEAD without looking up hashes.
> **See:** Commands using `HEAD~1`, `HEAD~2`, and `HEAD~3` to navigate history by relative position.
> **Feel:** That navigating Git history can be quick and intuitive with relative references.

> 🎙️ Looking up specific hashes can be tedious. Git provides a relative notation using the tilde character that lets you refer to commits relative to HEAD. HEAD tilde 1 means one commit before HEAD, HEAD tilde 3 means three commits back, and so on. This is often more convenient than copying hashes.

![HEAD tilde navigation](../images/module-05/head-tilde-navigation.png)

```bash
git diff HEAD~3 HEAD
```

`HEAD~3` means "3 commits before HEAD." You can use this notation anywhere Git expects a commit reference. Try a few variations:

```bash
git show HEAD~1
git diff HEAD~2 HEAD~1
```

> 💡 **Remember this one thing:** `git show` inspects a single commit. `git diff <A> <B>` compares any two commits. Between these two commands, you can always answer the question "what changed?"

## Building a File Across Multiple Commits

> 🎯 **Teach:** How to create a file with a multi-commit history so that tools like `git blame` have meaningful data to show.
> **See:** Three separate commits, each adding one line to the same file.
> **Feel:** That building up a file incrementally is natural in Git and creates a rich, traceable history.

> 🎙️ Git blame is one of those tools that sounds aggressive but is actually just informational. To see it in action, we need a file that was modified across several commits. Let's build one now -- we'll create a file and add a line in each of three separate commits.

Create a file and modify it across several commits so `blame` has something interesting to show:

```bash
echo "Line 1: Created in first commit" > history.txt
git add history.txt
git commit -m "Create history.txt with line 1"
```

```bash
echo "Line 2: Added in second commit" >> history.txt
git add history.txt
git commit -m "Add line 2 to history.txt"
```

```bash
echo "Line 3: Added in third commit" >> history.txt
git add history.txt
git commit -m "Add line 3 to history.txt"
```

Each commit adds one line to the file. Now each line has a different commit as its origin.

## Running git blame

> 🎯 **Teach:** How `git blame` annotates every line of a file with the commit, author, and date that last modified it.
> **See:** Blame output for `history.txt` showing three different commits responsible for three different lines.
> **Feel:** That you have a powerful forensic tool for understanding who changed what and when.

> 🎙️ Now that our file has lines from three different commits, git blame can show us exactly which commit is responsible for each line. It annotates every line with the commit hash, author, date, and the line content. On a team, this is invaluable for understanding who wrote what and when.

![Git blame as detective work](../images/module-05/git-blame-detective.png)

```bash
git blame history.txt
```

Each line shows:
- The commit hash that last modified that line
- The author
- The date
- The line content

This is invaluable for understanding **who** changed **what** and **when**.

## Custom Log Formatting

> 🎯 **Teach:** How to define custom log output using `--pretty=format` with placeholder codes like `%h`, `%an`, and `%s`.
> **See:** A personalized log format string that displays hash, author, date, and message in your chosen layout.
> **Feel:** That Git is highly customizable and you can tailor its output to your workflow.

> 🎙️ Git's log is surprisingly customizable. You can define exactly what information appears and how it's formatted using the pretty flag with format placeholders. This is useful for generating changelogs, piping output to other tools, or just making the log easier to scan.

Git supports custom log formats:

```bash
git log --pretty=format:"%h - %an, %ar : %s"
```

Format placeholders:
- `%h` -- abbreviated hash
- `%an` -- author name
- `%ar` -- relative date ("2 hours ago")
- `%s` -- subject (first line of message)
- `%ae` -- author email

Try experimenting with your own format strings to see what works best for you.

## Decorated Graph View

> 🎯 **Teach:** That the decorated graph view is the most informative way to visualize your entire repository at a glance.
> **See:** `git log --oneline --graph --decorate --all` showing branch labels, HEAD position, and commit relationships.
> **Feel:** Motivated to make this command a daily habit or shell alias.

> 🎙️ The decorated graph view is probably the single most informative way to look at your repository. It combines the compact oneline format with the branch graph, and adds labels showing where each branch pointer and HEAD are. Consider making this an alias -- you'll use it constantly.

Try this decorated format to see branch labels:

```bash
git log --oneline --graph --decorate --all
```

This will become very useful once you start working with branches. It shows where each branch pointer is, where HEAD is, and the full graph of how commits relate to each other.

> 💡 **Remember this one thing:** `git log --oneline --graph --decorate --all` is the single most informative view of your repository. Consider making it a shell alias -- you'll use it constantly.

## Submission

> 🎯 **Teach:** What complete, well-organized output looks like for grading, and how each rubric item maps to a task.
> **See:** A rubric table with point values for each section of today's exercises.
> **Feel:** Clear about what's expected and confident you can earn full marks by following the steps.

> 🎙️ Time to capture your work. Save all the terminal output from today's exercises into a single markdown file. Make sure each section is represented so the rubric items are clearly covered.

Save a file named `Day_05_Output.md` containing the terminal output from each task.

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
