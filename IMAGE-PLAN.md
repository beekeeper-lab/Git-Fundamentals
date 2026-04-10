# Image Plan

Total proposed images: 55

## Generation Cost Log

| Metric | Value |
|--------|-------|
| Images generated | 49 of 55 |
| Remaining (quota hit) | 6 (module-14: 1, module-15: 5) |
| Model | gemini-3-pro-image-preview (nanobanana-pro) |
| Total tokens | 92,229 |
| Total generation time | 19.1 minutes |
| Total image size | 30.2 MB |
| Avg tokens/image | 1,882 |
| Avg time/image | 23.4 seconds |
| **Estimated cost (49 images)** | **$6.86** |
| **Projected total (55 images)** | **$7.70** |
| Cost per image | ~$0.14 |
| Date | 2026-04-09 |
| Quota limit hit | 250 requests/day — retry module-15 after reset |

To generate remaining images:
```bash
uv run --with google-genai python scripts/generate_images.py
```

---

## Module 00: Welcome to Git Fundamentals

### Image 1: Hero - Course Launch
- **File**: `images/module-00/course-launch-hero.png`
- **Page**: 1
- **Placement**: after "Welcome!"
- **Description**: An eye-catching hero image showing a young developer standing at the entrance of a winding trail that climbs through 15 clearly numbered waypoints toward a mountain summit labeled "Git Pro." Sets the tone that this is an achievable journey with clear milestones.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A young developer with a backpack stands at a trailhead, looking up at a winding mountain path. The trail passes through 15 small numbered signposts leading to a sunlit summit. Each signpost has a tiny icon (a gear, a branch, a cloud, a tag). The developer looks eager and confident, not intimidated. A friendly trail guide character shaped like a Git logo waves from the first waypoint.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Three-Week Roadmap
- **File**: `images/module-00/three-week-roadmap.png`
- **Page**: 1
- **Placement**: after "What You'll Learn: Days 1-5"
- **Description**: A visual roadmap showing three columns (Week 1: Foundation, Week 2: Collaboration, Week 3: Advanced) with small icons representing each day's topic. Helps students see the full scope of the course at a glance.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three columns arranged left to right like a game board. The left column (warm yellow) shows icons for foundation skills: a toolbox, files, a magnifying glass. The middle column (warm blue) shows collaboration icons: tree branches, arrows connecting computers, handshakes. The right column (warm red) shows advanced icons: a tangle being untied, a treasure chest, a medal. A dotted path connects all three columns from start to finish.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Daily Structure
- **File**: `images/module-00/daily-structure.png`
- **Page**: 2
- **Placement**: after "How Each Day Works"
- **Description**: Shows the three-part daily structure (Read, Do, Prove) as three connected stations on a conveyor belt, reinforcing the consistent format students will follow every day.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A friendly conveyor belt with three stations. Station 1 has a character sitting in a comfy chair reading a book (labeled with a lightbulb icon). Station 2 shows the same character at a desk typing on a keyboard with a terminal screen glowing (labeled with a wrench icon). Station 3 shows the character proudly holding up a completed checklist (labeled with a checkmark icon). The conveyor belt loops back to Station 1 to show the daily cycle.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 01: What Is Git?

### Image 1: Hero - Version Control Chaos vs Git
- **File**: `images/module-01/version-control-chaos-hero.png`
- **Page**: 1
- **Placement**: after "What Is Version Control?"
- **Description**: A split image showing the chaos of manual version control (essay_v1, essay_final_FINAL files scattered everywhere) on the left versus a calm, organized Git timeline on the right. Immediately conveys why Git matters.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Split scene. Left side: a frantic student surrounded by a tornado of papers labeled "essay_v1", "essay_v2", "essay_final", "essay_FINAL_FINAL_v3", "essay_REALLY_final". The desk is messy, the student looks panicked. Right side: a calm student sitting at a tidy desk with a neat timeline of snapshots floating above their computer like a filmstrip. Each snapshot is a tidy frame. The student looks relaxed and confident.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Five Core Concepts Mental Model
- **File**: `images/module-01/five-core-concepts.png`
- **Page**: 1
- **Placement**: after "Key Concepts"
- **Description**: A visual diagram showing the five key Git concepts (repository, commit, working directory, staging area, branch) as labeled zones in a friendly workshop metaphor, building the mental model students will use throughout the course.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A workshop viewed from above. A large workbench represents the "working directory" where a craftsperson is building something. Next to it is a "packing table" (staging area) where finished pieces are placed into a shipping box. The sealed shipping box goes onto a shelf of neatly stacked boxes (repository/commits). Along the top wall, two parallel conveyor belts (branches) carry different projects. A small framed portrait of the craftsperson hangs on the wall (identity/config).
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Edit-Stage-Commit Flow
- **File**: `images/module-01/edit-stage-commit-flow.png`
- **Page**: 2
- **Placement**: after "Stage and Commit"
- **Description**: A three-step pipeline showing the edit-stage-commit workflow as a visual flow with color-coded states (red for untracked, green for staged, clean for committed). This is the core rhythm students need to internalize.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three connected zones flowing left to right like a pipeline. Zone 1 (warm red tint): a character is sculpting a clay figure at a messy workbench, representing editing. Zone 2 (warm green tint): the character carefully places the finished figure onto a display pedestal under a spotlight, representing staging. Zone 3 (warm blue tint): the figure is sealed inside a glass display case with a small plaque, representing a commit. Arrows flow between zones showing the progression.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 4: Your First Commit Celebration
- **File**: `images/module-01/first-commit-celebration.png`
- **Page**: 3
- **Placement**: after "View Your First Commit"
- **Description**: A celebratory image showing a developer seeing their first commit in the git log, marking the milestone moment. Reinforces the emotional payoff of completing the first full cycle.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A developer sitting at a desk sees their terminal screen showing a single beautiful commit entry. Above the screen, a tiny confetti cannon goes off. A small ribbon banner floats above reading something celebratory. The developer is pumping their fist. On the wall behind them, a timeline shows a single glowing dot -- their first commit -- as the beginning of a long, empty timeline stretching into the future.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 02: The Edit-Stage-Commit Workflow

### Image 1: Hero - The Three Stages of Git
- **File**: `images/module-02/three-stages-hero.png`
- **Page**: 1
- **Placement**: after "The Three Stages of Git"
- **Description**: A warehouse metaphor showing the three Git stages as physical spaces: a workshop (working directory), a loading dock (staging area), and a sealed vault (repository). This visual metaphor makes the abstract stages tangible.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A cross-section view of a warehouse with three clearly distinct rooms connected by conveyor belts. Room 1 (left): a busy workshop with tools, paint, and a character actively building things. Room 2 (middle): a well-lit loading dock where items are being inspected and placed on pallets, ready for shipment. Room 3 (right): a secure vault with numbered shelves, each shelf holding a sealed, labeled crate. Items flow from left to right along the conveyor belts.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Selective Staging Power
- **File**: `images/module-02/selective-staging.png`
- **Page**: 2
- **Placement**: after "Stage Selectively"
- **Description**: Shows a developer choosing which files to include in a commit, like a chef selecting ingredients for a specific dish rather than dumping everything in the pot. Illustrates the power of selective staging.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A chef standing at a prep counter with many different ingredients spread out (labeled as different colored files). The chef is carefully selecting two specific ingredients and placing them into a cooking pot, while deliberately leaving a third ingredient on the counter for later. The pot has a warm green glow (staged). The counter ingredients have a red tint (unstaged). A finished dish on a shelf behind represents a previous commit.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Diff - Unstaged vs Staged
- **File**: `images/module-02/diff-unstaged-vs-staged.png`
- **Page**: 3
- **Placement**: after "Stage and Diff Again"
- **Description**: A side-by-side comparison showing what git diff and git diff --staged reveal at different points in the workflow. Clarifies the subtle but critical distinction between the two commands.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Two magnifying glasses side by side, each held by a detective character. The left detective peers at the gap between a workbench and a loading dock, seeing changes highlighted in red and green (unstaged changes). The right detective peers at the gap between the loading dock and the vault, seeing a different set of highlighted changes (staged changes). Between them, the loading dock acts as the dividing line. Small arrows show the direction each detective is looking.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 03: Repositories and Ignoring Files

### Image 1: Hero - Two Ways to Get a Repo
- **File**: `images/module-03/two-ways-to-get-repo-hero.png`
- **Page**: 1
- **Placement**: after "Introduction"
- **Description**: A visual showing two paths to getting a repository: building from scratch (git init) versus copying an existing one (git clone). Sets up the two main topics for the day.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A fork in a road with a character standing at the junction. The left path leads to an empty plot of land with a sign reading "Build Here" where construction materials are neatly stacked (representing git init). The right path leads to a completed building with a photocopier next to it producing an exact replica (representing git clone). Both paths converge at a happy developer working inside a completed building.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Gitignore as a Bouncer
- **File**: `images/module-03/gitignore-bouncer.png`
- **Page**: 2
- **Placement**: after "What Is .gitignore?"
- **Description**: A metaphor showing .gitignore as a bouncer at a velvet rope, letting source code files through while blocking build artifacts, IDE settings, and secret files. Makes the concept of file filtering memorable and fun.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A large bouncer character wearing sunglasses stands at a velvet rope outside a fancy club labeled "Repository." Well-dressed file characters (source code files with .java and .txt extensions) walk past the bouncer into the club. Meanwhile, shady-looking characters are being turned away: a character wearing a trenchcoat labeled ".env" holding a briefcase of secrets, a dusty construction worker labeled "build/", and a character in weird clothes labeled ".DS_Store". The bouncer holds a clipboard (the .gitignore list).
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Clone - A Complete Copy
- **File**: `images/module-03/clone-complete-copy.png`
- **Page**: 3
- **Placement**: after "What Is Cloning?"
- **Description**: Shows that cloning creates a complete, independent copy with full history, not just the latest files. Distinguishes cloning from downloading a ZIP.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Two identical bookshelves side by side. The left bookshelf (the remote) is labeled "GitHub" and sits in a cloud. The right bookshelf (the clone) sits on a desk. Both shelves contain the exact same books in the same order, representing the full commit history. A magical beam connects them showing the clone operation. A small ZIP file icon in the corner is crossed out with an X, with only a single book next to it, showing that a ZIP only gets the latest version.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 04: Advanced Staging and Commit Messages

### Image 1: Hero - Staging Toolkit
- **File**: `images/module-04/staging-toolkit-hero.png`
- **Page**: 1
- **Placement**: after "Staging Strategies"
- **Description**: A hero image showing the expanded staging toolkit: staging by file, by directory, by pattern, and unstaging. Positions this module as a level-up from basic staging.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A developer standing before an open toolbox that is much larger than the small toolbox from earlier lessons. Inside the toolbox are specialized tools: a single-file grabber (tweezers), a directory scoop (a small shovel), a pattern net (a butterfly net with a star pattern), and a reverse tool (an undo magnet). The developer is reaching for the pattern net with a confident expression. A small "Level 2" badge glows in the corner.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Good vs Bad Commit Messages
- **File**: `images/module-04/good-vs-bad-commit-messages.png`
- **Page**: 3
- **Placement**: after "What Makes a Good Commit Message?"
- **Description**: A side-by-side comparison of good versus bad commit messages, showing how future-you reacts to each. Makes the case for descriptive messages through humor.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Two panels side by side. Left panel: A developer six months in the future opens a git log and sees a message reading only "fix bug." The developer is confused, scratching their head, surrounded by question marks. A calendar on the wall shows it is months later. Right panel: The same future developer opens a git log with a clear, descriptive message. The developer is smiling and nodding with a lightbulb above their head. A thought bubble shows them easily finding and understanding the change.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Amend as an Eraser
- **File**: `images/module-04/amend-eraser.png`
- **Page**: 4
- **Placement**: after "Fix a Commit Message with Amend"
- **Description**: Shows git commit --amend as erasing and rewriting the most recent commit, with a warning sign about not amending pushed commits. Conveys both the power and the safety boundary.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A timeline of commits shown as framed photos on a wall. The most recent photo (at the end) is being carefully removed by a developer holding a new, improved version. The developer is swapping the old frame for a new one with a corrected label. A caution tape barrier separates the recent commits from older ones labeled "already shared," with a friendly warning sign indicating those cannot be swapped.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 05: Viewing History

### Image 1: Hero - Git as a Time Machine
- **File**: `images/module-05/time-machine-hero.png`
- **Page**: 1
- **Placement**: after "Introduction"
- **Description**: A hero image portraying Git history as a time machine, with the developer able to look back through a window at any point in the project's past. Sets the tone for a day about exploring history.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A developer sitting in a whimsical time machine shaped like a desk chair with a control panel. Through a large circular window in front of them, different moments in the project's history are visible as snapshots arranged along a glowing timeline. The developer is turning a dial to scroll through the snapshots. Each snapshot shows a slightly different version of the same project, getting progressively more developed from left to right.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Log Format Comparison
- **File**: `images/module-05/log-format-comparison.png`
- **Page**: 1
- **Placement**: after "Basic Log Formats"
- **Description**: A visual comparison of three log formats (full, oneline, graph) showing the same history in different levels of detail, like zooming in and out on a map.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three picture frames on a wall, each showing the same landscape (representing the same commit history) at different zoom levels. The left frame shows a highly detailed, full-page view with every detail visible (full log). The middle frame shows a compressed thumbnail strip view (oneline). The right frame shows a bird's-eye satellite view with branching rivers visible (graph). A character with binoculars stands below, choosing which view to use.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Git Blame Detective
- **File**: `images/module-05/git-blame-detective.png`
- **Page**: 3
- **Placement**: after "Running git blame"
- **Description**: Shows git blame as a forensic investigation tool, with each line of a file tagged with its author and date like evidence tags at a crime scene. Makes the concept memorable through the detective metaphor.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A detective character with a magnifying glass examines a document pinned to a corkboard. Each line of the document has a small evidence tag attached to it with a string, and each tag shows a tiny avatar, a date, and a case number (commit hash). The detective is connecting the tags to photos of different "suspects" (authors) pinned around the edges of the board. The mood is playful investigation, not sinister.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 4: HEAD~N Navigation
- **File**: `images/module-05/head-tilde-navigation.png`
- **Page**: 3
- **Placement**: after "The HEAD~N Notation"
- **Description**: A visual showing HEAD as a pointer with relative navigation (HEAD~1, HEAD~2, HEAD~3) illustrated as stepping stones back through history. Demystifies the tilde notation.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A series of stepping stones in a stream, each representing a commit. A character labeled "HEAD" stands on the most recent stone. Behind them, the stones are labeled ~1, ~2, ~3 getting smaller as they recede into the distance. The character is looking back over their shoulder, able to hop to any previous stone. The stream flows forward representing the flow of time. The current stone glows brightest, with earlier stones slightly dimmer.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 06: Branching Basics

### Image 1: Hero - Parallel Railroad Tracks
- **File**: `images/module-06/parallel-railroad-tracks-hero.png`
- **Page**: 1
- **Placement**: after "Introduction"
- **Description**: A hero image showing branches as parallel railroad tracks diverging from a main line. Each track carries different cargo (features) independently. Establishes the branching mental model for the entire second week.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: An aerial view of a railroad junction. The main track runs straight through the center. At a switch point, two branch tracks split off in different directions, each carrying a different colored train with different cargo. The main track's train is stable and steady. The branch trains are smaller and experimental-looking, carrying new features. A friendly signal operator sits in a control tower, ready to switch between tracks. The tracks are labeled with tiny flags.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Files Appear and Disappear
- **File**: `images/module-06/files-appear-disappear.png`
- **Page**: 2
- **Placement**: after "Switch Back to Main"
- **Description**: The "aha moment" illustration showing files physically appearing and disappearing as branches are switched. This is the key conceptual breakthrough of the module.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Two snapshots of the same desk, side by side like a magic trick reveal. Left snapshot: the desk shows files A, B, and C, with a small branch label "feature" floating above. Right snapshot: the same desk now shows only file A, with files B and C fading away like ghosts, and the branch label reads "main." A magician's hand holds a wand (the git switch command) between the two snapshots. The developer watches with wide eyes and an amazed expression.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Branch Graph Visualization
- **File**: `images/module-06/branch-graph-visualization.png`
- **Page**: 3
- **Placement**: after "Visualize the Branches"
- **Description**: A clean, colorful diagram showing three branches (main, feature-greeting, feature-about) diverging from a common point, matching the exercise the student just completed. Reinforces the graph mental model.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A tree growing from a single trunk that splits into three colorful branches. Each branch has different colored leaves (representing commits). The trunk is labeled with a small flag, and each branch has its own small flag with a different name. The tree is growing from left to right (horizontally) rather than bottom to top, matching the way Git graphs are typically shown. Small birds sit on different branches, each working on something different.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 07: Merging Branches

### Image 1: Hero - Bringing Work Together
- **File**: `images/module-07/merging-hero.png`
- **Page**: 1
- **Placement**: after "Introduction"
- **Description**: A hero image showing merging as two rivers joining into one, representing how separate lines of development come back together. Sets up the module's theme of integration.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: An aerial view of two rivers (colored differently, one blue and one green) flowing from different mountain sources and merging into a single, wider river. Small boats on each river carry different cargo (representing different features). At the confluence point, the boats come together and continue downstream as a combined fleet. The merged river is broader and richer in color. A signpost at the junction shows the merge point.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Fast-Forward vs Three-Way Merge
- **File**: `images/module-07/fast-forward-vs-three-way.png`
- **Page**: 1
- **Placement**: after "Three-Way Merge"
- **Description**: A side-by-side comparison of the two merge types using a simple visual metaphor. Fast-forward is a pointer sliding forward; three-way merge creates a new junction commit. The most important concept in the module.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Two panels. Left panel (Fast-Forward): A bookmark in a book simply slides forward from page 3 to page 5 -- the pages were already written, the bookmark just caught up. The path is a straight line. Right panel (Three-Way Merge): Two people at a table, each bringing their own puzzle pieces. They combine the pieces into a new, complete puzzle that sits on the table between them. A new frame (the merge commit) surrounds the completed puzzle. The left panel feels effortless; the right panel feels collaborative.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Merge Commit Diamond
- **File**: `images/module-07/merge-commit-diamond.png`
- **Page**: 3
- **Placement**: after "Three-Way Merge"
- **Description**: Shows the classic diamond-shaped merge pattern in a commit graph where two branches diverge and then reconverge at a merge commit. This shape is one students will see repeatedly.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A road map showing two roads diverging from a single intersection, running parallel for a while, then meeting again at another intersection further along. Each road has small milestone markers (commits). At the second intersection, a special roundabout (the merge commit) connects both roads back into one. Cars from both roads merge into a single lane past the roundabout. The diamond shape formed by the two roads between intersections is highlighted with a subtle glow.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 08: Remote Repositories

### Image 1: Hero - Local Meets Cloud
- **File**: `images/module-08/local-meets-cloud-hero.png`
- **Page**: 1
- **Placement**: after "Introduction"
- **Description**: A hero image showing the bridge between local development and GitHub. A developer's laptop connects to a cloud server, transitioning from solo work to team collaboration. Marks the major shift in the course.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A developer at a desk with their laptop. From the laptop, a glowing bridge extends upward into the clouds where a friendly server building sits (representing GitHub). Packages (commits) are traveling across the bridge in both directions -- some going up (push), some coming down (pull). The laptop side is cozy and personal; the cloud side has multiple desks visible through windows showing other developers. A banner across the bridge marks the crossing from "solo" to "team."
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Push and Pull Arrows
- **File**: `images/module-08/push-pull-arrows.png`
- **Page**: 2
- **Placement**: after "First Push with -u"
- **Description**: A clear diagram showing the push and pull operations between a local repo and a remote, with directional arrows and the concept of upstream tracking. Makes the data flow intuitive.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Two buildings facing each other across a street. The left building (labeled "Local") has a mailroom with an outgoing chute (push) and an incoming slot (pull/fetch). The right building (labeled "Remote/Origin") has the matching receiving dock and sending window. Large friendly arrows show packages flowing in both directions. A thin dotted line connects the two buildings labeled with a small chain link icon, representing the tracking relationship set up by the -u flag.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Remote-Tracking Branches
- **File**: `images/module-08/remote-tracking-branches.png`
- **Page**: 3
- **Placement**: after "View Remote-Tracking Branches"
- **Description**: A visual showing how origin/main is a local snapshot of the remote's state, not a live connection. Clarifies a concept that confuses many beginners.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A photographer taking a Polaroid picture of a moving train (the remote's branch). The Polaroid photo (representing origin/main) sits on a desk, showing where the train was when the photo was taken. Meanwhile, the actual train has moved further down the tracks. A clock shows the photo was taken earlier. The photographer holds a camera labeled "fetch" -- taking a new photo updates the snapshot. The gap between the photo and the current train position represents how origin/main can fall behind.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 09: Clone, Fetch, and Pull

### Image 1: Hero - Two Developers, One Remote
- **File**: `images/module-09/two-developers-hero.png`
- **Page**: 1
- **Placement**: after "Introduction"
- **Description**: A hero image showing two developers (Developer A and Developer B) connected to the same remote repository, passing changes back and forth. Sets up the collaboration simulation.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Two developers sit at desks on opposite sides of a room. Between them, suspended in the air, floats a glowing hub (the GitHub remote). Both developers have cables connecting their laptops to the hub. Developer A is sending a package upward (pushing). Developer B is receiving a package downward (pulling). The hub acts as the central relay point. Both developers are smiling and waving at each other through the hub's transparent surface, even though they are working independently.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Fetch vs Pull
- **File**: `images/module-09/fetch-vs-pull.png`
- **Page**: 1
- **Placement**: after "Clone vs Fork vs Fetch vs Pull"
- **Description**: A clear comparison showing fetch (download but do not apply) versus pull (download and merge). The most important distinction in the module.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Two panels showing a mail delivery metaphor. Left panel (Fetch): A mail carrier delivers a package to the front porch but does not open the door. The package sits outside, and the homeowner peeks through the window to inspect it before deciding to bring it in. Right panel (Pull): The same mail carrier delivers the package AND walks it inside, placing it directly on the kitchen table. The homeowner looks up surprised as the package appears. A small equation below shows: pull = fetch + merge.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Collaboration Cycle
- **File**: `images/module-09/collaboration-cycle.png`
- **Page**: 3
- **Placement**: after "View Unified History"
- **Description**: A circular diagram showing the complete push-pull collaboration cycle between two developers through a shared remote. Reinforces that collaboration is bidirectional and continuous.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A circular track like a relay race course. Two runners (Developer A and Developer B) are running in the same direction around the track. At the top of the circle is a baton-passing zone (the GitHub remote). Developer A passes a baton (a commit) to the zone, and Developer B picks it up on the other side. Further around the track, Developer B passes a different baton back. The cycle continues endlessly. In the center of the track, a timeline grows longer with each lap, showing the shared history building up.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 10: The Feature Branch Workflow

### Image 1: Hero - The Professional Loop
- **File**: `images/module-10/professional-loop-hero.png`
- **Page**: 1
- **Placement**: after "The Feature Branch Workflow"
- **Description**: A hero image showing the six-step feature branch workflow as a continuous loop: branch, commit, push, PR, merge, sync. This is the heartbeat diagram of professional development.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A circular conveyor belt with six stations, viewed from above like a board game. Station 1: a branch splitting off from a main road. Station 2: a developer making commits (stacking blocks). Station 3: blocks being launched upward to a cloud (push). Station 4: a review desk where another person inspects the work (PR). Station 5: a green checkmark stamp being applied (merge). Station 6: an arrow pulling updates back down from the cloud (sync). The loop continues endlessly, with a developer cheerfully moving through it.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Pull Request Gateway
- **File**: `images/module-10/pull-request-gateway.png`
- **Page**: 2
- **Placement**: after "Open a Pull Request on GitHub"
- **Description**: Shows a pull request as a gateway or checkpoint between feature branches and main, where code is reviewed before being allowed through. Emphasizes the quality-control purpose of PRs.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A grand gateway or archway separating two areas. On the left side, a developer presents their work (a feature branch shown as a stack of colorful pages) to a reviewer sitting at the gateway. The reviewer has a magnifying glass and is examining the pages one by one. On the right side of the gateway is a pristine garden labeled "main" where only approved work is allowed. A green light above the gateway is ready to turn on once the review is complete. The mood is professional but friendly.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Local-Remote Sync Dance
- **File**: `images/module-10/local-remote-sync.png`
- **Page**: 3
- **Placement**: after "Update Your Local Main"
- **Description**: Shows the post-merge sync steps: switching to main, pulling the merged changes, and deleting the local branch. Illustrates why local and remote can be out of sync and how to fix it.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Two clocks side by side -- one on a desk (local) and one on a cloud (remote). The cloud clock is slightly ahead of the desk clock. A developer reaches up and pulls the cloud clock's time down to synchronize the desk clock. Below the clocks, a small branch label is being swept into a trash bin by a broom, representing branch cleanup. The synchronized clocks glow the same warm color, representing a clean, up-to-date local repository.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 11: Merge Conflicts

### Image 1: Hero - Two Writers, One Whiteboard
- **File**: `images/module-11/two-writers-whiteboard-hero.png`
- **Page**: 1
- **Placement**: after "Introduction"
- **Description**: A hero image showing two people trying to write different things on the same line of a whiteboard, with Git standing between them asking "Which one do you want?" Demystifies conflicts by showing they are just a question that needs answering.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Two developers standing on opposite sides of a whiteboard, each reaching toward the same line with different colored markers. Developer A has written something in blue, Developer B has written something in red, both on the same line. Between them stands a friendly referee character (representing Git) with hands up in a "wait" gesture, looking at the camera with a calm expression, as if to say "I need you to decide." The rest of the whiteboard lines are filled in cleanly with no conflicts -- only the one overlapping line is highlighted.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Anatomy of Conflict Markers
- **File**: `images/module-11/conflict-markers-anatomy.png`
- **Page**: 1
- **Placement**: after "Understanding Conflict Markers"
- **Description**: A visual breakdown of the three conflict marker lines, labeling each section clearly. The single most important reference image in this module.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A large document page with a sandwich-like structure in the middle. The top slice of bread is a zigzag line (representing the <<<<<<< markers) colored blue, with an arrow pointing to a label "Your branch's version." The filling shows two distinct layers, separated by a flat divider line (=======). The bottom slice is another zigzag line (>>>>>>>) colored red, with an arrow pointing to "Incoming branch's version." The rest of the document above and below the sandwich is normal and clean. Arrows show that the entire sandwich must be replaced with the final decision.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Three-Step Resolution
- **File**: `images/module-11/three-step-resolution.png`
- **Page**: 2
- **Placement**: after "Complete the Merge"
- **Description**: A simple three-step flow showing the conflict resolution process: Edit the file, git add, git commit. Gives students a clear, repeatable procedure to follow.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three stepping stones across a stream, each showing an action. Stone 1: a hand holding a pencil is editing a document, erasing the conflict markers and writing clean content. Stone 2: the cleaned document is being placed onto a green staging platform. Stone 3: the staged document is being sealed into a frame (the merge commit) with a small ribbon. The stream underneath is turbulent before the first stone but calm after the third, representing the resolution of the conflict.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 4: Merge Abort Safety Net
- **File**: `images/module-11/merge-abort-safety-net.png`
- **Page**: 3
- **Placement**: after "Start a Conflict and Abort"
- **Description**: Shows git merge --abort as a safety net or "undo" button that catches you if a merge gets overwhelming. Builds confidence that conflicts are always escapable.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A trapeze artist (the developer) swinging between two platforms (branches). Below them is a large, visible safety net labeled with a friendly undo symbol. The artist has let go of one trapeze and is reaching for the other, but hasn't caught it yet (representing the in-progress merge). The safety net is brightly colored and reassuring, showing that falling (aborting) is safe and painless. A small "rewind" arrow near the net shows that aborting takes you back to where you started.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 12: Rebasing

### Image 1: Hero - Rewriting the Timeline
- **File**: `images/module-12/rewriting-timeline-hero.png`
- **Page**: 1
- **Placement**: after "Introduction"
- **Description**: A hero image showing rebase as lifting commits off one timeline and replaying them onto another, creating a clean linear history. Captures the essence of what rebasing does.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A developer wearing work gloves carefully lifts a segment of railroad track (representing feature branch commits) off a branching junction and repositions it onto the end of the main track, creating one continuous straight line. The original junction point has a ghostly outline where the track used to branch off. The repositioned track segment glows slightly to indicate the commits have new identities (new hashes). The main track is clean and straight from end to end.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Merge vs Rebase Side-by-Side
- **File**: `images/module-12/merge-vs-rebase-comparison.png`
- **Page**: 1
- **Placement**: after "Merge vs. Rebase"
- **Description**: The definitive side-by-side comparison of merge (preserves branching history) versus rebase (creates linear history). The key decision point students need to understand.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Two framed maps hanging on a wall. Left map (Merge): shows a river system where tributaries join the main river, creating visible forks and confluences. The history is rich and shows exactly where each tributary joined. Right map (Rebase): shows a single, perfectly straight canal with no tributaries -- all the water flows in one clean line. Both maps represent the same total amount of water (same total work), just organized differently. A developer stands between the maps, chin in hand, considering which they prefer.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Golden Rule Warning
- **File**: `images/module-12/golden-rule-warning.png`
- **Page**: 1
- **Placement**: after "The Golden Rule of Rebasing"
- **Description**: A memorable visual warning about the golden rule: never rebase commits that have been pushed to a shared remote. Uses a "do not cross" metaphor to make the rule stick.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A clear boundary line on the ground dividing two zones. On the left (safe zone, green), a developer happily rebases commits on their own local branch -- the commits are being rearranged like tiles on a personal workbench. On the right (danger zone, red), the same commits have been uploaded to a shared billboard that other people are reading. A large friendly "do not cross" barrier separates the zones, with a sign showing that once commits cross to the shared side, they should not be rebased. Other developers on the right side look up from their desks, concerned.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 4: Rebase-Then-Merge Workflow
- **File**: `images/module-12/rebase-then-merge-flow.png`
- **Page**: 2
- **Placement**: after "Fast-Forward Merge After Rebase"
- **Description**: A two-step flow diagram showing the rebase-then-merge workflow that produces the cleanest possible history. Shows how rebase enables a fast-forward merge.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A two-step assembly line. Step 1 (Rebase): A worker on a feature branch picks up their commits and carefully places them at the end of the main branch's conveyor belt, straightening the line. Step 2 (Fast-Forward Merge): The main branch pointer, shown as a flag on wheels, simply rolls forward along the now-straight conveyor belt to catch up with the feature commits. No new merge commit is created -- the flag just moves forward. The final result is a perfectly straight conveyor belt with one continuous line of commits.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 13: Stashing

### Image 1: Hero - Bookmark Your Work
- **File**: `images/module-13/bookmark-your-work-hero.png`
- **Page**: 1
- **Placement**: after "Introduction"
- **Description**: A hero image showing stash as placing a bookmark in your work and setting it aside on a shelf while you handle an urgent interruption. Captures the everyday scenario that makes stashing essential.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A developer is working at a desk with papers and code spread out. A phone rings urgently (representing an interrupt -- a bug report). The developer calmly places a large, colorful bookmark into the pile of work, then slides the entire pile onto a nearby shelf labeled "Stash Shelf." The desk is now clean and ready for the emergency task. On the shelf, previous bookmarked piles are also visible, neatly stacked. The developer's expression is calm and organized, not stressed.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Stash Stack (LIFO)
- **File**: `images/module-13/stash-stack-lifo.png`
- **Page**: 2
- **Placement**: after "Create Multiple Stashes"
- **Description**: Shows the stash as a stack of trays (last in, first out) with numbered positions. Makes the LIFO data structure concept visual and intuitive.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A spring-loaded cafeteria tray dispenser with three colorful trays stacked on top of each other. The top tray (most recent, labeled stash 0) is easily accessible. The middle tray (stash 1) is partially visible. The bottom tray (stash 2) is barely visible. A developer reaches for the top tray. Arrows show that new trays go on top (push) and are taken from the top (pop). A small side view shows a developer reaching deeper to grab a specific tray from the middle (apply stash at 1).
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Stash-Switch-Fix-Switch-Pop Pattern
- **File**: `images/module-13/stash-switch-fix-switch-pop.png`
- **Page**: 3
- **Placement**: after "The Real-World Use Case"
- **Description**: A comic-strip style sequence showing the five-step real-world stashing pattern: working on a feature, getting interrupted, stashing, fixing the bug, and returning to the feature. The most practical takeaway from the module.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A five-panel comic strip flowing left to right. Panel 1: Developer happily coding on a feature branch, desk covered in work. Panel 2: An alarm goes off (urgent bug), developer looks startled. Panel 3: Developer slides work into a drawer (stash) and the desk is clean; a sign on the desk changes from "Feature" to "Main." Panel 4: Developer quickly fixes the bug, looking focused and efficient, with a small checkmark appearing. Panel 5: Developer returns to their feature branch, opens the drawer (pop), and the work is back on the desk exactly as before. The developer smiles with relief.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 14: Tags and Releases

### Image 1: Hero - Milestones on the Timeline
- **File**: `images/module-14/milestones-timeline-hero.png`
- **Page**: 1
- **Placement**: after "Introduction"
- **Description**: A hero image showing tags as permanent milestone markers along a project timeline, contrasting with branches which are temporary and moving. Establishes the core purpose of tags.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A long road stretching into the distance (the project timeline). Along the road, permanent stone mile markers stand at specific points, each engraved with a version number (v1.0, v1.1, v2.0). The markers are solid and immovable. In contrast, a few lightweight flags on the road are blowing in the wind and moving forward (representing branches that advance with new commits). A developer stands at the latest mile marker, planting a new stone marker with a ceremonial mallet.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Semantic Versioning Explained
- **File**: `images/module-14/semantic-versioning.png`
- **Page**: 1
- **Placement**: after "Semantic Versioning"
- **Description**: A visual breakdown of the MAJOR.MINOR.PATCH convention showing what each number means and when it increments. Makes the versioning system intuitive through a building metaphor.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three floors of a building representing the three version numbers. The ground floor (PATCH) shows a maintenance worker patching a small crack in the wall -- small fixes, nothing new. The middle floor (MINOR) shows a construction worker adding a new room onto the building -- new features, but the existing structure is intact. The top floor (MAJOR) shows architects with blueprints completely redesigning the building layout -- breaking changes, everything shifts. Each floor has a counter displaying its number, and the full version number is assembled on the building's facade.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Annotated vs Lightweight Tags
- **File**: `images/module-14/annotated-vs-lightweight.png`
- **Page**: 2
- **Placement**: after "Create a Lightweight Tag"
- **Description**: A comparison showing annotated tags (with metadata: who, when, why) versus lightweight tags (just a name). Helps students understand when to use each type.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Two gift tags side by side. The left tag (annotated) is large, detailed, and has a full shipping label with the sender's name, date, a description message, and a signature -- like a proper package label. The right tag (lightweight) is a tiny blank sticky note with just a name scribbled on it -- quick but minimal. Both are attached to identical packages (commits). The annotated tag looks professional and informative; the lightweight tag looks casual and quick. An arrow points to the annotated tag with a thumbs-up.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 4: Detached HEAD Warning
- **File**: `images/module-14/detached-head-warning.png`
- **Page**: 3
- **Placement**: after "Check Out a Tag (Detached HEAD)"
- **Description**: A visual explanation of detached HEAD state when checking out a tag: you are viewing a historical snapshot but not on any branch. Prevents confusion about this common warning.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A museum visitor (the developer) has stepped through a velvet rope to stand inside a historical diorama (a tagged commit). They are looking around at the preserved scene, taking notes. A museum guard (Git) stands nearby with a polite sign reminding them this is "look but don't build here." Outside the diorama, the main exhibition hallway (branches) continues forward. The visitor needs to step back into the hallway to resume normal work. A floating compass icon (HEAD) is shown disconnected from any branch label.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

---

## Module 15: Git Collaboration Workflows

### Image 1: Hero - Three Workflows Overview
- **File**: `images/module-15/three-workflows-hero.png`
- **Page**: 1
- **Placement**: after "Three Workflows Overview"
- **Description**: A hero image showing the three major collaboration workflows (Feature Branch, Gitflow, Forking) as three different team configurations. The capstone image that shows how everything fits together.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three distinct team setups arranged in a triptych. Left panel (Feature Branch): A small agile team of 3-4 developers around a single shared whiteboard, each with a colored marker drawing their own line that merges into the center. Middle panel (Gitflow): A larger, more structured team with a project manager directing traffic between different lanes (develop, release, hotfix) like an air traffic controller. Right panel (Forking): A wide-open commons where many independent developers each work at their own copy of a blueprint, submitting suggestions back to the original architect.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 2: Feature Branch Workflow Diagram
- **File**: `images/module-15/feature-branch-workflow-diagram.png`
- **Page**: 1
- **Placement**: after "Feature Branch Workflow Diagram"
- **Description**: A polished version of the ASCII feature branch diagram showing parallel features being developed and merged into main. The visual students will remember as the standard workflow.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A horizontal highway (main branch) running left to right. Two exit ramps branch off at different points, loop around through short scenic routes (feature work), then merge back onto the highway via on-ramps. Each scenic route has a few small rest stops (commits). The highway continues straight and wide, carrying all the combined traffic. Small cars on each route carry different colored cargo. The on-ramps have toll booths (representing pull request reviews) where cars are inspected before joining the highway.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 3: Gitflow Branch Structure
- **File**: `images/module-15/gitflow-branch-structure.png`
- **Page**: 2
- **Placement**: after "2. Gitflow Workflow"
- **Description**: A diagram showing the Gitflow branch structure with its five branch types (main, develop, feature, release, hotfix) and how code flows between them. The most complex diagram in the course.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A multi-level building cross-section. The ground floor (main) is a solid foundation that rarely changes, with version tags on the walls. The second floor (develop) is a busy workshop where features are assembled. Above that, multiple small workrooms (feature branches) open onto the second floor. A separate elevator shaft (release branch) connects the second floor to the ground floor for controlled deployments. An emergency staircase (hotfix) connects directly from the ground floor back to itself, bypassing the second floor for urgent fixes. Workers move between levels following clear pathways.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 4: Forking Workflow - Origin and Upstream
- **File**: `images/module-15/forking-workflow.png`
- **Page**: 3
- **Placement**: after "Add Upstream and Sync"
- **Description**: Shows the two-remote setup in the forking workflow: origin (your fork) and upstream (the original repo). Critical for understanding open-source contribution.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: Three buildings arranged in a triangle. The top building (upstream, the original project) is a grand library maintained by a head librarian. The bottom-left building (origin, your fork) is your personal copy of the library on your own property. The bottom-right building (local) is your reading desk at home. Arrows show the flow: you can freely carry books between your fork and your local desk (push/pull). You can request the head librarian to accept your contributions (pull request arrow going up). You can also copy new books from the original library to stay updated (fetch upstream arrow coming down).
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots

### Image 5: Course Completion - The Full Toolkit
- **File**: `images/module-15/course-completion-toolkit.png`
- **Page**: 4
- **Placement**: after "Key Takeaways"
- **Description**: A celebratory closing image showing the student's complete Git toolkit -- every skill learned across all 15 days arranged as tools in a professional toolbox. Provides a sense of accomplishment and mastery.
- **Status**: Not generated
- **Prompt**:
  Goal: editorial illustration for a programming textbook
  Scene: A developer stands proudly next to a large, fully loaded professional toolbox. Each drawer and compartment is labeled with a tool from the course: commits, branches, merges, remotes, pull requests, rebasing, stashing, tags. The toolbox glows warmly, fully equipped. Behind the developer, a certificate or diploma hangs on the wall. In the distance through a window, a city skyline of software projects awaits. The developer rolls up their sleeves, ready to join a team and start building.
  Style: Head First book illustration style, clean lines, slightly whimsical and humorous, warm colors, educational
  Aspect ratio: 16:9
  Background: white
  Text in image: minimal or none
  Avoid: photorealistic, dark, scary, complex UI screenshots
