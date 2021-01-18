# Day 2 - Working with github concepts

## Remote

Git works locally on our computer, but what if we want to collaborate with other developers and would like to share the git folder. For this, we use github which hosts git folders.

To link a git folder to a remote git repository, we use `git remote add <name of remote> <url link of remote git repo>`. This can be seen as syncing your git folder with a remote computer that contains the same git repo.

## Push / Pull / Fetch

In order to send updates to the remote repo, we use 
`git push <remote repo name> <branch name>`

In order to get updates from the remote repo, we use 
`git pull <remote repo name> <branch name>`

Another way of getting updates from the remote repo, we also can use 
`git fetch <remote repo name> <branch name>`

!!! info "git pull vs git fetch"
    The differences between `git pull` and `git fetch`, is that `git pull` automatically merges the changes into your local directory while `git fetch` gets all the changes and stores in in another commit in a branch named `FETCH_HEAD ` in which you can later combine using `git merge FETCH_HEAD`. 

    Therefore `git pull` actually calls `git fetch` and `git merge FETCH_HEAD` automatically.

<figure>
  <img src="../imgs/git/fetch-pull.png" width="500"/>
</figure>

## Clone

To download repositories on github as a git repo, we use `git clone <repo url>`.
A url can be accessed as follows:

<figure>
    <img src="../imgs/git/clone.png" width="500"/>
</figure>

Running `git clone <repo url>` will download the entire repo as a git repo instead of just a zip folder.


## gitignore
If we have files that we want git to always ignore and not track them, we use a `.gitignore` file to list down specific files.

!!! info "Why does the file name have a dot infront?"
    File with a `.` infront are called `dotfiles`. They are hidden files are hidden from the OS and even the `ls` command doesn't show it. In fact, we need to use `ls -a` in which the `-a` flag tells the command to include hidden files or "all" files.

    dotfiles are generally used for config files such as gitignore in this case.

`.gitignore` uses a globbing patterns to match file names.

Commonly used pattern are such as:

- `**/folderName` : every file that have a parent directory named `folderName` such as folderName/apiKeys , secret/folderName/apiKeys
- `*.log` : Any file that has `.log` in it such as apiKeys.log

!!! note ""
    No need to memorise such patterns. Google is always your bestfriend.

<a href="https://www.atlassian.com/git/tutorials/saving-changes/gitignore#git-ignore-patterns" target="_blank">Link to more information on gitignore patterns</a>

## Licenses
Once your work is made public, it must have a license as all creative work are eligible for intellectual property and copyright protection. A license.txt file in the base directory tells people how and what they are able to do with your work.

For speicific cases, please refer to this <a href="https://choosealicense.com" target="_blank">link to choose a license</a>.

Otherwise, the `MIT license` is the most common as it allows anyone to do anything with your work.

!!! info "If unsure"
    Always just refer to <a href="https://choosealicense.com" target="_blank">link to choose a license</a> as it lists out each case with specific details.