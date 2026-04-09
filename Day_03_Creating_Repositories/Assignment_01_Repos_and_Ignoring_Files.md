# Day 3 Assignment: Repositories and Ignoring Files

## Overview

- **Topic:** Creating Repos, Cloning, and Using `.gitignore`
- **Type:** Technical / Hands-On
- **Estimated Time:** 30 minutes

## Background

There are two ways to get a Git repository:

1. **`git init`** — Create a new repo from scratch (you did this on Day 1)
2. **`git clone <url>`** — Copy an existing repo from a remote server

Most real-world projects also need a `.gitignore` file — a list of patterns telling Git which files to **never track**. Common examples include build output, dependency folders, and IDE configuration files.

Example `.gitignore`:
```
# Compiled output
*.class
*.o
build/

# Dependencies
node_modules/

# IDE files
.idea/
.vscode/

# OS files
.DS_Store
Thumbs.db

# Secrets
.env
*.key
```

Each line is a pattern. Lines starting with `#` are comments. A trailing `/` means "directory only."

---

## Part 1: Creating a Fresh Repository

### Task A: Build a Project from Scratch

Create a new project repository with a proper structure:

```bash
mkdir ~/git-project
cd ~/git-project
git init
```

Create a basic project structure:

```bash
mkdir src
mkdir build
mkdir docs
echo "# My Git Project" > README.md
echo "public class Main { }" > src/Main.java
echo "This is a placeholder." > docs/notes.txt
```

Stage and commit everything:

```bash
git add .
git commit -m "Initial project structure"
```

---

## Part 2: The `.gitignore` File

### Task B: Create a `.gitignore`

Suppose your project generates compiled files and has IDE settings you don't want tracked. Create a `.gitignore`:

```bash
cat > .gitignore << 'EOF'
# Compiled output
build/
*.class

# IDE settings
.idea/
.vscode/
*.iml

# OS files
.DS_Store
Thumbs.db

# Secrets — never commit these
.env
*.key
EOF
```

Stage and commit the `.gitignore`:

```bash
git add .gitignore
git commit -m "Add .gitignore for build artifacts and IDE files"
```

### Task C: Test That `.gitignore` Works

Create files that should be ignored:

```bash
echo "SECRET_KEY=abc123" > .env
echo "compiled code" > build/Main.class
mkdir .idea
echo "ide config" > .idea/workspace.xml
```

Now check status:

```bash
git status
```

None of those files should appear. Git is ignoring them as expected.

### Task D: Prove Tracked Files Are Not Affected

Create a normal file that IS tracked:

```bash
echo "real code" > src/App.java
git status
```

`src/App.java` should appear as untracked — it's not matched by any `.gitignore` pattern.

```bash
git add src/App.java
git commit -m "Add App.java source file"
```

---

## Part 3: Cloning a Repository

### Task E: Clone a Public Repository

Clone a small public repository to see how `git clone` works:

```bash
cd ~
git clone https://github.com/octocat/Hello-World.git
cd Hello-World
```

Explore the cloned repo:

```bash
git log --oneline
git status
ls -la
```

Notice that the cloned repo has the full history — every commit ever made. This is what "distributed" means: your clone is a complete copy.

### Task F: Examine the Remote

```bash
git remote -v
```

This shows where the repo was cloned from. The name `origin` is the default alias for the remote server you cloned from.

---

## Part 4: Reinitializing vs. Starting Fresh

### Task G: See What Happens with `git init` on an Existing Repo

```bash
cd ~/git-project
git init
```

Running `git init` on an existing repo is safe — it prints "Reinitialized existing Git repository" and does not destroy anything. This is useful to know so you don't accidentally worry about it.

### Task H: View Everything Together

```bash
git log --oneline
git status
cat .gitignore
```

Confirm your project has 3 commits and the `.gitignore` is working.

---

## Submission

Save a file named `Day_03_Output.md` in this folder containing the terminal output from each task.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| New project created with directory structure | 15 |
| `.gitignore` created with appropriate patterns | 20 |
| Ignored files confirmed not appearing in `git status` | 20 |
| Tracked files still work alongside `.gitignore` | 10 |
| Public repo cloned and explored | 20 |
| Remote examined with `git remote -v` | 10 |
| `git init` on existing repo demonstrated | 5 |
| **Total** | **100** |
