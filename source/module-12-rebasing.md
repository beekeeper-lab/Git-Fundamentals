# Module 12: Rebasing

## Introduction

> 🏷️ When You're Ready

> 🎯 **Teach:** What rebasing does, how it differs from merging, and when to use each.
> **See:** Side-by-side comparisons of merge vs. rebase, conflict resolution during rebase, and the resulting history graphs.
> **Feel:** Comfortable choosing between merge and rebase, and confident about the golden rule of rebasing.

> 🎙️ Yesterday you learned how to resolve merge conflicts. Today you'll learn a different way to integrate changes -- rebasing. Where merging preserves the full branching history, rebasing replays your commits on top of another branch, creating a clean, linear timeline. Both are valid tools, and knowing when to use each one is a key professional skill.

> 🔄 **Where this fits:** You've been merging branches since Day 7. Rebasing gives you a second integration strategy. Many teams use rebase to keep feature branches up to date and merge for the final integration into main.

## Merge vs. Rebase

> 🎯 **Teach:** The fundamental difference between merge (preserves history) and rebase (linearizes history).
> **See:** ASCII diagrams showing the same integration done both ways, with different resulting graphs.
> **Feel:** Clear mental models for both approaches -- no confusion about which does what.

> 🎙️ Before we touch the keyboard, let's understand what makes rebase different from merge. Both integrate changes from one branch into another, but they do it in fundamentally different ways. Merge preserves history as it happened; rebase rewrites history to be linear.

**Merge** preserves the full branching history:

```
main:    A --- B --- E --- M
                  \       /
feature:           C --- D
```

**Rebase** replays your commits on top of main, creating a straight line:

```
Before:  main:    A --- B --- E
                           \
         feature:           C --- D

After:   main:    A --- B --- E
                               \
         feature:               C' --- D'
```

The commits `C'` and `D'` have different hashes than `C` and `D` because they now have different parent commits. The **content** is the same, but the **history** is rewritten.

## The Golden Rule of Rebasing

> 🎯 **Teach:** The one rule you must never break: never rebase commits that have been pushed to a shared remote.
> **See:** A clear statement of the rule and an explanation of why violating it causes problems.
> **Feel:** A healthy respect for the rule -- not fear, but understanding of why it exists.

> 🎙️ This is the most important rule in all of rebasing, and you need to internalize it before we go any further. Never rebase commits that have been pushed to a shared remote. If other people have those commits, rewriting them causes real problems. Rebase is for local cleanup only.

> **Never rebase commits that have been pushed to a shared remote.** Rebasing rewrites history, which causes problems for anyone else who has those commits.

Rebase is safe for local branches that haven't been pushed yet, or for personal branches that only you use.

## Set Up Diverging Branches

> 🎯 **Teach:** How to create a repo where main and a feature branch have diverged from a common ancestor.
> **See:** A feature branch with two commits and main with one new commit, creating a fork in history.
> **Feel:** Ready to see rebase in action on a concrete example.

> 🎙️ Let's start with the simplest case. We'll create a repo, make a feature branch with some commits, and then add a commit to main so the two branches diverge. This sets the stage for a rebase.

```bash
mkdir ~/rebase-practice
cd ~/rebase-practice
git init

echo "Version 1" > app.txt
git add app.txt
git commit -m "Initial commit"

echo "Version 2" >> app.txt
git add app.txt
git commit -m "Update to version 2"
```

Create a feature branch and add commits:

```bash
git switch -c feature-x
echo "Feature X - part 1" > feature-x.txt
git add feature-x.txt
git commit -m "Feature X: part 1"

echo "Feature X - part 2" >> feature-x.txt
git add feature-x.txt
git commit -m "Feature X: part 2"
```

Go back to `main` and add a commit to create divergence:

```bash
git switch main
echo "Version 3 - hotfix" >> app.txt
git add app.txt
git commit -m "Hotfix: update to version 3"
```

## View the Divergence

> 🎯 **Teach:** How to visualize diverging branches using the log graph before rebasing.
> **See:** A `git log --graph` showing main and feature-x splitting from a common ancestor.
> **Feel:** A clear picture of the forked history that rebase will straighten out.

> 🎙️ Before we rebase, let's look at the graph. You should see main and feature-x splitting from a common ancestor and heading in different directions. This is the forked history that rebase will straighten out.

```bash
git log --oneline --graph --all
```

You should see `main` and `feature-x` diverging from a common ancestor.

## Rebase the Feature Branch

> 🎯 **Teach:** How `git rebase main` replays feature commits on top of the latest main commit.
> **See:** The rebase command running, and the resulting linear graph with no fork.
> **Feel:** Impressed by how cleanly rebase straightens out the history.

> 🎙️ Now for the main event. When you run git rebase main from the feature branch, Git takes your feature commits, temporarily sets them aside, moves the branch pointer to the tip of main, and replays your commits one by one on top. Watch the graph change from forked to perfectly linear.

```bash
git switch feature-x
git rebase main
git log --oneline --graph --all
```

After the rebase:
- The feature branch commits are now **on top of** main's latest commit
- The history is a straight line
- No merge commit was created

## Fast-Forward Merge After Rebase

> 🎯 **Teach:** Why a rebase followed by merge results in a clean fast-forward with no merge commit.
> **See:** `git merge feature-x` producing a fast-forward and a perfectly linear log.
> **Feel:** Appreciation for the cleanest possible integration strategy.

> 🎙️ Since feature-x is now directly ahead of main with no divergence, merging is a simple fast-forward. Git just moves the main pointer up to match feature-x. No merge commit needed. This is the cleanest possible integration.

```bash
git switch main
git merge feature-x
git log --oneline --graph --all
```

The result is a perfectly linear history.

```bash
git branch -d feature-x
```

> 💡 **Remember this one thing:** The rebase-then-merge workflow gives you the cleanest possible history -- rebase your feature branch onto main, then fast-forward merge. No merge commits, no forks in the graph.

## Create a Rebase Conflict

> 🎯 **Teach:** That rebase can encounter conflicts just like merge when the same lines are changed.
> **See:** Two branches modifying the same file, setting up a conflict during rebase.
> **Feel:** Prepared -- rebase conflicts are resolved the same way as merge conflicts, with a slight twist.

> 🎙️ Just like merging, rebasing can run into conflicts when both branches changed the same lines. The difference is how you resolve them -- instead of resolving once in a merge commit, you resolve during the rebase process itself. Let's create that situation.

```bash
git switch -c feature-y
echo "Feature Y changes this line" > conflict-file.txt
git add conflict-file.txt
git commit -m "Feature Y: add conflict-file"

git switch main
echo "Main changes this line" > conflict-file.txt
git add conflict-file.txt
git commit -m "Main: add conflict-file"
```

## Resolve During Rebase

> 🎯 **Teach:** The rebase conflict workflow: resolve the file, `git add`, then `git rebase --continue`.
> **See:** A conflict pausing the rebase, manual resolution, and `--continue` finishing the job.
> **Feel:** Confident that rebase conflicts are just as manageable as merge conflicts.

> 🎙️ When you rebase and Git hits a conflict, it pauses and lets you fix things -- just like a merge conflict. The difference is that after resolving, you run git rebase dash dash continue instead of git commit. Git then keeps replaying the remaining commits.

```bash
git switch feature-y
git rebase main
```

Git will pause with a conflict. Inspect it:

```bash
git status
cat conflict-file.txt
```

Edit `conflict-file.txt` to resolve the conflict -- remove the markers, choose the content you want. Then continue the rebase:

```bash
git add conflict-file.txt
git rebase --continue
```

### Verify the Result

```bash
git log --oneline --graph --all
```

The rebase completed with a clean, linear history.

## Abort a Rebase

> 🎯 **Teach:** How `git rebase --abort` safely cancels a rebase and restores the original state.
> **See:** A conflict triggered during rebase, then cleanly aborted with no changes lost.
> **Feel:** Safe knowing there's always an escape hatch during rebase.

> 🎙️ Just like you can abort a merge, you can abort a rebase that's gone sideways. If you're in the middle of resolving conflicts and decide you'd rather not continue, git rebase dash dash abort takes you right back to where you started. Nothing is lost.

```bash
git switch -c feature-z
echo "Z content" > z-file.txt
git add z-file.txt
git commit -m "Feature Z: add z-file"

git switch main
echo "Main Z content" > z-file.txt
git add z-file.txt
git commit -m "Main: add z-file"

git switch feature-z
git rebase main
```

Instead of resolving, abort:

```bash
git rebase --abort
git status
git log --oneline --graph --all
```

The branch is back to its pre-rebase state. Nothing was lost.

> 💡 **Remember this one thing:** `git rebase --abort` is your escape hatch. If a rebase gets complicated, abort and rethink your approach.

## Set Up Side-by-Side Comparison

> 🎯 **Teach:** How to create identical scenarios for comparing merge and rebase approaches.
> **See:** Two demo branches prepared from the same starting point for a fair comparison.
> **Feel:** Curious to see the same integration done two different ways.

> 🎙️ Now let's see the two approaches side by side so you can really feel the difference. We'll create two identical scenarios and integrate one with merge, the other with rebase. Compare the graphs at the end -- that's the tradeoff you're choosing between.

```bash
git switch main
```

We'll create two demo branches from the same starting point and integrate them differently.

## The Merge Approach

> 🎯 **Teach:** How a standard merge creates a merge commit and preserves the branching history.
> **See:** A feature branch merged into main with a visible merge commit in the graph.
> **Feel:** Understanding that merge commits are a record of integration, not clutter.

> 🎙️ First, the merge approach. We'll create a branch, add a commit, let main advance, and then merge. Notice the merge commit that appears in the graph -- it records that two lines of development were combined.

```bash
git switch -c demo-merge
echo "Merge demo" > merge-demo.txt
git add merge-demo.txt
git commit -m "Demo merge commit"

git switch main
echo "Main progress" >> app.txt
git add app.txt
git commit -m "Main: more progress"

# Merge approach
git merge demo-merge
git log --oneline --graph -6
```

Note the merge commit in the graph.

## The Rebase Approach

> 🎯 **Teach:** How rebase-then-merge produces a linear history with no merge commit.
> **See:** The same scenario integrated via rebase, resulting in a straight-line graph.
> **Feel:** Able to make an informed choice between merge and rebase for any situation.

> 🎙️ Now the same scenario, but with rebase. Create a branch, add a commit, let main advance, then rebase and fast-forward merge. Compare this graph to the merge one -- no merge commit, just a straight line. That's the tradeoff: merge preserves history as it happened, rebase rewrites it to be clean.

```bash
git switch -c demo-rebase
echo "Rebase demo" > rebase-demo.txt
git add rebase-demo.txt
git commit -m "Demo rebase commit"

git switch main
echo "Even more progress" >> app.txt
git add app.txt
git commit -m "Main: even more progress"

git switch demo-rebase
git rebase main
git switch main
git merge demo-rebase
git log --oneline --graph -8
```

Compare the two sections of the graph -- the rebased one has no merge commit, just a straight line.

> 💡 **Remember this one thing:** **Merge** preserves history as it happened (with forks and merge commits). **Rebase** rewrites history to be linear. Use rebase for local cleanup, merge for shared integration.

## Submission

> 🎯 **Teach:** How to document rebase exercises and comparisons for submission.
> **See:** A checklist of required outputs including graphs at each step and the side-by-side comparison.
> **Feel:** Accomplishment from mastering a second integration strategy.

> 🎙️ Save all your terminal output from today's exercises. Make sure you captured the graph at each step -- the divergence, the rebase result, the conflict resolution, the abort, and especially the side-by-side merge vs. rebase comparison.

Save a file named `Day_12_Output.md` containing the terminal output from each task.

| Criteria | Points |
|----------|--------|
| Diverging branches created for rebase | 10 |
| Basic rebase completed (linear history shown) | 20 |
| Fast-forward merge after rebase | 10 |
| Rebase conflict resolved with `--continue` | 20 |
| Rebase aborted with `--abort` | 10 |
| Merge vs. rebase compared side by side | 20 |
| Graph output shown at each step | 10 |
| **Total** | **100** |
