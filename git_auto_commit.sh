#!/bin/bash

# Define the path to the file
file_path="/root/Scripts/random.txt"

# Generate a random string
random_text=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | head -c 50)

# Add a timestamp
timestamp=$(date "+%Y-%m-%d %H:%M:%S")
content="$timestamp - $random_text"

# Append the random text to the file
echo "$content" >> "$file_path"

# Display a message
echo "Random text added to $file_path:"
echo "$content"

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


