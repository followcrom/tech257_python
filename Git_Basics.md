
# Git Basics

## Introduction
Git is a distributed version control system that allows developers to track changes in source code during software development.
It's designed for coordinating work among programmers, but it can be used to track changes in any set of files.

## Before Git
Centralized Version Control Systems (CVCS) rely on a single server to store all versions of a project's files, 
with clients checking out files from this central location, simplifying collaboration but creating a single point of failure.

## Basic Commands

### git init
Initializes a new Git repository.

```bash
git init
```

### git clone
Clones a repository into a new directory.

```bash
git clone <repository-url>
```

### git add
Adds files to the staging area.

```bash
git add <file> # Add a single file
git add . # Add all files in the directory
```

### git commit
Commits the staged changes to the repository.

```bash
git commit -m "Commit message"
```

### git status
Shows the status of changes as untracked, modified, or staged.

```bash
git status
```

### git push
Pushes commits to the remote repository.

```bash
git push origin <branch-name>
```

### git pull
Fetches changes from the remote repository and merges them into the current branch.

```bash
git pull origin <branch-name>
```

### git branch
Lists, creates, or deletes branches.

```bash
git branch # List all branches
git branch <branch-name> # Create a new branch
git branch -d <branch-name> # Delete a branch
```

### git checkout
Switches branches or restores working tree files.

```bash
git checkout <branch-name> # Switch to a branch
git checkout -b <branch-name> # Create and switch to a new branch
```

### git merge
Merges two branches together.

```bash
git merge <branch-name>
```

### git log
Shows the commit logs.

```bash
git log
```

## Best Practices
- Commit often with meaningful commit messages.
- Keep your branches short-lived.
- Use branches for features, bug fixes, or experiments.
- Pull changes from the remote before pushing to avoid conflicts.
- Review changes before committing using `git diff` or `git status`.

## Conclusion
Git is a powerful tool for version control and collaboration in software development. Understanding and using these basic commands can help manage your code effectively.
