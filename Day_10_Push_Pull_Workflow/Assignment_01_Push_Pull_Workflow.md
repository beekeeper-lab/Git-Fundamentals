# Day 10 Assignment: Push, Pull, and Branch Workflow

## Overview

- **Topic:** Pushing Branches, Pull Requests, and the Feature Branch Workflow
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

In real-world projects, you rarely push directly to `main`. Instead, you:

1. Create a **feature branch**
2. Make commits on the branch
3. **Push** the branch to the remote
4. Open a **Pull Request (PR)** on GitHub
5. Get the PR reviewed and **merged**
6. **Delete** the branch and pull the updated `main`

This is called the **feature branch workflow**. Pull requests are a GitHub feature (not a Git feature) that let teams review code before it's merged.

---

## Part 1: Push a Feature Branch

### Task A: Create and Push a Feature Branch

```bash
cd ~/merge-practice
git switch -c feature-login
echo "<form>Username: <input></form>" > login.html
git add login.html
git commit -m "Add login page HTML"
```

Push the branch to GitHub:

```bash
git push -u origin feature-login
```

Go to your GitHub repository in a browser. You should see a banner saying "feature-login had recent pushes" with a button to create a pull request.

### Task B: Add More Commits to the Branch

```bash
echo "form { padding: 20px; }" > login.css
git add login.css
git commit -m "Add login page styles"
git push
```

The second `git push` doesn't need `-u` since the tracking is already set up.

---

## Part 2: Create a Pull Request on GitHub

### Task C: Open a Pull Request

1. Go to your repository on GitHub
2. Click **"Compare & pull request"** (or go to the Pull Requests tab → New Pull Request)
3. Set the base branch to `main` and the compare branch to `feature-login`
4. Write a title: `Add login page`
5. Write a description explaining what the PR adds
6. Click **Create pull request**

### Task D: Review the PR

On the PR page:
1. Click the **"Files changed"** tab to see the diff
2. Notice you can leave line-by-line comments
3. Go back to the **"Conversation"** tab

### Task E: Merge the PR on GitHub

1. Click **"Merge pull request"**
2. Click **"Confirm merge"**
3. Click **"Delete branch"** to clean up the remote branch

---

## Part 3: Sync Your Local Repository

### Task F: Update Your Local Main

```bash
git switch main
git pull
ls
```

`login.html` and `login.css` should now be on `main` locally.

### Task G: Delete the Local Feature Branch

```bash
git branch -d feature-login
git branch
```

The branch is safely deleted because its commits are now part of `main`.

### Task H: Prune Remote-Tracking Branches

The remote branch was deleted on GitHub, but your local Git still remembers it:

```bash
git branch -a
```

You'll see `remotes/origin/feature-login` still listed. Clean it up:

```bash
git fetch --prune
git branch -a
```

Now the stale remote-tracking branch is gone.

---

## Part 4: Full Cycle Practice

### Task I: Do the Complete Workflow Again

Practice the full cycle one more time, faster:

```bash
git switch -c feature-footer
echo "<footer>© 2025 My Site</footer>" > footer.html
git add footer.html
git commit -m "Add footer component"
git push -u origin feature-footer
```

Then on GitHub:
1. Create a pull request
2. Merge it
3. Delete the remote branch

Back in the terminal:

```bash
git switch main
git pull
git branch -d feature-footer
git fetch --prune
git log --oneline -5
```

---

## Submission

Save a file named `Day_10_Output.md` in this folder containing terminal output and screenshots of the GitHub PR process.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Feature branch created and pushed to remote | 15 |
| Additional commits pushed to the branch | 10 |
| Pull request created on GitHub | 15 |
| PR diff reviewed on Files Changed tab | 10 |
| PR merged on GitHub | 15 |
| Local main updated with `git pull` | 10 |
| Local and remote branches cleaned up | 10 |
| Full cycle repeated independently | 15 |
| **Total** | **100** |
