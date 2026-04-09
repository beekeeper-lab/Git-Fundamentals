# Day 7 Assignment: Merging Branches

## Overview

- **Topic:** Fast-Forward Merges and Three-Way Merges
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

When you're done working on a branch, you **merge** it back into another branch (usually `main`). Git has two types of merges:

### Fast-Forward Merge

If `main` hasn't changed since the branch was created, Git just moves the `main` pointer forward:

```
Before:  main: A --- B
               feature: A --- B --- C --- D

After:   main: A --- B --- C --- D  (main moved to D)
```

No merge commit is created — the history is linear.

### Three-Way Merge

If both branches have new commits, Git creates a **merge commit** that combines both:

```
Before:  main:    A --- B --- E
                           \
         feature:           C --- D

After:   main:    A --- B --- E --- M  (M is the merge commit)
                           \       /
         feature:           C --- D
```

---

## Part 1: Fast-Forward Merge

Start with a clean repository so the examples are clear.

### Task A: Set Up a Fresh Repo

```bash
mkdir ~/merge-practice
cd ~/merge-practice
git init
echo "# Merge Practice" > README.md
git add README.md
git commit -m "Initial commit"
```

### Task B: Create a Feature Branch and Add Commits

```bash
git switch -c add-homepage
echo "<h1>Welcome</h1>" > index.html
git add index.html
git commit -m "Add homepage HTML"

echo "body { font-family: sans-serif; }" > style.css
git add style.css
git commit -m "Add stylesheet"
```

### Task C: Merge with Fast-Forward

```bash
git switch main
git log --oneline --all --graph
git merge add-homepage
git log --oneline --all --graph
```

Notice:
- Git says "Fast-forward" — no merge commit was created
- `main` now points to the same commit as `add-homepage`
- The history is a straight line

### Task D: Clean Up the Branch

```bash
git branch -d add-homepage
git branch
```

The branch is safely deleted because all its commits are now part of `main`.

---

## Part 2: Three-Way Merge

### Task E: Create Diverging Branches

```bash
git switch -c add-about
echo "<h1>About Us</h1>" > about.html
git add about.html
git commit -m "Add about page"
```

Now go back to `main` and make a different change:

```bash
git switch main
echo "<footer>Copyright 2025</footer>" >> index.html
git add index.html
git commit -m "Add footer to homepage"
```

### Task F: Visualize the Divergence

```bash
git log --oneline --all --graph
```

You should see two branches diverging — `main` and `add-about` each have commits the other doesn't.

### Task G: Perform the Three-Way Merge

```bash
git merge add-about
```

Git will open your editor for a merge commit message. Accept the default message or write your own, then save and close.

```bash
git log --oneline --all --graph
```

You should see the merge commit where the branches come back together.

### Task H: Verify the Result

```bash
ls
cat index.html
```

Both the footer (from `main`) and `about.html` (from the branch) are present. The merge combined both lines of work.

```bash
git branch -d add-about
```

---

## Part 3: Multiple Merges

### Task I: Merge Two Feature Branches Sequentially

Create two feature branches from `main`:

```bash
git switch -c feature-nav
echo "<nav>Home | About | Contact</nav>" > nav.html
git add nav.html
git commit -m "Add navigation bar"

git switch main
git switch -c feature-contact
echo "<h1>Contact Us</h1>" > contact.html
git add contact.html
git commit -m "Add contact page"
```

Merge both into `main`:

```bash
git switch main
git merge feature-nav
git merge feature-contact
git log --oneline --graph --all
```

### Task J: Clean Up

```bash
git branch -d feature-nav
git branch -d feature-contact
git branch
ls
```

All feature branch work is now in `main`, and the branches are cleaned up.

---

## Submission

Save a file named `Day_07_Output.md` in this folder containing the terminal output from each task.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Fast-forward merge completed and identified as fast-forward | 20 |
| Branch deleted after fast-forward merge | 5 |
| Diverging branches created for three-way merge | 15 |
| Three-way merge completed with merge commit | 20 |
| Merge result verified (both changes present) | 10 |
| Two feature branches merged sequentially | 20 |
| Branch graph shown at each stage | 10 |
| **Total** | **100** |
