#!/bin/bash

# Change to your Git repository directory
cd /root/Scripts

# Add all changes
git add .

# Generate a random commit message
commit_message="Random commit message: $(date +%s)"
git commit -m "$commit_message"

# Pull changes from the remote repository
git pull

# Push changes to the remote repository
git push


