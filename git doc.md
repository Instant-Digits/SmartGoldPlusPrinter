git --version

    git --config --global user.name "shaganan"
    git --config --global user.email "shaganan@gmail.com"
    git --config --list


initialize a respository

    git init
    git status

    git add -A    (Staging area)
    git reset     (remove from staging area)

    git commit -m "something"  (clean staging area)
    git log 

    git remote add origin master  https://github.com/ShagananThiru/tempforgabilan.git
    git push -u origin master

remote repositories

    git clone http//

to check the remote repositories

     git remote -v

list all of the branches localy + remotely

    git branch -a

to show the changes

    git diff

to check the status/edited one 

    git status

to adding to staging  area

    git add -A 
    git commit -m "something"

to push to remote repositories

    git pull origin master /particular branch- some one clould change it
    git push origin master


to create a new branch

    git branch name
    git branch -a

to get into that branch

    git chechout name

follow add commit pull push for the branch

to push the new branch to remote repositories

    git push -u origin name   first tinme only need he -u
     git branch -a

to merge the new branch with master

    git checkout master
    git pull origin master
    git branch --merged  to check what brances are merged
    git merge name    this is merge cmd
    git push orgin master

to delete the branch

    git branch --merged  to check what brances are merged
    git branch -d name    delete localy
    git branch -a
    git push origin --delete name delete from remote repositories


to ignore from git 
    touch .gitignore