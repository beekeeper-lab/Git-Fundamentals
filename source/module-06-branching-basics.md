# Module 6: Branching Basics

## Introduction

> 🏷️ Useful Soon

> 🎯 **Teach:** How to create, switch, and manage Git branches.
> **See:** Files appearing and disappearing as you switch branches, and a graph showing parallel lines of development.
> **Feel:** That branches are lightweight, fast, and safe to experiment with.

> 🎙️ Branches are where Git goes from useful to powerful. A branch lets you work on something new without affecting the stable version of your code. You can have multiple branches going at once, switch between them instantly, and your files literally change on disk when you do. Today you'll create branches, switch between them, and see this magic in action.

A branch is simply a movable pointer to a commit. When you create a branch, Git creates a new pointer -- it doesn't copy any files.

```
main:       A --- B --- C
                         \
feature:                  D --- E
```

In this diagram, `feature` branched off from `main` at commit C, then added commits D and E independently.

### Key Commands

| Command | Purpose |
|---------|---------|
| `git branch` | List all local branches |
| `git branch <name>` | Create a new branch |
| `git switch <name>` | Switch to a branch |
| `git switch -c <name>` | Create and switch in one step |
| `git branch -d <name>` | Delete a branch (safe -- won't delete unmerged work) |
| `git branch -D <name>` | Force delete a branch (even if unmerged) |
| `git branch -m <old> <new>` | Rename a branch |
| `git branch -v` | List branches with latest commit info |

> **Note:** `git switch` is the modern replacement for `git checkout` when switching branches. You may see `checkout` in older tutorials.

## See Your Current Branch

> 🎯 **Teach:** How to check which branch you're currently on using `git branch`.
> **See:** The branch listing with an asterisk marking the active branch.
> **Feel:** Oriented -- always knowing where you are before making changes.

> 🎙️ Before creating any new branches, let's see where you are right now. The git branch command with no arguments lists all your local branches. The one with the asterisk next to it is the branch you're currently on.

Use your `git-project` repository.

```bash
cd ~/git-project
git branch
```

The branch with the `*` next to it is your current branch (should be `main`).

## Create a New Branch

> 🎯 **Teach:** That creating a branch is instant and does NOT automatically switch you to it.
> **See:** `git branch feature-greeting` creating a new branch while the asterisk stays on `main`.
> **Feel:** That branches are so lightweight there's no reason not to use them.

> 🎙️ Creating a branch in Git is nearly instant -- it's just writing a 40-character hash to a file. The important thing to notice is that creating a branch does NOT switch you to it. You'll still be on main after this command runs.

```bash
git branch feature-greeting
git branch
```

You now have two branches, but you're still on `main`. The new branch points to the same commit as `main`.

## Switch to the Branch

> 🎯 **Teach:** How `git switch` moves you to a different branch and updates your working directory.
> **See:** The asterisk moving from `main` to `feature-greeting` after running `git switch`.
> **Feel:** That switching branches is fast, safe, and reversible.

> 🎙️ Now let's actually move to the new branch. When you switch branches, Git updates your working directory to match that branch's state. Right now both branches point to the same commit so nothing will change on disk, but that's about to change once you start making commits.

```bash
git switch feature-greeting
git branch
```

The `*` should now be next to `feature-greeting`. You're on the new branch.

## Make Commits on the Branch

> 🎯 **Teach:** That commits made on a branch only exist on that branch -- they don't affect `main`.
> **See:** Two new files committed on `feature-greeting` while `main` remains unchanged.
> **Feel:** Free to experiment on a branch without any risk to the stable codebase.

> 🎙️ Here's where it gets interesting. Any commits you make now will only exist on feature-greeting. Main won't know about them at all. Let's create a couple of files and commit them so the two branches diverge.

```bash
echo "Hello from the feature branch!" > greeting.txt
git add greeting.txt
git commit -m "Add greeting.txt on feature branch"
```

```bash
echo "Another feature file." > feature-notes.txt
git add feature-notes.txt
git commit -m "Add feature-notes.txt on feature branch"
```

These commits are now part of `feature-greeting` but not `main`.

## Switch Back to Main

> 🎯 **Teach:** That switching branches physically changes the files in your working directory to match that branch's state.
> **See:** Files disappearing when you switch to `main` and reappearing when you switch back to `feature-greeting`.
> **Feel:** The "aha moment" that branches are real, isolated workspaces -- not just labels.

> 🎙️ This is the moment that makes branches click for most people. When you switch back to main, those files you just created are going to disappear from your working directory. They aren't deleted -- they're safely stored in the feature-greeting branch. Git is just showing you what main looks like.

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

> 💡 **Remember this one thing:** Branches are cheap and instant. Switching branches changes the files on disk to match that branch's history. This is not copying files -- Git is rewiring what your working directory points to.

## Create a Second Branch from Main

> 🎯 **Teach:** How to create and switch to a new branch in one step with `git switch -c`, and that branches are independent of each other.
> **See:** A second feature branch created from `main` that has none of the first branch's files.
> **Feel:** That managing multiple parallel workstreams is natural and organized in Git.

> 🎙️ In real projects, you'll often have several branches going at once -- maybe one for a new feature, one for a bug fix, and main as the stable base. Let's create a second branch so you can see how Git keeps multiple lines of work organized independently.

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

## Visualize the Branches

> 🎯 **Teach:** How the `--graph --all` flags on `git log` show the structure of all branches visually.
> **See:** An ASCII graph with three branches diverging from a common commit.
> **Feel:** That you can always see the big picture of your repository's branching structure.

> 🎙️ Now you have three branches -- main, feature-greeting, and feature-about -- each with different content. The graph view of git log shows you how they all relate. You should see lines diverging from a common point, which is exactly how parallel development works.

```bash
git log --oneline --graph --all
```

You should see three branches diverging from a common point. This is how parallel development works -- each branch is independent.

## List Branches with Details

> 🎯 **Teach:** How `git branch -v` shows each branch's latest commit hash and message at a glance.
> **See:** A branch listing with abbreviated hashes and commit messages next to each branch name.
> **Feel:** Informed about what's happening across all branches without needing to switch to each one.

> 🎙️ The dash-v flag on git branch adds useful context to the branch listing -- it shows the latest commit hash and message for each branch. This is a quick way to see what's happening on each branch without switching to it.

```bash
git branch -v
```

This shows each branch with its latest commit hash and message. You can see at a glance what the latest work on each branch was.

## Rename a Branch

> 🎯 **Teach:** How to rename a branch with `git branch -m` without affecting its commits or history.
> **See:** A branch renamed from `feature-about` to `feature-about-page` with history intact.
> **Feel:** That Git gives you flexibility to fix naming mistakes easily.

> 🎙️ Branches are meant to be temporary, and sometimes you realize the name you picked isn't quite right. The dash-m flag lets you rename a branch without affecting any of its history or commits.

```bash
git switch main
git branch -m feature-about feature-about-page
git branch -v
```

The branch is renamed. History is unchanged.

## Delete a Branch

> 🎯 **Teach:** The difference between safe delete (`-d`) and force delete (`-D`), and when to use each.
> **See:** A safe delete being refused for an unmerged branch, then a force delete removing it.
> **Feel:** That Git's safety checks protect you from accidental data loss.

> 🎙️ When you're done with a branch, you clean it up by deleting it. Git has two levels of deletion: the safe version with lowercase d refuses to delete a branch that has unmerged work, and the force version with uppercase D deletes it regardless. Let's see both.

### Safe Delete

```bash
git branch -d feature-about-page
```

Git will warn you that the branch has changes not yet merged into `main`. This is a safety feature.

### Force Delete

Try force-deleting it (since this is practice):

```bash
git branch -D feature-about-page
git branch -v
```

> **Important:** `-d` is safe (refuses to delete unmerged branches). `-D` is forced deletion -- use with caution.

> 💡 **Remember this one thing:** Use `-d` to delete branches safely after merging. Only use `-D` when you're sure you want to discard unmerged work. In professional workflows, you'll almost always use `-d`.

## Submission

> 🎯 **Teach:** What complete, well-organized output looks like for grading, and how each rubric item maps to a task.
> **See:** A rubric table with point values for each branching exercise.
> **Feel:** Clear about what's expected and confident you can earn full marks by demonstrating each skill.

> 🎙️ Time to capture your work. Save all the terminal output from today's exercises into a single markdown file. Make sure each section is represented so the rubric items are clearly covered.

Save a file named `Day_06_Output.md` containing the terminal output from each task.

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
