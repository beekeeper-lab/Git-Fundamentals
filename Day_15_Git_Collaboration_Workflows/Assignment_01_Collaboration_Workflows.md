# Day 15 Assignment: Git Collaboration Workflows

## Overview

- **Topic:** Feature Branch Workflow, Forking Workflow, and Best Practices
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

Teams use different Git workflows depending on their size and needs. The three most common are:

### 1. Feature Branch Workflow (Most Common)

Everyone works on `main`. For each new feature or bugfix, create a short-lived branch:

```
main:      A --- B --- M1 --- M2 --- M3
                  \   /       /
feature-1:         C-D       /
                    \       /
feature-2:           E --- F
```

Rules:
- `main` is always deployable
- All work happens on feature branches
- Code gets to `main` via pull requests
- Branches are deleted after merging

### 2. Gitflow Workflow

Uses dedicated branches for releases, hotfixes, and development:

```
main:      v1.0 ──────────────── v1.1 ──── v2.0
              \                  /    \    /
hotfix:        \           fix─┘      \  /
                \                      \/
develop:    ─────D1──D2──D3────────D4──D5
                  \      /
feature:           F1──F2
```

Branches:
- `main` — Production releases only
- `develop` — Integration branch for features
- `feature/*` — Individual features
- `release/*` — Release preparation
- `hotfix/*` — Emergency production fixes

### 3. Forking Workflow (Open Source)

Each contributor forks the repository, works in their fork, and submits pull requests to the original:

```
Original repo (upstream) ← PR ← Your fork (origin)
```

---

## Part 1: Feature Branch Workflow Practice

### Task A: Set Up a Team Project

```bash
mkdir ~/workflow-practice
cd ~/workflow-practice
git init

echo "# Team Project" > README.md
echo "app.js" > app.js
git add .
git commit -m "Initial project setup"
```

### Task B: Simulate Two Features in Parallel

Create two feature branches:

```bash
git switch -c feature/user-auth
echo "function login() { }" > auth.js
git add auth.js
git commit -m "Add login function"

echo "function logout() { }" >> auth.js
git add auth.js
git commit -m "Add logout function"
```

```bash
git switch main
git switch -c feature/dashboard
echo "function renderDashboard() { }" > dashboard.js
git add dashboard.js
git commit -m "Add dashboard renderer"
```

### Task C: Merge Features Sequentially

```bash
git switch main
git merge feature/user-auth
git merge feature/dashboard

git log --oneline --graph --all

git branch -d feature/user-auth
git branch -d feature/dashboard
```

Both features are now in `main` with a clear history.

---

## Part 2: Working with Naming Conventions

### Task D: Branch Naming Patterns

Create branches using common naming conventions:

```bash
git switch -c feature/add-search-bar
echo "search functionality" > search.js
git add search.js
git commit -m "Add search bar component"
git switch main

git switch -c bugfix/fix-login-redirect
echo "redirect fix" > fix.js
git add fix.js
git commit -m "Fix login redirect bug"
git switch main

git switch -c hotfix/security-patch
echo "security update" > security.js
git add security.js
git commit -m "Apply security patch"
git switch main
```

List all branches:

```bash
git branch
```

Common prefixes:
- `feature/` — New functionality
- `bugfix/` — Bug repairs
- `hotfix/` — Urgent production fixes
- `release/` — Release preparation
- `chore/` — Maintenance tasks

Merge them all and clean up:

```bash
git merge feature/add-search-bar
git merge bugfix/fix-login-redirect
git merge hotfix/security-patch
git branch -d feature/add-search-bar bugfix/fix-login-redirect hotfix/security-patch
```

---

## Part 3: Forking Workflow

### Task E: Fork a Repository

1. Go to a public repository on GitHub (e.g., https://github.com/octocat/Spoon-Knife)
2. Click the **"Fork"** button in the top right
3. This creates a copy under your GitHub account

### Task F: Clone Your Fork

```bash
cd ~
git clone https://github.com/YOUR-USERNAME/Spoon-Knife.git
cd Spoon-Knife
```

### Task G: Add the Upstream Remote

```bash
git remote add upstream https://github.com/octocat/Spoon-Knife.git
git remote -v
```

You now have two remotes:
- `origin` — Your fork
- `upstream` — The original repository

### Task H: Keep Your Fork in Sync

```bash
git fetch upstream
git merge upstream/main
```

This pulls the latest changes from the original project into your local copy. Push to keep your fork updated:

```bash
git push origin main
```

---

## Part 4: Best Practices Checklist

### Task I: Practice the Complete Workflow

Do the full feature branch workflow one more time with proper practices:

```bash
cd ~/workflow-practice

# 1. Start from an updated main
git switch main

# 2. Create a descriptive branch name
git switch -c feature/add-contact-form

# 3. Make small, focused commits
echo "<form id='contact'>" > contact.html
git add contact.html
git commit -m "Add contact form HTML structure"

echo ".contact-form { margin: 20px; }" > contact.css
git add contact.css
git commit -m "Add contact form styles"

# 4. Review your changes before merging
git log --oneline main..HEAD
git diff main...HEAD --stat

# 5. Merge into main
git switch main
git merge feature/add-contact-form

# 6. Clean up
git branch -d feature/add-contact-form

# 7. Verify
git log --oneline -5
```

Key takeaways:
- `git log main..HEAD` shows commits on your branch that aren't on main
- `git diff main...HEAD --stat` shows a summary of all changes vs. main
- Small, focused commits are easier to review and revert

---

## Submission

Save a file named `Day_15_Output.md` in this folder containing the terminal output from each task.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Two parallel feature branches created and merged | 15 |
| Branch naming conventions used correctly | 15 |
| Multiple convention branches merged and cleaned up | 10 |
| Repository forked on GitHub | 10 |
| Fork cloned and upstream remote added | 15 |
| Fork synced with upstream | 10 |
| Full feature branch workflow completed with best practices | 25 |
| **Total** | **100** |
