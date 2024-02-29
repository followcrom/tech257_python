# Git / GitHub

## Introduction
Git is a distributed version control system that allows developers to track changes in source code during software development. It's designed for coordinating work among programmers, but it can be used to track changes in any set of files.

## Before Git
Centralized Version Control Systems (CVCS) rely on a single server to store all versions of a project's files, with clients checking out files from this central location, simplifying collaboration but creating a single point of failure.

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

 ### git diff
 
The git diff command shows the differences between various commits, branches, working directory, etc. It's a powerful way to see what has changed.

### git checkout
The git checkout command is used to switch between branches or to check out files or commits. It can be used to update the working directory to match the specified branch, commit, or files.
```git checkout feature-branch```
```git checkout <commit-hash>```

### git reset
`git reset`
The git reset command is used to undo changes. Its effect depends on the options used (--soft, --mixed, --hard).


### git rm --cached <file>
To stop tracking a file in Git without deleting it from your local filesystem, you can use the git rm --cached command. This is particularly useful for files that were accidentally committed and pushed but should have been ignored by Git.

### .gitignore
The .gitignore file is used to tell Git which files or directories to ignore in a project. Any file or pattern listed in .gitignore will not be tracked by Git, which is useful for excluding build directories, temporary files, or sensitive information.

## Branching in Git
Branching in Git allows you to diverge from the main line of development and continue to work independently without affecting the main line. It's a core concept in Git that enables multiple workflows like feature development, fixes, and experiments by creating isolated environments in the repository.

Example:
To create a new branch named feature-branch and switch to it:
`git checkout -b feature-branch`
This command combines the creation of a new branch and checking it out into one step.

Branches are incredibly useful for managing features, fixes, or any changes that you want to keep separate from the main codebase until they're ready to be merged.

## Best Practices
- Commit often with meaningful commit messages.
- Keep your branches short-lived.
- Use branches for features, bug fixes, or experiments.
- Pull changes from the remote before pushing to avoid conflicts.
- Review changes before committing using `git diff` or `git status`.


# Python & Markdown

## Markdown basics

### code block:
```
a = 1
b = 2
c = a + b
print(f"The sum of {a} and {b} is [c}")
```

### Bullet points vs numbered lists
* item 1
* item 2
* item 3
* item 4
  * item 4a
  * item 4b

1. first item
2. second item
   * point about step 2
   * another point
3. third point
4. fourth point
5. 


