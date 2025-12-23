# Contributing to Goeckoh

Thank you for your interest in contributing to the Goeckoh Neuro-Acoustic Exocortex project! This guide will help you understand how to send files and changes to this repository from your terminal.

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Initial Setup](#initial-setup)
- [Making Changes](#making-changes)
- [Committing Your Changes](#committing-your-changes)
- [Pushing to the Repository](#pushing-to-the-repository)
- [Creating a Pull Request](#creating-a-pull-request)
- [Common Workflows](#common-workflows)
- [Troubleshooting](#troubleshooting)

## Prerequisites

Before you begin, make sure you have:

1. **Git installed** on your system
   ```bash
   git --version
   ```
   If not installed, visit: https://git-scm.com/downloads

2. **GitHub account** with access to this repository

3. **Git configured** with your name and email
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

## Initial Setup

### 1. Clone the Repository

If you haven't already cloned the repository:

```bash
# Clone the repository
git clone https://github.com/kaleidoscopeAI/goeckoh.git

# Navigate to the repository directory
cd goeckoh
```

### 2. Verify Your Setup

```bash
# Check your current branch
git branch

# Check remote repository
git remote -v
```

## Making Changes

### 1. Create a New Branch (Recommended)

Always create a new branch for your changes:

```bash
# Create and switch to a new branch
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b fix/your-fix-name
```

### 2. Make Your Changes

Edit, add, or delete files as needed using your preferred editor or IDE.

### 3. Check What Changed

```bash
# See which files were modified
git status

# See the specific changes in files
git diff

# See changes for a specific file
git diff path/to/file
```

## Committing Your Changes

### 1. Stage Your Files

Stage the files you want to commit:

```bash
# Stage a specific file
git add path/to/file

# Stage multiple files
git add file1.py file2.js file3.md

# Stage all changed files
git add .

# Stage all files of a specific type
git add *.py
```

### 2. Review Staged Changes

```bash
# See what's staged for commit
git status

# See the detailed changes that are staged
git diff --staged
```

### 3. Commit Your Changes

```bash
# Commit with a descriptive message
git commit -m "Add feature: descriptive message about your changes"

# For multi-line commit messages
git commit -m "Short summary of changes" -m "Longer description of what changed and why"
```

**Commit Message Best Practices:**
- Use present tense ("Add feature" not "Added feature")
- Be descriptive but concise
- Reference issue numbers if applicable (e.g., "Fix #123: Resolve audio bug")

### Example Commit Messages:
```bash
git commit -m "Add voice cloning documentation"
git commit -m "Fix audio pipeline initialization error"
git commit -m "Update dependencies in requirements.txt"
git commit -m "Refactor echo_core.py for better performance"
```

## Pushing to the Repository

### 1. Push Your Branch

```bash
# Push your branch to GitHub
git push origin your-branch-name

# For the first push of a new branch, use:
git push -u origin your-branch-name
```

### 2. If Push is Rejected

If your push is rejected, you may need to pull the latest changes first:

```bash
# Pull the latest changes from the main branch
git pull origin main

# Resolve any merge conflicts if they occur
# Then push again
git push origin your-branch-name
```

## Creating a Pull Request

After pushing your branch:

1. Go to https://github.com/kaleidoscopeAI/goeckoh
2. You'll see a notification about your recently pushed branch
3. Click "Compare & pull request"
4. Fill in the pull request details:
   - **Title**: Brief description of your changes
   - **Description**: Detailed explanation of what changed and why
5. Click "Create pull request"

## Common Workflows

### Quick Workflow: Add and Commit All Changes

```bash
# Check what changed
git status

# Add all changes
git add .

# Commit with message
git commit -m "Your commit message here"

# Push to repository
git push origin your-branch-name
```

### Working with Main Branch (Use with Caution)

```bash
# Switch to main branch
git checkout main

# Pull latest changes
git pull origin main

# Make your changes...

# Add and commit
git add .
git commit -m "Your message"

# Push to main (only if you have permission)
git push origin main
```

### Update Your Branch with Latest Changes

```bash
# Save your current work
git add .
git commit -m "WIP: Save current work"

# Switch to main and update
git checkout main
git pull origin main

# Switch back to your branch
git checkout your-branch-name

# Merge main into your branch
git merge main

# Or rebase (alternative to merge)
git rebase main
```

### Undo Changes

```bash
# Discard changes in a specific file (before staging)
git checkout -- path/to/file

# Unstage a file (keep the changes)
git reset HEAD path/to/file

# Undo the last commit (keep changes)
git reset --soft HEAD~1

# Undo the last commit (discard changes) - USE WITH CAUTION
git reset --hard HEAD~1
```

## Complete Example: Adding a New Feature

Here's a complete workflow from start to finish:

```bash
# 1. Clone the repository (if you haven't already)
git clone https://github.com/kaleidoscopeAI/goeckoh.git
cd goeckoh

# 2. Create a new branch
git checkout -b feature/new-audio-filter

# 3. Make your changes (edit files, add new files, etc.)
# ... edit files ...

# 4. Check what changed
git status
git diff

# 5. Stage your changes
git add audio_manager.py
git add tests/test_audio_manager.py

# 6. Commit your changes
git commit -m "Add new audio filter for noise reduction"

# 7. Push to GitHub
git push -u origin feature/new-audio-filter

# 8. Create a Pull Request on GitHub
# Go to the repository URL and follow the prompts
```

## Troubleshooting

### "Permission denied" Error

Make sure you have:
- Authenticated with GitHub (use SSH keys or personal access token)
- Access to the repository
- Set up SSH: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

### "Your branch is behind" Message

```bash
# Pull the latest changes
git pull origin your-branch-name

# If there are conflicts, resolve them, then:
git add .
git commit -m "Merge remote changes"
git push origin your-branch-name
```

### Accidentally Committed to Wrong Branch

```bash
# Create a new branch with current changes
git branch correct-branch-name

# Reset current branch to previous state
git reset --hard HEAD~1

# Switch to the correct branch
git checkout correct-branch-name

# Push the correct branch
git push -u origin correct-branch-name
```

### Need to Change Last Commit Message

```bash
# Amend the last commit
git commit --amend -m "New commit message"

# If already pushed, force push (use carefully)
git push --force origin your-branch-name
```

## Git Configuration Tips

### Set Up Git Aliases (Shortcuts)

```bash
# Create shortcuts for common commands
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit

# Now you can use:
git st  # instead of git status
git co  # instead of git checkout
git br  # instead of git branch
git ci  # instead of git commit
```

### Set Up Default Branch

```bash
# Set default branch name for new repositories
git config --global init.defaultBranch main
```

## Additional Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Understanding Git Branches](https://learngitbranching.js.org/)

## Getting Help

If you need help:

1. Check the [GitHub Issues](https://github.com/kaleidoscopeAI/goeckoh/issues)
2. Read the project documentation in the `docs/` directory
3. Contact the maintainers

---

## Quick Reference: Essential Git Commands

```bash
# Clone repository
git clone <repository-url>

# Check status
git status

# Create new branch
git checkout -b <branch-name>

# Stage files
git add <file>          # specific file
git add .               # all files

# Commit changes
git commit -m "message"

# Push to remote
git push origin <branch-name>

# Pull latest changes
git pull origin <branch-name>

# View commit history
git log

# View remote repositories
git remote -v

# Switch branches
git checkout <branch-name>

# Merge branch
git merge <branch-name>
```

Thank you for contributing to Goeckoh! 🎉
