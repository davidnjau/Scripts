#!/bin/bash

# run `chmod +x git_command.sh`
# ./git_command.sh 


# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Git is not installed on this system. Please install git and try again."
    exit 1
fi

# Check if the current folder is being tracked by git
if ! git rev-parse --is-inside-work-tree &> /dev/null; then
    # Initialize a new Git repository
    git init

    # Add all files to the Git repository
    git add .

    # Prompt for the origin URL
    read -p "Enter the origin URL: " origin_url

    # Add a remote named 'origin' pointing to the provided URL
    git remote add origin $origin_url

    # Prompt for a commit message
    read -p "Enter the commit message: " commit_message

    # Create the commit with the provided message
    git commit -m "$commit_message"

    # Rename the default branch from 'master' to 'main'
    git branch -M main

    # Push the commits to the 'main' branch on the remote repository
    git push -u origin main
else
    # Prompt for a commit message
    read -p "Enter the commit message: " commit_message

    # Add all files to the Git repository
    git add .

    # Create the commit with the provided message
    git commit -m "$commit_message"

    # Check for merge conflicts
    if git pull --no-commit &> /dev/null; then
        echo "Merge conflicts detected. Please resolve the conflicts before pushing."
        exit 1
    fi

    # Push the commits to the remote repository
    git push
fi
