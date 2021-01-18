# Day 2 - Git Key Concepts (Local)

## Staging Area

Before moving to how to create a snapshot / making a commit. We need to understand the `git add` command and the staging area. `git add` is the command that places certain files into the staging area. Files in the staging area will then be placed into a snapshot / commit when the `git commit` command is run.

!!! info "Why do we need the staging area?"
    Staging area allows you to be selective in what you want git to keep track of or what to make into a commit.
    
    This allow for clean snapshots in which you as the developer can choose how to segment your newly created or edited files into seperate snapshots / commits.

!!! Tip "Commonly used git add commands:"
    - `git add <filename>` add file into staging area
    - `git add --all` add all files in all directories into staging area
    - `git add .` add all files in current directory into staging area
    - `git rm --cached <filename>` remove a file from the staging area


## Commits
`git commit` moves the files in the staging area into a snapshot / commit. This can be viewed as a milestone in your project, just like how you frequently save your word documents after every paragraph or what not.

!!! Tip "Commonly used git commit commands:"
    - `git commit -m "some descriptive commit message" ` Move files in staging area to a snapshot and include a descriptive message


## Branching
A branch is basically a pointer that allows for meaningful human readable text to describe a snapshot.

!!! info "Important to understand"
    A branch is just a pointer that maps a meaningful text to a commit's id.
    
    Example:  
    My branch named`feature/redButton` maps to a commit with an id of `cf23df2207d99a74fbe169e3eba035e633b65d94`

### main / master Branch
Everytime you inialize git, main or master is the default branch na,e. You can view this as the main line of development where the live code lives in.

### HEAD Branch
The HEAD branch is the branch in which points to the current Branch you are currently on.

### Committing on a branch
Since a branch is just a named pointer, whenever you commit on a different branch, git will create a new snapshot and then move the HEAD and the current branch forward to the new snapshot.

### Git checkout
The command `git checkout` is used to switch and create branches.
!!! Tip "Commonly used git checkout commands:"
    - `git checkout <branch name>` switches branches.
    - `git checkout -b <new branch name>` creates a new branch as per name passed in as arguement, then switches to it.


## Merging

There are 2 ways of merging branches together which are the `git merge` and `git rebase` commands.

Everytime git merges commits, there are 2 possible types of merges which are the **Fast Forward** and **Three Way Merge**.

### Fast Forward Merge
When the branch is linear (No branching out). A fast forward merge will occur. Do remember that a branch is simply a pointer to a commit, so if it is linear, there is no need to create another commit, the branch only needs to update the pointer.

Example as follows:
<figure>
    <img src="../imgs/git/merge-6.png" width="500"/>
</figure>

### Three Way Merge
When the commits are not linear, git will create another commit and merge the branches together.

Example as follows:
<figure>
    <img src="../imgs/git/merge-5.png" width="500"/>
</figure>

!!! Tip "Commonly used git merge commands:"
    - `git merge <branch name>` merge specific branch name into current branch.

### git rebase
`git rebase <branch to rebase to>` stores all the differences between the branches, then resetting the branch you are currently on to a commit preceeding the branch you are rebase-ing to. It then merges all the differences into that commit. You may then perform a `git merge` to fast-forward the branch.

Example as follows:
<figure>
    <img src="../imgs/git/git-rebase-1.png" width="500"/>
</figure>

You can view `git rebase` as git recording all the differences between `newBranch` and `main` then creating a new commit, then reapplying the differences into the new commit.

<figure>
    <img src="../imgs/git/git-rebase-2.png" width="500"/>
</figure>

A `git merge main` will then do a fast-forward merge. Take note that as previously mentioned, a branch is simply a pointer so a fast forward merge just redefines that the `main` branch is pointing at.


## Merge Conflicts
When merging 2 or more branches, git will do auto merging, however when it comes across something it is unsure of, it will trigger a merge conflict. An example of such a conflict is as shown:

<figure>
    <img src="../imgs/git/mergeConflictDiag.png" width="500"/>
</figure>

You will see weird seperators on the merge conflict. The following image explains what they are and what they mean:

<figure>
    <img src="../imgs/git/mergeConflictExpl.png" width="500"/>
</figure>

## git utilities
Some useful git commands as listed:


### git status

`git status` shows you the current state of your working directory in respect to your current branch.


### git log

You will frequently use `git log --all --graph --decorate` to print out a diagram of the timeline of your commits. This is useful in visualizing your commits and where your branches are pointing at.


### git diff

`git diff <filename>` shows the changes you made in relation to the current snapshot of the file.

`git diff <branch name> <filename>` shows the differences as compared to a sepcific file in the specified branch.



