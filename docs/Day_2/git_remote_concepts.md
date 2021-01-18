# Day 2 - Working with github concepts

## Remote

Git works locally on our computer, but what if we want to collaborate with other developers and would like to share the git folder. For this, we use github which hosts git folders.

To link a git folder to a remote git repository, we use `git remote add <name of remote> <url link of remote git repo>`. This can be seen as syncing your git folder with a remote computer that contains the same git repo.

### push / pull / fetch

In order to send updates to the remote repo, we use 
`git push <remote repo name> <branch name>`

In order to get updates from the remote repo, we use 
`git pull <remote repo name> <branch name>`

Another way of getting updates from the remote repo, we also can use 
`git fetch <remote repo name> <branch name>`

The differences between `git pull` and `git fetch`, is that `git pull` automatically merges the changes into your local directory while `git fetch` gets all the changes and stores in in another commit in a branch named `FETCH_HEAD ` in which you can later combine using `git merge FETCH_HEAD`. 

Therefore `git pull` actually calls `git fetch` and `git merge FETCH_HEAD` automatically.

<a name="github/clone"></a>
### clone

To download repositories on github as a git repo, we use `git clone <repo url>`.
A url can be accessed as follows:

<figure>
    <img src="../imgs/git/clone.png" width="500"/>
</figure>

Running `git clone <repo url>` will download the entire repo as a git repo instead of just a zip folder.

### Licenses
Once your work is made public, it must have a license as all creative work are eligible for intellectual property and copyright protection. A license.txt file in the base directory tells people how and what they are able to do with your work.

For speicific cases, please refer to this <a href="https://choosealicense.com" target="_blank">link to choose a license</a>.

Otherwise, the `MIT license` is the most common as it allows anyone to do anything with your work.

!!! info "If unsure"
    Always just refer to <a href="https://choosealicense.com" target="_blank">link to choose a license</a> as it lists out each case with specific details.