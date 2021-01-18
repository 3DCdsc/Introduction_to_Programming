# Day 2 - Git Examples

<a name="Examples using commands"></a>
## Examples using commands we have learnt
To better illustrate how you could visualise basic git commands. We will be going through the 2 ways of merging but starting from scratch.

<figure>
    <img src="../imgs/git/merge-1.png" width="500"/>
</figure>

1. On our first commit, 1 snapshot in which the default branches `main / master` and `HEAD` points to. Take note `main / master` is a default branch created and `HEAD` is a pointer to show which branch you are currently on.

2. We then use `git checkout -b "newBranch" ` to create a new branch named "newBranch" and also move the `HEAD` pointer to that newly created branch. Do note that a branch is just a pointer to a commit, so creating a new branch just creates another pointer to the current commit you are on.

<figure>
    <img src="../imgs/git/merge-2.png" width="500"/>
</figure>
3. After making some changes, we need to use `git add .` to add all modified file from my current directory into the staging area. This is to tell git that the added files are to be tracked. After adding files we want to commit to the staging area, we use `git commit -m "1st change"`. This tells git to create a snapshot and store a meaningful commit message named "1st change". Git will then create the commit and then move the pointers `newBranch` and `HEAD` to the new commit you just created.

<figure>
    <img src="../imgs/git/merge-3.png" width="500"/>
</figure>
4.  Now to go back to the main branch, we use `git checkout main` to switch the HEAD pointer to the main branch.

<figure>
    <img src="../imgs/git/merge-4.png" width="500"/>
</figure>
5. Now that we are on the main branch, we make more changes and do the same as previously mentioned to add modified files to the staging area then commit them with a meaningful message.

<figure>
    <img src="../imgs/git/merge-5.png" width="500"/>
</figure>
6. Now we have 2 branches with 2 different feature sets / changes. We want to merge them together. Now we run `git merge newBranch` to merge newBranch to the current branch HEAD is on which is main in this case. Git will then do a Three-way merge since there is no linear path of commits.

<figure>
    <img src="../imgs/git/merge-6.png" width="500"/>
</figure>
7. To illustrate a fast forward commit, refer to the left of the image for an example of a linear path of commits. You will realise that newBranch2 is simply some form of modification of the main branch. Therefore, git does not need to create another snapshot like what it did previously, but it only needs to update the main pointer to point to the commit in which newBranch2 points to.

