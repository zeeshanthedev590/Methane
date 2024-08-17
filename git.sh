#!/bin/bash

# Add all changes to the staging area
git add .

# Prompt for the commit message
read -p "Enter commit message: " COMMIT_MESSAGE

# Commit the changes with the provided message
git commit -m "$COMMIT_MESSAGE"

# Ask if the user wants to push the changes
read -p "Do you want to push the changes to the remote repository? (y/n): " PUSH_CONFIRM

# Check user response
if [ "$PUSH_CONFIRM" == "y" ] || [ "$PUSH_CONFIRM" == "Y" ]; then
    # Push changes to the main branch (or specify your branch)
    git push origin main
    echo "Changes have been pushed to the remote repository."
else
    echo "Changes were committed but not pushed."
fi
