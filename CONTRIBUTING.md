# Contributing to Goeckoh

Thank you for your interest in contributing to the Goeckoh project! This guide will help you get started with sending your changes to this repository using Git from your terminal.

## Prerequisites

Before you begin, make sure you have:
- Git installed on your system ([Download Git](https://git-scm.com/downloads))
- A GitHub account
- Git configured with your name and email:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```

## Quick Git Workflow

Here are the essential Git commands to send files to this repository from your terminal:

### 1. Clone the Repository (First Time Only)

```bash
git clone https://github.com/kaleidoscopeAI/goeckoh.git
cd goeckoh
```

### 2. Create a New Branch

Always create a new branch for your changes:

```bash
git checkout -b your-feature-branch-name
```

### 3. Make Your Changes

Edit, add, or delete files as needed for your contribution.

### 4. Check Your Changes

See what files you've modified:

```bash
git status
```

View the specific changes:

```bash
git diff
```

### 5. Stage Your Files

Add specific files:

```bash
git add filename.py
```

Or add all changed files:

```bash
git add .
```

### 6. Commit Your Changes

Commit with a descriptive message:

```bash
git commit -m "Add brief description of your changes"
```

For a more detailed commit message:

```bash
git commit
```

This will open your default text editor where you can write:
- A short title (50 characters or less)
- A blank line
- A detailed description of what changed and why

### 7. Push Your Branch to GitHub

```bash
git push origin your-feature-branch-name
```

If it's your first push of this branch, you may need to set the upstream:

```bash
git push -u origin your-feature-branch-name
```

### 8. Create a Pull Request

After pushing, go to https://github.com/kaleidoscopeAI/goeckoh and GitHub will prompt you to create a pull request from your branch.

## Common Scenarios

### Updating Your Branch with Latest Changes

Before starting work or before creating a pull request, sync with the main branch:

```bash
git checkout main
git pull origin main
git checkout your-feature-branch-name
git merge main
```

### Fixing Your Last Commit

If you need to modify your last commit (before pushing):

```bash
git add forgotten-file.py
git commit --amend
```

### Viewing Commit History

```bash
git log
```

Or for a compact view:

```bash
git log --oneline
```

### Undoing Changes

Discard changes to a specific file:

```bash
git restore filename.py
```

Unstage a file (keep changes but remove from staging):

```bash
git restore --staged filename.py
```

## Best Practices

1. **Write clear commit messages**: Explain what changed and why
2. **Keep commits focused**: Each commit should represent one logical change
3. **Test your changes**: Make sure your code works before committing
4. **Pull before pushing**: Always sync with the remote repository before pushing
5. **Use meaningful branch names**: Like `fix-audio-bug` or `add-voice-feature`

## Getting Help

- Check Git documentation: `git help <command>`
- View command options: `git <command> --help`
- GitHub Guides: https://guides.github.com/

## Development Setup

For information on setting up the development environment, see the [README.md](README.md).

## Questions?

If you have questions about contributing, feel free to open an issue in the repository.
