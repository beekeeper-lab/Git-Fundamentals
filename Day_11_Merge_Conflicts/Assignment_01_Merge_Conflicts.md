# Day 11 Assignment: Merge Conflicts

## Overview

- **Topic:** Understanding, Creating, and Resolving Merge Conflicts
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

A **merge conflict** happens when two branches modify the **same lines** of the **same file**. Git can automatically merge changes to different files or different parts of the same file, but when changes overlap, you need to decide which version to keep.

When a conflict occurs, Git marks the file with conflict markers:

```
<<<<<<< HEAD
This is the version on your current branch.
=======
This is the version from the branch being merged.
>>>>>>> feature-branch
```

- Everything between `<<<<<<< HEAD` and `=======` is YOUR current branch's version
- Everything between `=======` and `>>>>>>>` is the INCOMING branch's version
- You resolve the conflict by editing the file to keep what you want, removing the markers, then staging and committing

---

## Part 1: Create a Conflict

### Task A: Set Up a Fresh Repo

```bash
mkdir ~/conflict-practice
cd ~/conflict-practice
git init
echo "Line 1: Original content" > shared.txt
echo "Line 2: This line stays the same" >> shared.txt
echo "Line 3: Original ending" >> shared.txt
git add shared.txt
git commit -m "Initial version of shared.txt"
```

### Task B: Modify the File on Two Branches

Create a branch and change line 1:

```bash
git switch -c branch-a
sed -i 's/Line 1: Original content/Line 1: Changed by Branch A/' shared.txt
git add shared.txt
git commit -m "Branch A: modify line 1"
```

Go back to `main` and change the same line differently:

```bash
git switch main
sed -i 's/Line 1: Original content/Line 1: Changed by Main/' shared.txt
git add shared.txt
git commit -m "Main: modify line 1"
```

### Task C: Attempt the Merge

```bash
git merge branch-a
```

Git will report: **CONFLICT (content): Merge conflict in shared.txt**. The merge is paused — it needs your help.

---

## Part 2: Resolve the Conflict

### Task D: Inspect the Conflict

```bash
git status
cat shared.txt
```

`git status` shows `shared.txt` as "both modified." The file contents show the conflict markers. Read them carefully.

### Task E: Resolve the Conflict

Open `shared.txt` in your editor and resolve it. Remove the conflict markers and decide what the final version should be. For example, you might combine both changes:

```
Line 1: Changed by Main and Branch A
Line 2: This line stays the same
Line 3: Original ending
```

Or pick one side:

```
Line 1: Changed by Main
Line 2: This line stays the same
Line 3: Original ending
```

The key is: **remove all `<<<<<<<`, `=======`, and `>>>>>>>` lines** and leave the file in the correct final state.

### Task F: Complete the Merge

```bash
git add shared.txt
git commit -m "Merge branch-a: resolve conflict in shared.txt"
git log --oneline --graph --all
```

The merge commit records that both branches were combined and the conflict was resolved.

---

## Part 3: Multi-File Conflicts

### Task G: Create Conflicts in Multiple Files

```bash
git switch -c branch-b
echo "Branch B header" > header.txt
echo "Branch B content" > content.txt
git add header.txt content.txt
git commit -m "Branch B: add header and content"

git switch main
echo "Main header" > header.txt
echo "Main content" > content.txt
git add header.txt content.txt
git commit -m "Main: add header and content"
```

### Task H: Merge and Resolve Multiple Conflicts

```bash
git merge branch-b
git status
```

Both files have conflicts. Resolve each one:

```bash
cat header.txt
# Edit header.txt to resolve the conflict
cat content.txt
# Edit content.txt to resolve the conflict
```

After editing both files:

```bash
git add header.txt content.txt
git commit -m "Merge branch-b: resolve conflicts in header and content"
```

---

## Part 4: Aborting a Merge

### Task I: Start a Conflict and Abort

Sometimes you realize you're not ready to resolve a conflict. You can abort:

```bash
git switch -c branch-c
echo "Branch C version" > abort-test.txt
git add abort-test.txt
git commit -m "Branch C: add abort-test"

git switch main
echo "Main version" > abort-test.txt
git add abort-test.txt
git commit -m "Main: add abort-test"

git merge branch-c
git status
```

Instead of resolving, abort:

```bash
git merge --abort
git status
cat abort-test.txt
```

Everything is back to the way it was before the merge attempt. No harm done.

---

## Submission

Save a file named `Day_11_Output.md` in this folder containing the terminal output from each task.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Conflicting changes created on two branches | 15 |
| Conflict markers identified and explained | 15 |
| Single-file conflict resolved cleanly | 20 |
| Merge commit created after resolution | 10 |
| Multi-file conflict created and resolved | 20 |
| Merge aborted with `git merge --abort` | 10 |
| Branch graph shown after each merge | 10 |
| **Total** | **100** |
