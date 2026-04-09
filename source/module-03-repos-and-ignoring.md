# Module 3: Repositories and Ignoring Files

## Introduction

> 🎙️ Today you'll learn two essential skills: creating repositories from scratch and from remotes, and using `.gitignore` to keep unwanted files out of your repo. Every real project needs a `.gitignore` — it keeps your repository clean and your secrets safe.

> 🏷️ Start Here

> 🎯 **Teach:** How to create repos with git init and git clone, and how .gitignore works.
> **See:** A project with proper .gitignore patterns filtering out build artifacts and secrets.
> **Feel:** Confident about repository setup and keeping repos clean.

There are two ways to get a Git repository:
1. **`git init`** — Create a new repo from scratch
2. **`git clone <url>`** — Copy an existing repo from a remote server

Most real-world projects also need a `.gitignore` file — a list of patterns telling Git which files to **never track**.

> 🔄 **Where this fits:** Repository creation is a one-time step at the start of any project. The gitignore concepts you learn today will be used in every project you ever work on.

## Build a Project from Scratch

> 🎯 **Teach:** A real project starts with organized directories and an initial commit that captures the structure.
> **See:** Creating `src/`, `build/`, and `docs/` directories, then committing the initial structure.
> **Feel:** Like a professional setting up a project the right way from day one.

> 🎙️ Let's build a properly structured project from scratch. This time we'll create directories for source code, build output, and documentation — just like a real project. Notice how we organize files into folders before making our first commit.

```bash
mkdir ~/git-project
cd ~/git-project
git init
```

Create a basic project structure:

```bash
mkdir src build docs
echo "# My Git Project" > README.md
echo "public class Main { }" > src/Main.java
echo "This is a placeholder." > docs/notes.txt
git add .
git commit -m "Initial project structure"
```

## What Is .gitignore?

> 🎯 **Teach:** Not everything in your project folder should be tracked — build output, IDE settings, and secrets must be excluded.
> **See:** Categories of files that should never be committed: compiled code, IDE configs, OS files, and credentials.
> **Feel:** Aware of the risks of committing the wrong files and ready to prevent it.

> 🎙️ Here's something that trips up beginners — not everything in your project folder should be tracked by Git. Compiled code, dependency folders, IDE settings, and especially secrets like API keys should never be committed. That's what `.gitignore` is for. It's a simple text file that tells Git which files to pretend don't exist.

A `.gitignore` file contains patterns — one per line — that tell Git which files and directories to ignore. Common things to ignore include:

- **Build output** — compiled files, binaries, generated code
- **IDE settings** — `.idea/`, `.vscode/`, `*.iml`
- **OS files** — `.DS_Store`, `Thumbs.db`
- **Secrets** — `.env`, `*.key`, credentials files

## Create a .gitignore

> 🎯 **Teach:** Each line in `.gitignore` is a pattern — directories, extensions, and wildcards all work.
> **See:** Writing a `.gitignore` with patterns for build artifacts, IDE files, OS files, and secrets.
> **Feel:** Methodical — building a safety net that protects your repo from day one.

> 🎙️ Let's create a `.gitignore` file for our project. Each line is a pattern — you can use directory names, file extensions, and wildcards. The comments (lines starting with `#`) help you and your teammates understand why each pattern is there.

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

```bash
git add .gitignore
git commit -m "Add .gitignore for build artifacts and IDE files"
```

## Test That .gitignore Works

> 🎯 **Teach:** Files matching `.gitignore` patterns are invisible to Git — they won't appear in `git status`.
> **See:** Creating `.env`, build output, and IDE config files that are all hidden from `git status`.
> **Feel:** Satisfied that your safety net is working — secrets and junk stay out of your repo.

> 🎙️ Now let's prove it actually works. We'll create files that match the ignore patterns — a `.env` file, some compiled output, and IDE config — and then check `git status`. If the `.gitignore` is working, none of these files will appear.

```bash
echo "SECRET_KEY=abc123" > .env
echo "compiled code" > build/Main.class
mkdir .idea
echo "ide config" > .idea/workspace.xml
git status
```

None of those files should appear. Git is ignoring them.

> 💡 **Remember this one thing:** If a file shouldn't be in your repo (secrets, build output, OS files), add it to `.gitignore` BEFORE you ever track it. Once a file is tracked, `.gitignore` won't help.

## Tracked Files Alongside .gitignore

> 🎯 **Teach:** `.gitignore` only affects untracked files — files already committed continue to be tracked normally.
> **See:** Adding a new source file that shows up in `git status` because `src/` is not ignored.
> **Feel:** Clear on the boundary between ignored and tracked files.

> 🎙️ An important detail — `.gitignore` only affects untracked files. Files you've already committed are still tracked normally. Let's prove that by adding a new source file. It shows up in `git status` because `src/` isn't in our ignore list.

```bash
echo "real code" > src/App.java
git status
git add src/App.java
git commit -m "Add App.java source file"
```

## What Is Cloning?

> 🎯 **Teach:** Cloning creates a complete local copy of a remote repository, including its entire history.
> **See:** The definition of cloning and what it preserves: history, branches, tags, and the remote connection.
> **Feel:** Impressed by Git's distributed nature — every clone is a full, independent copy.

> 🎙️ The other way to get a repository is cloning. When you clone, you get the entire history — every commit ever made. This is what "distributed" means: your clone is a complete, independent copy of the repository. You could disconnect from the internet and still have the full history.

Cloning creates a local copy of a remote repository. Unlike downloading a ZIP file, cloning preserves:
- The entire commit history
- All branches and tags
- The connection back to the remote (called `origin`)

## Clone a Public Repository

> 🎯 **Teach:** `git clone <url>` downloads a full repository from a remote server in one command.
> **See:** Cloning the `octocat/Hello-World` repository from GitHub and entering the new directory.
> **Feel:** Connected to the wider world of open-source code on GitHub.

> 🎙️ Let's try it out. We'll clone a well-known public repository from GitHub. Watch the output — Git tells you what it's downloading and where it's putting it.

```bash
cd ~
git clone https://github.com/octocat/Hello-World.git
cd Hello-World
```

## Examine the Remote

> 🎯 **Teach:** After cloning, Git sets up a remote called `origin` pointing back to the source URL.
> **See:** The output of `git log --oneline` and `git remote -v` showing the connection to GitHub.
> **Feel:** Oriented — you can see where the repo came from and what's in it.

> 🎙️ After cloning, Git automatically sets up a remote called `origin` that points back to where you cloned from. The `git remote -v` command shows you the URL for both fetching (downloading) and pushing (uploading). We'll use remotes extensively starting in Day 8.

```bash
git log --oneline
git remote -v
```

Notice that `origin` is automatically set to where you cloned from.

## Reinitializing Is Safe

> 🎯 **Teach:** Running `git init` on an existing repository is harmless — it changes nothing.
> **See:** The "Reinitialized" message and confirming the project is still intact with `git log` and `git status`.
> **Feel:** Reassured that you can't accidentally break a repo by running `git init` twice.

> 🎙️ One last thing — running `git init` on a folder that's already a repository is perfectly safe. It prints "Reinitialized" and changes nothing. This is good to know so you don't worry about accidentally running it twice.

```bash
cd ~/git-project
git init
```

Confirm your project is intact:

```bash
git log --oneline
git status
cat .gitignore
```

## Submission

> 🎯 **Teach:** How to save your work as proof of completion and what the grading rubric expects.
> **See:** The rubric covering project creation, `.gitignore`, cloning, remotes, and reinitialization.
> **Feel:** Prepared and clear on exactly what to submit.

> 🎙️ Nice work today! You now know both ways to create a repository, and you know how to keep unwanted files out with `.gitignore`. Save your terminal output and check against the rubric below.

Save a file named `Day_03_Output.md` containing the terminal output from each task.

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
