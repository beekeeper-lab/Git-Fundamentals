# Module 15: Git Collaboration Workflows

## Introduction

> 🏷️ Advanced

> 🎯 **Teach:** The three most common Git collaboration workflows and when to use each.
> **See:** Feature branches merged in sequence, naming conventions in practice, and a forking workflow with upstream syncing.
> **Feel:** Ready to collaborate on real team projects with confidence.

> 🎙️ This is the final day -- and it's where everything comes together. You've learned commits, branches, merges, rebases, stashes, and tags. Now you'll see how real teams combine all of those tools into structured workflows.

> 🔄 **Where this fits:** This is the capstone of the course. Every skill from Days 1 through 14 feeds into these workflows. Branching, merging, conflict resolution, rebasing, stashing, tagging -- they're all tools in the collaboration toolbox you're building here.

## Three Workflows Overview

> 🎯 **Teach:** The three major Git workflows and what kind of team each one suits.
> **See:** Feature branch, Gitflow, and forking workflows described side by side.
> **Feel:** Oriented -- you'll know which workflow to reach for in any team setting.

> 🎙️ Teams use different Git workflows depending on their size and needs. The three most common are the feature branch workflow (used by most teams), Gitflow (for larger projects with formal releases), and the forking workflow (used by open source). Let's look at each one before we start practicing.

Teams use different Git workflows depending on their size and needs:

### 1. Feature Branch Workflow (Most Common)

Everyone works on `main`. For each new feature or bugfix, create a short-lived branch. Code gets to main via pull requests. Branches are deleted after merging.

### 2. Gitflow Workflow

Uses dedicated branches for releases, hotfixes, and development:
- `main` -- Production releases only
- `develop` -- Integration branch for features
- `feature/*` -- Individual features
- `release/*` -- Release preparation
- `hotfix/*` -- Emergency production fixes

### 3. Forking Workflow (Open Source)

Each contributor forks the repository, works in their fork, and submits pull requests to the original:

```
Original repo (upstream) ← PR ← Your fork (origin)
```

## Feature Branch Workflow Diagram

> 🎯 **Teach:** How the feature branch workflow looks as a commit graph -- parallel branches merging into main.
> **See:** An ASCII diagram of two features being developed and merged in sequence.
> **Feel:** That the workflow is visual and intuitive, not abstract.

> 🎙️ The feature branch workflow is the one you'll use most. The diagram below shows how two features are developed in parallel and merged into main one at a time. Main stays stable because all work happens on branches, and code only enters main through pull requests.

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

## Set Up a Team Project

> 🎯 **Teach:** How to initialize a shared project that multiple developers will work on.
> **See:** A fresh repo with README and app file -- the starting point for team collaboration.
> **Feel:** Like you're setting up a real team project, not just a practice exercise.

> 🎙️ Let's simulate this workflow hands-on. We'll create a project repo and then develop two features in parallel, just like two teammates would on a real project.

```bash
mkdir ~/workflow-practice
cd ~/workflow-practice
git init

echo "# Team Project" > README.md
echo "app.js" > app.js
git add .
git commit -m "Initial project setup"
```

## Two Features in Parallel

> 🎯 **Teach:** How two developers can work on separate features simultaneously using branches.
> **See:** Two feature branches created from main, each with independent commits.
> **Feel:** The power of branching -- two streams of work happening without interference.

> 🎙️ Now we'll create two feature branches from main, each with its own commits. This simulates two developers working on different features at the same time. Neither one knows about the other's work yet.

Create the first feature branch:

```bash
git switch -c feature/user-auth
echo "function login() { }" > auth.js
git add auth.js
git commit -m "Add login function"

echo "function logout() { }" >> auth.js
git add auth.js
git commit -m "Add logout function"
```

Create a second feature branch from main:

```bash
git switch main
git switch -c feature/dashboard
echo "function renderDashboard() { }" > dashboard.js
git add dashboard.js
git commit -m "Add dashboard renderer"
```

## Merge Features Sequentially

> 🎯 **Teach:** Features are merged into main one at a time, then branches are deleted.
> **See:** Both feature branches merged into main, the graph showing the merged history, branches cleaned up.
> **Feel:** The satisfying rhythm of merge-and-clean that keeps a repo tidy.

> 🎙️ Back on main, we merge one feature at a time. This is how it works on a real team -- pull requests get merged in sequence. After merging, we delete the branches to keep things tidy. Check the graph to see how the history looks.

```bash
git switch main
git merge feature/user-auth
git merge feature/dashboard

git log --oneline --graph --all

git branch -d feature/user-auth
git branch -d feature/dashboard
```

Both features are now in `main` with a clear history. Each feature's commits are preserved, and the branches are cleaned up.

> 💡 **Remember this one thing:** The feature branch workflow boils down to: **branch off main, do your work, merge back, delete the branch**. Keep branches short-lived and focused on one thing.

## Branch Naming Conventions

> 🎯 **Teach:** The standard prefix conventions that teams use for branch names.
> **See:** The five common prefixes: feature/, bugfix/, hotfix/, release/, chore/.
> **Feel:** That naming conventions are simple to follow and make teamwork smoother.

> 🎙️ Branch names matter more than you'd think. On a team, a well-named branch tells everyone what it's for at a glance. Most teams use a prefix-slash-name convention -- feature slash, bugfix slash, hotfix slash. Here are the standard prefixes.

Common prefixes:

- `feature/` -- New functionality
- `bugfix/` -- Bug repairs
- `hotfix/` -- Urgent production fixes
- `release/` -- Release preparation
- `chore/` -- Maintenance tasks

## Create Convention Branches

> 🎯 **Teach:** How to create branches using each naming convention with real commits.
> **See:** Three branches created (feature/, bugfix/, hotfix/), each with a focused commit.
> **Feel:** Comfortable using naming conventions naturally, not as extra overhead.

> 🎙️ Let's practice creating branches with each of these naming conventions. We'll make a feature branch, a bugfix branch, and a hotfix branch, each with a descriptive name that tells the team exactly what it's for.

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

## Merge and Clean Up

> 🎯 **Teach:** The full merge-and-delete cycle for multiple convention branches.
> **See:** All three branches merged into main and then deleted in one batch.
> **Feel:** That branch cleanup is a natural final step, not an afterthought.

> 🎙️ Now merge all three convention branches into main and delete them. This is the rhythm of daily teamwork -- branches come and go, but main keeps moving forward. List all branches before and after so you can see the cleanup in action.

List all branches, then merge everything:

```bash
git branch

git merge feature/add-search-bar
git merge bugfix/fix-login-redirect
git merge hotfix/security-patch
git branch -d feature/add-search-bar bugfix/fix-login-redirect hotfix/security-patch
```

## Fork a Repository

> 🎯 **Teach:** Forking creates your own copy of someone else's repo on GitHub.
> **See:** The Fork button on GitHub and how it creates a copy under your account.
> **Feel:** That contributing to open source starts with a single click.

> 🎙️ Now let's look at the forking workflow -- how open source works. Instead of pushing branches to a shared repository, each contributor has their own complete copy called a fork. You work in your fork and submit pull requests back to the original. Let's walk through it.

1. Go to a public repository on GitHub (e.g., https://github.com/octocat/Spoon-Knife)
2. Click the **"Fork"** button in the top right
3. This creates a copy under your GitHub account

## Clone Your Fork

> 🎯 **Teach:** Cloning your fork gives you a local copy you can push to freely.
> **See:** The git clone command pulling down your forked repository.
> **Feel:** That you now own a full working copy of a real open-source project.

> 🎙️ After forking on GitHub, clone your fork to your local machine. This is your personal copy -- you have full push access to it. The original repository is still out there, and we'll connect to it next.

```bash
cd ~
git clone https://github.com/YOUR-USERNAME/Spoon-Knife.git
cd Spoon-Knife
```

## Add Upstream and Sync

> 🎯 **Teach:** The two-remote setup (origin = your fork, upstream = original) and how to sync them.
> **See:** git remote -v showing both remotes, and fetch/merge pulling updates from upstream.
> **Feel:** In control of your relationship with the original project -- you can always catch up.

> 🎙️ The key to the forking workflow is having two remotes: origin (your fork, which you can push to) and upstream (the original repository, which you pull from). Adding the upstream remote lets you fetch the latest changes from the original project and keep your fork up to date.

```bash
git remote add upstream https://github.com/octocat/Spoon-Knife.git
git remote -v
```

You now have two remotes:
- `origin` -- Your fork (you can push to this)
- `upstream` -- The original repository (read-only for you)

Sync your fork with upstream:

```bash
git fetch upstream
git merge upstream/main
```

This pulls the latest changes from the original project into your local copy. Push to keep your fork updated:

```bash
git push origin main
```

> 💡 **Remember this one thing:** In the forking workflow, `origin` is your fork and `upstream` is the original. Regularly `fetch upstream` and merge to stay in sync.

## The Complete Best-Practices Workflow

> 🎯 **Teach:** The complete professional feature branch workflow from start to finish.
> **See:** Branch creation, focused commits, pre-merge review, merge, and cleanup -- all in one exercise.
> **Feel:** Like a professional developer running through a workflow you could use on day one of a real job.

> 🎙️ Let's put it all together with one final exercise -- the complete feature branch workflow done the professional way. Small, focused commits. Descriptive branch names. Review before merging. Clean up after yourself. This is the rhythm you'll use on every team you join.

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

## Key Takeaways

> 🎯 **Teach:** The professional habits that make Git collaboration smooth.
> **See:** A checklist of daily practices: small commits, descriptive names, clean merges.
> **Feel:** That these habits are simple, memorable, and immediately applicable.

> 🎙️ Here are the professional habits that tie everything together. These aren't just Git tips -- they're team collaboration skills that will make you a better colleague on any project. Small commits, good names, clean merges, and no leftover branches.

- `git log main..HEAD` shows commits on your branch that aren't on main
- `git diff main...HEAD --stat` shows a summary of all changes vs. main
- Small, focused commits are easier to review and revert
- Always delete merged branches to keep the branch list clean
- Use descriptive branch names so the team knows what each branch is for
- Review your own changes before asking others to review them

> 💡 **Remember this one thing:** Good Git habits are team habits. Descriptive branches, focused commits, clean merges, and deleted branches -- these small disciplines make collaboration smooth for everyone.

## Submission

> 🎯 **Teach:** What to capture and submit for this capstone module.
> **See:** The grading rubric covering all exercises from today.
> **Feel:** Proud -- you've completed the entire Git Fundamentals course.

> 🎙️ Save all your terminal output from today's exercises. This is the capstone module, so make sure you captured the parallel features, the naming conventions, the fork workflow, and the best-practices exercise. You've earned this one -- congratulations on finishing the course.

Save a file named `Day_15_Output.md` containing the terminal output from each task.

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
