# Module 13: Git Stash

## Introduction

> 🏷️ When You're Ready

> 🎯 **Teach:** How to save, list, restore, and manage stashed changes.
> **See:** Stashing in action across multiple scenarios, including the real-world branch-switching use case.
> **Feel:** Relieved that there's a clean way to pause work without making junk commits.

> 🎙️ You're halfway through building a feature and your boss messages you -- there's a bug in production that needs fixing now. You can't commit half-finished work, and you can't switch branches with a messy working directory. This is exactly what git stash is for.

> 🔄 **Where this fits:** Stashing is a workflow tool that complements branching. You've learned to create branches for parallel work -- stashing handles the in-between moments when you need to context-switch quickly without committing incomplete changes.

## Why Stash Exists

> 🎯 **Teach:** The purpose of stash -- saving work in progress to a temporary shelf for later retrieval.
> **See:** A command reference table showing all the key stash operations.
> **Feel:** Equipped with a mental model of stash as a bookmark for your in-progress work.

> 🎙️ Stash saves your work in progress to a temporary shelf, gives you a clean slate, and lets you come back to it later. Think of it like putting a bookmark in your work and setting it aside. Here are the key commands you'll be using today.

| Command | Purpose |
|---------|---------|
| `git stash push -m "message"` | Save uncommitted changes with a description |
| `git stash --include-untracked` | Also stash untracked (new) files |
| `git stash list` | Show all stashes |
| `git stash show` | Summary of what's in the top stash |
| `git stash show -p` | Full diff of the top stash |
| `git stash pop` | Apply most recent stash and remove it |
| `git stash apply` | Apply most recent stash but keep it |
| `git stash drop` | Delete the most recent stash |
| `git stash clear` | Delete ALL stashes |

Stashes are stored in a stack (LIFO -- last in, first out). The most recent stash is `stash@{0}`.

## Set Up

> 🎯 **Teach:** How to create a simple practice repo for stashing exercises.
> **See:** A fresh repo initialized with one committed file, ready for experimentation.
> **Feel:** Ready to start experimenting with stash in a clean environment.

> 🎙️ Let's create a fresh repo to practice in. We just need a single committed file to get started. Everything else we'll build as we go.

```bash
mkdir ~/stash-practice
cd ~/stash-practice
git init
echo "# Stash Practice" > README.md
git add README.md
git commit -m "Initial commit"
```

## Stash Uncommitted Work

> 🎯 **Teach:** How to stash both tracked and untracked changes using `--include-untracked`.
> **See:** A dirty working directory cleaned instantly by `git stash push`.
> **Feel:** Amazed at how quickly stash clears the slate while keeping your work safe.

> 🎙️ Now let's make some changes but not commit them. We'll create a new file and modify the readme. Then we'll stash everything away and watch the working directory go clean. The dash dash include-untracked flag is important -- without it, brand new files won't be stashed.

Start making changes but don't commit:

```bash
echo "Work in progress..." > wip.txt
echo "Modified readme" >> README.md
git status
```

You have an untracked file and a modified tracked file. Stash everything:

```bash
git stash push -m "WIP: working on new feature" --include-untracked
git status
```

The working directory is clean again. Your changes are safely saved.

> **Note:** `--include-untracked` (or `-u`) is needed to stash untracked files too. Without it, only tracked modified files are stashed.

## View the Stash

> 🎯 **Teach:** How to inspect stashed changes using `list`, `show`, and `show -p`.
> **See:** The stash list with your descriptive message, a change summary, and the full diff.
> **Feel:** Confident you can verify what's in a stash before restoring it.

> 🎙️ Your changes are stashed, but where did they go? The stash list shows all your saved stashes, show gives a summary, and show dash-p gives the full diff. Always check the stash before popping it -- make sure you're restoring what you think you're restoring.

```bash
git stash list
git stash show
git stash show -p
```

- `list` shows all stashes with their messages
- `show` shows a summary (files changed, insertions, deletions)
- `show -p` shows the full diff

> 💡 **Remember this one thing:** Always use `-m "message"` when stashing. Future you will thank present you when the stash list has descriptive names instead of cryptic default messages.

## Pop the Stash

> 🎯 **Teach:** How `git stash pop` restores changes and removes the stash from the list in one step.
> **See:** Changes restored to the working directory and the stash list becoming empty.
> **Feel:** The satisfying snap of getting your work back exactly as you left it.

> 🎙️ The most common way to get your work back is git stash pop. It applies the most recent stash and removes it from the list in one step. After popping, your working directory should look exactly like it did before you stashed.

```bash
git stash pop
git status
ls
```

Your changes are back. `pop` applies the stash AND removes it from the list:

```bash
git stash list
```

The list should be empty.

## Stash and Apply (Without Removing)

> 🎯 **Teach:** The difference between `pop` (apply + remove) and `apply` (apply + keep).
> **See:** `git stash apply` restoring changes while the stash remains in the list.
> **Feel:** Understanding when to use each -- apply for safety or multi-branch use, pop for normal flow.

> 🎙️ There's another way to restore a stash -- git stash apply. Unlike pop, apply keeps the stash in the list after restoring it. This is useful if you want to apply the same stash to multiple branches, or if you want a safety net in case something goes wrong.

```bash
git stash push -m "Same WIP again" --include-untracked
git stash apply
git status
git stash list
```

Unlike `pop`, `apply` keeps the stash in the list. This is useful if you want to apply the same stash to multiple branches.

Clean up the stash we no longer need:

```bash
git stash drop
git stash list
```

## Create Multiple Stashes

> 🎯 **Teach:** That stashes stack up with LIFO numbering -- the most recent is always `stash@{0}`.
> **See:** Three stashes created in sequence, each with a descriptive message and a numbered position.
> **Feel:** Comfortable managing multiple stashes without losing track of which is which.

> 🎙️ You can stack up multiple stashes, and each one gets a number. The most recent is always stash at zero. Let's create three stashes so you can see how the numbering works. Commit the current work first so we start clean.

Commit current work first, then create several stashes:

```bash
git add .
git commit -m "Add WIP files"

echo "Change set A" > changes-a.txt
git stash push -m "Feature A changes" --include-untracked

echo "Change set B" > changes-b.txt
git stash push -m "Feature B changes" --include-untracked

echo "Change set C" > changes-c.txt
git stash push -m "Feature C changes" --include-untracked
```

## Apply a Specific Stash

> 🎯 **Teach:** How to target a specific stash by its number using `stash@{n}` syntax.
> **See:** A middle stash applied by index, and `git stash clear` wiping the entire list.
> **Feel:** In control of the stash stack -- able to pick exactly what you need.

> 🎙️ When you have multiple stashes, you can apply any specific one by its number. The numbering starts at zero for the most recent. This is handy when you've shelved several things and need to pick one out of the middle of the stack.

```bash
git stash list
```

You should see three stashes numbered `stash@{0}` through `stash@{2}`. Apply a specific one:

```bash
git stash apply stash@{1}
ls
git status
```

This applies "Feature B changes" without removing it from the list.

Clear all stashes:

```bash
git checkout -- .
rm -f changes-b.txt
git stash clear
git stash list
```

All stashes are gone. Use `clear` with caution -- there's no undo.

## The Real-World Use Case

> 🎯 **Teach:** The stash-switch-fix-switch-pop pattern for handling interruptions mid-feature.
> **See:** Work in progress stashed, a branch switch to fix a bug, then a return to the feature branch.
> **Feel:** Prepared for the most common real-world stashing scenario you'll encounter on the job.

> 🎙️ This is the scenario that makes stashing indispensable. You're in the middle of a feature, you get pulled away to fix a bug, and you need to switch branches cleanly. Let's walk through it step by step -- stash, switch, fix, switch back, pop.

Start working on a new feature:

```bash
git switch -c feature-new
echo "Started a new feature" > new-feature.txt
echo "Additional modifications" >> README.md
git status
```

Suddenly you need to fix a bug on `main`. Stash your work and switch:

```bash
git stash push -m "Pausing feature-new work" --include-untracked
git switch main
```

## Fix the Bug on Main

> 🎯 **Teach:** How to make a clean fix on main while feature work is safely stashed.
> **See:** A bugfix committed on main with no trace of the stashed feature work.
> **Feel:** Focused -- stashing let you context-switch cleanly without mixing concerns.

> 🎙️ Now you're on main with a clean working directory. Fix the bug, commit it, and you're done. The whole time, your feature work is safely tucked away in the stash, waiting for you to come back.

```bash
echo "Bug fix applied" > bugfix.txt
git add bugfix.txt
git commit -m "Fix critical bug"
```

## Return and Restore

> 🎯 **Teach:** How to switch back to the feature branch and pop the stash to resume work.
> **See:** The feature branch restored to its exact pre-interruption state after `git stash pop`.
> **Feel:** Smooth and professional -- interruptions handled without any throwaway commits.

> 🎙️ Bug is fixed. Now switch back to your feature branch and pop the stash. Your work in progress is exactly where you left it. Commit and finish up. This stash-switch-fix-switch-pop pattern is the professional way to handle interruptions.

```bash
git switch feature-new
git stash pop
git status
ls
```

Your work in progress is exactly where you left it. Commit and finish:

```bash
git add .
git commit -m "Complete new feature"
git log --oneline --all --graph
```

> 💡 **Remember this one thing:** The stash-switch-fix-switch-pop pattern is the professional way to handle interruptions. Never make a throwaway "WIP" commit just to switch branches -- stash instead.

## Submission

> 🎯 **Teach:** How to document stashing exercises for submission.
> **See:** A checklist of required outputs covering all stash operations practiced.
> **Feel:** Accomplishment from adding a powerful workflow tool to your Git toolkit.

> 🎙️ Capture all your terminal output from today -- the basic stashing, the pop vs. apply comparison, the multiple stashes, and especially the real-world branch-switching scenario. That last one is the skill you'll use most often on the job.

Save a file named `Day_13_Output.md` containing the terminal output from each task.

| Criteria | Points |
|----------|--------|
| Changes stashed with a descriptive message | 10 |
| Stash inspected with `list`, `show`, and `show -p` | 15 |
| Stash restored with `pop` (removed from list) | 15 |
| Stash restored with `apply` (kept in list) | 10 |
| Multiple stashes created and specific one applied | 20 |
| Stash used to switch branches mid-work | 20 |
| Stash list cleaned up | 10 |
| **Total** | **100** |
