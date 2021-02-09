# Github Colaborate Note

## How to create a new branch

If you get an error while running `git add .` try replacing the '.' for the file name.

    git pull
    git checkout -b <branchName>
    Make your changes
    git add .  
    git commit -m "message"
    git push -u origin <branchName>

## Merging it back to main

let Andrea know when you're done

    git checkout main
    git merge <branchName>
    git status - to check the changes
    git log - will allow you to check all the commits
    git commit -m "message"
    git push

## Other Git Command

To see what branches are on the project

    git branch

To delete a branch, use it after merging

    git branch -d <branchName>