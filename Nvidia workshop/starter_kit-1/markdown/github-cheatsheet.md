# GitHub Cheatsheet for NVIDIA Cloud Lab Terminal Users - (C) AiProff.ai

## 📚 Table of Contents
- [Why Use GitHub?](#why-use-github)
- [First-Time Setup: Logging Into GitHub](#first-time-setup-logging-into-github)
- [Creating Your First Repository](#creating-your-first-repository)
- [Basic Git Workflow](#basic-git-workflow)
- [Working with Branches](#working-with-branches)
- [Cloning Existing Repositories](#cloning-existing-repositories)
- [Pushing Media Files (Videos, Images)](#pushing-media-files-videos-images)
- [Pro Tips](#pro-tips)

---

## ⚠️ Important Note

The data transfer throughput is limited by the edge device limitations, which may result in slower upload speeds when pushing to GitHub.

---

## Why Use GitHub?

You're working on our cloud-based NVIDIA Cloud Lab with 3-hour sessions. While your data is saved on our NVIDIA Cloud Lab hardware, using GitHub provides you with:

- **🔒 Backup outside the NVIDIA Cloud Lab environment** - Your work is safe even if something happens to the lab
- **🌍 Access from anywhere** - Continue your work from any device
- **📜 Version control** - Track changes and revert if needed
- **💼 Portfolio** - Showcase your projects to potential employers or collaborators

Think of GitHub as your safety net and portfolio combined!

---

## First-Time Setup: Logging Into GitHub

Before you can push code from the NVIDIA Cloud Lab terminal, you need to authenticate with GitHub. There are two methods:

### Method 1: HTTPS with Personal Access Token (⭐ Recommended for Beginners)

This method is simpler and doesn't require SSH key setup.

**Step 1: Create a Personal Access Token (PAT)**

1. Go to GitHub.com and log in
2. Click your profile picture (top-right) → **Settings**
3. Scroll down and click **Developer settings** (bottom-left)
4. Click **Personal access tokens** → **Tokens (classic)**
5. Click **Generate new token** → **Generate new token (classic)**
6. Give it a name (e.g., "Jetson Lab Access")
7. Set expiration (e.g., 90 days)
8. Check these scopes: `repo`, `workflow`, `write:packages`
9. Click **Generate token**
10. **⚠️ COPY THE TOKEN NOW** - You won't see it again!

**Step 2: Configure Git on NVIDIA Cloud Lab Terminal**

```bash
# Set your GitHub username
git config --global user.name "YourGitHubUsername"

# Set your GitHub email
git config --global user.email "your.email@example.com"
```

**Step 3: When Pushing Code**

When you first push, Git will ask for credentials:
- **Username:** Your GitHub username
- **Password:** Paste your Personal Access Token (NOT your GitHub password)

Git will remember these credentials for future pushes.

---

### Method 2: SSH Keys (For Advanced Users)

SSH is more secure and doesn't require entering credentials each time, but setup is more complex.

**Step 1: Generate SSH Key**

```bash
# Generate a new SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Press Enter to accept default location
# Optionally set a passphrase (or press Enter for none)
```

**Step 2: Add SSH Key to SSH Agent**

```bash
# Start the SSH agent
eval "$(ssh-agent -s)"

# Add your SSH key
ssh-add ~/.ssh/id_ed25519
```

**Step 3: Add SSH Key to GitHub**

```bash
# Copy your public key
cat ~/.ssh/id_ed25519.pub
```

1. Copy the output (starts with `ssh-ed25519`)
2. Go to GitHub.com → **Settings** → **SSH and GPG keys**
3. Click **New SSH key**
4. Give it a title (e.g., "Jetson Lab")
5. Paste the key
6. Click **Add SSH key**

**Step 4: Test Connection**

```bash
ssh -T git@github.com
# You should see: "Hi username! You've successfully authenticated..."
```

**Step 5: Configure Git**

```bash
git config --global user.name "YourGitHubUsername"
git config --global user.email "your.email@example.com"
```

---

## Creating Your First Repository

### Option A: Create Repository on GitHub First (Easier)

**Step 1: Create Repo on GitHub.com**

1. Go to GitHub.com and log in
2. Click the **+** icon (top-right) → **New repository**
3. Enter repository name (e.g., `jetson-project`)
4. Choose **Public** or **Private**
5. ✅ Check **Add a README file**
6. Click **Create repository**

**On the NVIDIA Cloud Lab Terminal, clone the repo -**

```bash
# Navigate to where you want your project
cd ~

# Clone the repository (HTTPS method)
git clone https://github.com/YourUsername/jetson-project.git

# OR clone using SSH method
git clone git@github.com:YourUsername/jetson-project.git

# Enter the project directory
cd jetson-project
```

---

### Option B: Create Repository from Existing Code

If you already have code on the NVIDIA Cloud Lab terminal:

**Step 1: Initialize Git Repository**

```bash
# Navigate to your project folder
cd ~/my-existing-project

# Initialize git
git init

# Add all files to staging
git add .

# Make your first commit
git commit -m "Initial commit"
```

**Step 2: Create Empty Repository on GitHub**

1. Go to GitHub.com → **+** icon → **New repository**
2. Enter repository name
3. ⚠️ **DO NOT** check "Add a README file"
4. Click **Create repository**

**Step 3: Link and Push to GitHub**

```bash
# Add remote repository (HTTPS)
git remote add origin https://github.com/YourUsername/repository-name.git

# OR add remote repository (SSH)
git remote add origin git@github.com:YourUsername/repository-name.git

# Push your code
git branch -M main
git push -u origin main
```

---

## Basic Git Workflow

Once your repository is set up, here's your daily workflow:

### 1. Check Status

```bash
# See what files have changed
git status
```

### 2. Stage Files (Add to Commit)

```bash
# Add specific file
git add filename.py

# Add all changed files
git add .

# Add all Python files
git add *.py
```

### 3. Commit Changes

```bash
# Commit with a message
git commit -m "Add object detection script"

# Commit with detailed message
git commit -m "Add YOLOv8 inference script

- Implemented real-time object detection
- Added support for custom weights
- Fixed memory leak issue"
```

### 4. Push to GitHub

```bash
# Push to main branch
git push origin main

# First time pushing? Use -u flag
git push -u origin main
```

### 5. Pull Latest Changes

```bash
# Get latest changes from GitHub
git pull origin main
```

### Complete Workflow Example

```bash
# Make changes to your code
nano my_script.py

# Check what changed
git status

# Stage changes
git add my_script.py

# Commit changes
git commit -m "Update detection threshold"

# Push to GitHub
git push origin main
```

---

## Working with Branches

Branches let you work on new features without affecting your main code. This is crucial for experimentation!

### Why Use Branches?

- 🧪 Test new ideas safely
- 👥 Collaborate without conflicts
- 🔄 Keep main branch stable
- 📦 Organize different versions

### Creating and Using Branches

**Step 1: Create a New Branch**

```bash
# Create and switch to new branch
git checkout -b feature-name

# Example: Create branch for testing new model
git checkout -b yolov8-testing
```

**Step 2: Work on Your Branch**

```bash
# Make changes to files
nano model.py

# Stage and commit (same as before)
git add model.py
git commit -m "Test YOLOv8 model integration"
```

**Step 3: Push Branch to GitHub**

```bash
# Push new branch to GitHub
git push -u origin feature-name

# Example
git push -u origin yolov8-testing
```

**Step 4: Switch Between Branches**

```bash
# Switch to main branch
git checkout main

# Switch back to feature branch
git checkout yolov8-testing

# List all branches
git branch
```

**Step 5: Merge Branch into Main** (When Feature is Complete)

```bash
# Switch to main branch
git checkout main

# Merge feature branch
git merge yolov8-testing

# Push merged changes
git push origin main

# Optional: Delete branch after merging
git branch -d yolov8-testing
git push origin --delete yolov8-testing
```

### Branch Workflow Example

```bash
# Start: You're on main branch
git checkout main

# Create branch for new experiment
git checkout -b pose-estimation-test

# Work on your code
nano pose_model.py
git add pose_model.py
git commit -m "Add pose estimation model"

# Push to GitHub
git push -u origin pose-estimation-test

# Continue working...
git add results/
git commit -m "Add initial test results"
git push

# When satisfied, merge to main
git checkout main
git merge pose-estimation-test
git push origin main
```

---

## Cloning Existing Repositories

Want to continue work from a previous session or collaborate with others?

### Clone a Repository

```bash
# Navigate to desired location
cd ~

# Clone repository (HTTPS)
git clone https://github.com/YourUsername/repository-name.git

# Clone repository (SSH)
git clone git@github.com:YourUsername/repository-name.git

# Clone and rename folder
git clone https://github.com/YourUsername/repo.git my-custom-folder

# Enter the repository
cd repository-name
```

### Working with Cloned Repository

```bash
# Always pull latest changes first
git pull origin main

# Create your branch
git checkout -b my-work

# Make changes, commit, push
git add .
git commit -m "Continue work on feature"
git push -u origin my-work
```

---

## Pushing Media Files (Videos, Images)

When working with inference outputs, you'll often want to push videos, images, and other media files to GitHub. Here's how to decide which method to use:

### 📊 Decision Tree: Regular Push vs Git LFS

```
                    Need to push media files?
                              |
                              |
                              v
                    What's the file size?
                              |
                ______________|______________
               |                             |
               v                             v
        File < 100 MB                  File ≥ 100 MB
               |                             |
               v                             v
        ✅ REGULAR PUSH                 ⚠️ MUST USE GIT LFS
        (See Section A)                 (See Section B)
               |                             |
        Simple & Free                   1 GB free storage
        Works immediately               1 GB/month bandwidth
                                       Requires setup
```

**Quick Guide:**
- **Inference images** (JPG, PNG) - Usually < 10 MB → Regular push ✅
- **Short video clips** (< 100 MB) → Regular push ✅
- **Long videos, 4K videos** (≥ 100 MB) → Git LFS required ⚠️
- **Large datasets** → Git LFS required ⚠️

---

### Section A: Regular Push (Files < 100 MB)

For small media files like inference images and short videos.

**Limitations:**
- ⚠️ Maximum file size: 100 MB (hard limit)
- ⚠️ Repository should stay under 1 GB (soft limit)

**How to Push:**

```bash
# Add your media files
git add output_image.jpg
git add inference_video.mp4

# Or add entire folder
git add inference_results/

# Commit
git commit -m "Add inference outputs"

# Push
git push origin main
```

**Example Workflow:**

```bash
# You ran inference and got results
ls inference_results/
# output1.jpg (2 MB)
# output2.jpg (3 MB)
# demo_video.mp4 (45 MB)

# All files are under 100 MB, so regular push works
git add inference_results/
git commit -m "Add YOLOv8 inference results"
git push origin main
```

---

### Section B: Git LFS (Files ≥ 100 MB)

For large video files and datasets.

**What is Git LFS?**
- Git Large File Storage handles big files efficiently
- Stores actual files separately, keeps small "pointers" in your repo
- **Free tier: 1 GB storage + 1 GB/month bandwidth**
- After free limit: Need to purchase data packs

**One-Time Setup:**

```bash
# Step 1: Install Git LFS
git lfs install

# Step 2: Track file types you want to use LFS for
# Track all MP4 videos
git lfs track "*.mp4"

# Track all AVI videos
git lfs track "*.avi"

# Track all MOV videos
git lfs track "*.mov"

# Track specific large image formats
git lfs track "*.tif"
git lfs track "*.tiff"

# Step 3: Add .gitattributes file (created by git lfs track)
git add .gitattributes
git commit -m "Configure Git LFS for video files"
git push origin main
```

**Pushing Large Files with LFS:**

After setup, use regular git commands - LFS handles everything automatically!

```bash
# Add your large video file (e.g., 250 MB)
git add large_inference_video.mp4

# Commit (LFS processes it automatically)
git commit -m "Add full inference video"

# Push (LFS uploads to LFS storage automatically)
git push origin main
```

**Complete Example:**

```bash
# You have a large video file
ls -lh output_video.mp4
# 350M output_video.mp4

# Setup LFS (one-time)
git lfs install
git lfs track "*.mp4"
git add .gitattributes
git commit -m "Setup Git LFS"
git push

# Now push the large file (same commands as regular push!)
git add output_video.mp4
git commit -m "Add high-resolution inference video"
git push origin main

# Done! The 350 MB file is safely in GitHub LFS
```

**Checking LFS Usage:**

```bash
# See which files are tracked by LFS
git lfs ls-files

# Check LFS storage usage (requires GitHub CLI or web interface)
# Visit: https://github.com/settings/billing
```

**Important Notes:**
- ✅ Once LFS is configured, pushing works exactly like regular git
- ✅ Team members cloning your repo will get LFS files automatically
- ⚠️ Keep an eye on your 1 GB storage limit
- ⚠️ Watch your 1 GB/month bandwidth (downloads count against this)

---

### What If I Exceed LFS Limits?

If you go over 1 GB storage or 1 GB/month bandwidth:

**Options:**
1. **Purchase GitHub data packs** ($5/month for 50 GB storage + 50 GB bandwidth)
2. **Use external storage** for very large datasets (Google Drive, AWS S3)
3. **Keep only recent videos** in Git, archive old ones externally
4. **Compress videos** before pushing

---

## Pro Tips

### 🎯 Pro Tip #1: Split-Screen Viewing of Inference Media

When you push inference images or videos, you can view them immediately in GitHub without downloading!

**How to Set It Up:**

1. **On your computer (not NVIDIA Cloud Lab terminal):**
   - Open your terminal/command prompt in one half of the screen
   - Open your web browser with GitHub in the other half

2. **Workflow:**
   ```bash
   # In terminal: Push your inference results
   git add inference_output.jpg
   git commit -m "Add inference result"
   git push origin main
   ```

3. **In browser:**
   - Refresh your GitHub repository page
   - Navigate to the file (e.g., `inference_output.jpg`)
   - Click on it to view immediately!

4. **Why this is useful:**
   - ✅ Instantly verify your results are uploaded correctly
   - ✅ Share results with team members immediately
   - ✅ View high-quality images without downloading
   - ✅ Create visual documentation of your progress

**For Videos:**
- GitHub can play MP4, MOV, and other common formats directly in the browser
- Useful for quickly reviewing inference videos

---

### 🎯 Pro Tip #2: Commit Often, Push Regularly

```bash
# Bad: Work for 3 hours, push once
# Good: Commit every milestone, push regularly

# After implementing a feature
git add feature.py
git commit -m "Implement feature X"
git push

# After fixing a bug
git add bugfix.py
git commit -m "Fix memory leak in inference loop"
git push

# After getting good results
git add results/
git commit -m "Add inference results - 95% accuracy"
git push
```

---

### 🎯 Pro Tip #3: Write Good Commit Messages

```bash
# Bad commit messages
git commit -m "update"
git commit -m "fix"
git commit -m "changes"

# Good commit messages
git commit -m "Update YOLOv8 model weights to v8.0.20"
git commit -m "Fix detection threshold causing false positives"
git commit -m "Add inference script for video processing"
```

---

### 🎯 Pro Tip #4: Use .gitignore for Unnecessary Files

Create a `.gitignore` file to exclude files you don't want to push:

```bash
# Create .gitignore file
nano .gitignore
```

Add these common patterns:

```
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/

# Jupyter Notebooks checkpoints
.ipynb_checkpoints/

# Model weights (if very large)
*.weights
*.pth
*.pt

# Temporary files
*.tmp
*.log
*.swp

# OS files
.DS_Store
Thumbs.db
```

Save and commit:

```bash
git add .gitignore
git commit -m "Add .gitignore"
git push
```

---

### 🎯 Pro Tip #5: Check Before You Push

Always verify what you're about to push:

```bash
# See what files changed
git status

# See exact changes in files
git diff

# See what will be pushed
git log origin/main..HEAD

# Then push
git push origin main
```

---

## Quick Reference Commands

### Essential Commands

| Command | Description |
|---------|-------------|
| `git status` | Check current status |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Commit changes |
| `git push origin main` | Push to main branch |
| `git pull origin main` | Pull latest changes |
| `git log` | View commit history |

### Branch Commands

| Command | Description |
|---------|-------------|
| `git branch` | List branches |
| `git checkout -b name` | Create and switch to branch |
| `git checkout main` | Switch to main branch |
| `git merge branch-name` | Merge branch into current |
| `git branch -d name` | Delete branch locally |

### LFS Commands

| Command | Description |
|---------|-------------|
| `git lfs install` | Install LFS (one-time) |
| `git lfs track "*.mp4"` | Track file type with LFS |
| `git lfs ls-files` | List LFS tracked files |
| `git lfs untrack "*.mp4"` | Stop tracking file type |

---

## Common Workflows Recap

### Starting a New Project

```bash
# On GitHub.com: Create new repository
# Then in NVIDIA Cloud Lab terminal:
git clone https://github.com/YourUsername/new-project.git
cd new-project
# Start coding!
```

### Daily Work

```bash
# Pull latest
git pull origin main

# Make changes
# ... code ...

# Stage, commit, push
git add .
git commit -m "Description of changes"
git push origin main
```

### Working on a Feature

```bash
# Create feature branch
git checkout -b new-feature

# Work and commit
git add .
git commit -m "Implement new feature"
git push -u origin new-feature

# When done, merge to main
git checkout main
git merge new-feature
git push origin main
```

### Pushing Inference Results

```bash
# Small files (< 100 MB)
git add inference_results/
git commit -m "Add inference outputs"
git push origin main

# Large files (≥ 100 MB) - Setup LFS first
git lfs install
git lfs track "*.mp4"
git add .gitattributes
git commit -m "Setup LFS"
git push

# Then push large files normally
git add large_video.mp4
git commit -m "Add full inference video"
git push origin main
```

---

## Need Help?

- **GitHub Documentation:** https://docs.github.com
- **Git LFS Documentation:** https://git-lfs.github.com
- **Git Basics Tutorial:** https://git-scm.com/book/en/v2/Getting-Started-Git-Basics

---

**Remember:** GitHub is your backup and portfolio. Commit often, push regularly, and don't be afraid to experiment with branches!

Happy Coding on NVIDIA Cloud Lab !
