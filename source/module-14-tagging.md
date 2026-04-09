# Module 14: Tags and Releases

## Introduction

> 🏷️ Advanced

> 🎙️ Commits have hashes like a3f7b2c -- useful for Git, but not great for humans. When you ship version 1.0 of your software, you want to mark that exact commit with a meaningful name you can find later. That's what tags are for.

> 🎯 **Teach:** How to create and manage Git tags, understand semantic versioning, and create GitHub releases.
> **See:** Annotated vs. lightweight tags, tag inspection, detached HEAD state, and a published GitHub release.
> **Feel:** Equipped to mark important milestones in any project with proper version numbers.

> 🔄 **Where this fits:** You've been making commits and merging branches for two weeks. Tags add a naming layer on top of commits -- they're how teams mark releases, milestones, and stable points in the history.

## What Are Tags?

> 🎙️ Tags are permanent markers for specific commits. While branches move forward as you add commits, a tag stays put -- it always points to the same commit. There are two types: lightweight (just a name) and annotated (a name plus metadata like who tagged it and why). Annotated tags are what you'll use most.

**Tags** are permanent markers for specific commits -- typically used to mark releases (v1.0.0, v2.1.3, etc.).

| Type | Created With | Contains |
|------|-------------|----------|
| **Lightweight** | `git tag v1.0` | Just a name pointing to a commit |
| **Annotated** | `git tag -a v1.0 -m "message"` | Name + tagger + date + message (recommended) |

Annotated tags are preferred because they contain metadata about who created the tag and why.

## Semantic Versioning

> 🎙️ Before we start creating tags, let's talk about how to name them. Most projects follow semantic versioning -- a three-number system that communicates exactly what kind of changes happened. Understanding this convention will make your tags meaningful to anyone who reads them.

Most projects follow the `MAJOR.MINOR.PATCH` convention:

```
v1.0.0 → v1.0.1 → v1.1.0 → v2.0.0
```

- **PATCH** (1.0.0 → 1.0.1) -- Bug fixes, no new features
- **MINOR** (1.0.0 → 1.1.0) -- New features, backwards compatible
- **MAJOR** (1.0.0 → 2.0.0) -- Breaking changes

## Set Up a Repo with History

> 🎙️ Let's create a repo with a few commits that simulate a project's lifecycle -- an initial release, a bugfix, a new feature, and a breaking change. Each of these will get a tag so we can practice the full range of tagging operations.

```bash
mkdir ~/tag-practice
cd ~/tag-practice
git init

echo "v1 code" > app.txt
git add app.txt
git commit -m "Initial release"

echo "v1 bugfix" >> app.txt
git add app.txt
git commit -m "Fix startup bug"

echo "v1.1 feature" >> app.txt
git add app.txt
git commit -m "Add user profiles feature"

echo "v2 breaking change" >> app.txt
git add app.txt
git commit -m "Redesign API (breaking change)"
```

## Create Annotated Tags

> 🎙️ Now let's tag these commits. We'll start with the current commit and work backward. Annotated tags use the dash-a flag and take a message with dash-m. You can tag any commit in the history by specifying its reference -- HEAD tilde 1 for one commit back, HEAD tilde 2 for two back, and so on.

View the history and tag specific commits:

```bash
git log --oneline
```

Tag the current commit (HEAD) as v2.0.0:

```bash
git tag -a v2.0.0 -m "Version 2.0.0: API redesign"
```

Tag past commits to mark earlier releases:

```bash
git tag -a v1.1.0 -m "Version 1.1.0: user profiles" HEAD~1
git tag -a v1.0.1 -m "Version 1.0.1: startup bugfix" HEAD~2
git tag -a v1.0.0 -m "Version 1.0.0: initial release" HEAD~3
```

## Create a Lightweight Tag

> 🎙️ For comparison, let's also create a lightweight tag. No dash-a, no dash-m -- just a name. Lightweight tags are quick and simple, but they don't store any metadata. You'll see the difference when we inspect them in a moment.

```bash
git tag beta-test
```

No `-a` or `-m` -- this creates a simple pointer with no metadata.

## List and Filter Tags

> 🎙️ As a project grows, you might have dozens of tags. The git tag command lists them all, and the dash-l flag lets you filter by pattern. This is how you'd find all the v1 releases, for example, without scrolling through everything.

```bash
git tag
git tag -l "v1.*"
```

The `-l` flag filters tags by pattern.

## Inspect Annotated vs. Lightweight

> 🎙️ Here's where you can really see the difference between the two tag types. When you run git show on an annotated tag, you get the tagger's name, the date, and the message -- plus the commit details. A lightweight tag just shows the commit, nothing extra.

Inspect an annotated tag:

```bash
git show v1.0.0
```

This shows the tag metadata AND the commit it points to. Compare with the lightweight tag:

```bash
git show beta-test
```

No tag metadata -- just the commit.

## View Log with Tags

> 🎙️ Tags also show up in your log output, right next to the commits they point to. The dash dash decorate flag makes them visible. This gives you a nice overview of which commits correspond to which releases.

```bash
git log --oneline --decorate
```

Tags appear in the log next to their commits.

## Check Out a Tag (Detached HEAD)

> 🎙️ You can check out a tag to look at the code as it existed at that point in time. But here's the catch -- it puts you in detached HEAD state. That means you're not on any branch, just viewing a snapshot. Look around all you want, but switch back to a branch when you're done.

```bash
git checkout v1.0.0
```

Git puts you in **detached HEAD** state -- you're looking at historical code, not a branch. Look around:

```bash
cat app.txt
git log --oneline
```

Go back to your branch:

```bash
git switch main
```

> 💡 **Remember this one thing:** Detached HEAD means you're viewing a snapshot, not working on a branch. Always `git switch main` (or another branch) when you're done exploring.

## Push Tags to Remote

> 🎙️ Here's something that catches people off guard -- tags are not pushed automatically when you git push. You have to push them explicitly. Let's connect to a remote and push our tags so they show up on GitHub.

If you have a GitHub repository from earlier days, connect this repo:

```bash
git remote add origin https://github.com/YOUR-USERNAME/git-fundamentals-practice.git
```

Or create a new GitHub repository and connect it.

Tags are NOT pushed by default with `git push`. Push them explicitly:

```bash
# Push a single tag
git push origin v1.0.0

# Push all tags at once
git push origin --tags
```

Check GitHub -- the tags should appear under the "Tags" section of your repository.

> 💡 **Remember this one thing:** Always push tags explicitly with `git push origin --tags`. Regular `git push` does not include tags.

## Delete Tags

> 🎙️ Sometimes you need to remove a tag -- maybe you tagged the wrong commit, or a beta tag has served its purpose. You can delete tags locally with dash-d, and from the remote with push dash dash delete. Let's clean up that beta-test tag.

Delete locally:

```bash
git tag -d beta-test
git tag
```

Delete from the remote:

```bash
git push origin --delete beta-test
```

## GitHub Releases

> 🎙️ Tags mark commits, but GitHub Releases take it a step further. A release bundles a tag with release notes, a changelog, and downloadable archives. It's how open source projects and teams communicate what's new in each version. Let's create one on GitHub.

1. Go to your repository on GitHub
2. Click **"Releases"** on the right sidebar (or go to the Tags tab)
3. Click **"Create a new release"**
4. Choose the tag `v2.0.0`
5. Title: `Version 2.0.0`
6. Description: Write a brief changelog (what changed since v1.1.0)
7. Click **"Publish release"**

Releases are GitHub's way of packaging a tagged version with release notes, changelogs, and downloadable archives. They're especially important for projects where others depend on your code.

> 💡 **Remember this one thing:** A tag is Git's way of naming a commit. A GitHub Release wraps that tag with human-readable notes and downloadable files -- use both together for professional releases.

## Submission

> 🎙️ Save your terminal output and a screenshot of your GitHub release page. Make sure you captured the git show output for both annotated and lightweight tags -- that comparison is a key learning moment.

Save a file named `Day_14_Output.md` containing the terminal output from each task and a screenshot of your GitHub release.

| Criteria | Points |
|----------|--------|
| Annotated tags created for multiple versions | 20 |
| Lightweight tag created for comparison | 5 |
| Tags listed and filtered | 10 |
| `git show` used on annotated vs. lightweight tag | 10 |
| Tag checked out (detached HEAD) and returned to branch | 10 |
| Tags pushed to remote | 15 |
| Tag deleted locally and remotely | 10 |
| GitHub release created from a tag | 20 |
| **Total** | **100** |
