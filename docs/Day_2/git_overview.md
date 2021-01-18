# Day 2 - Overview of Git

You may use this youtube playlist to accompany the lecture notes:

<a href="https://www.youtube.com/playlist?list=PL_D88w5Aragp5062QqlgDrUkDl2-kgv79" target="_blank">Link to 
Youtube Playlist</a>

## Why should you learn Git?
Git is the de facto version control system in which most developers and companies use. Learning the basics will greatly enhance your internship / career in the future. It will also enable you to collaborate easily with other open sourced projects and even your school projects.

## Why do we need git?
Git is an open sourced version control system. It helps us organize our codebase into snapshots so that one can revert back or combine different snapshots easily. We all have done this too, just in a less efficient manner such as :

<figure>
  <img src="../imgs/git/purpose.png" width="1000"/>
</figure>

This can get confusing and is rather prone to human errors. Therefore this is where git comes in to help us organize different stages of development and bug fixes.

## Git vs Github
Git is a version control system that works without Github in which it saves a local copy of the snapshots and Github is like an online service that hosts Git repositories which can be seen like a google drive where people can freely upload their local Git repositories.

## Overview
<figure>
  <img src="../imgs/git/overview.png" width="500" />
</figure>

Git models the history and timeline of a bunch of files and folders using a series of snapshots. Each snapshot can be viewed as a state of the entire folder in which git is tracking. It contains information about every file and folder.

!!! TLDR
    Git works by taking a bunch of snapshots of the state of files. This is like saving your game progress at different checkpoints so you can track your progress or even revert back when needed.
  
## Data Model

The data model of Git might not be the most essential in getting git to work but understanding what happens under the hood will allow you to have a greater understanding. 

Git has 3 main data types:

<figure>
  <img src="../imgs/git/gitTerminology.png" width="500" />
</figure>

1. Blob
    Git terminology for Files

2. Tree
    Git terminology for Folders

3. Commits
    Git terminology for Snapshots

For each Commit, Git needs to store data on the current state of the file and more. 

Each commit has the following data:

<figure>
  <img src="../imgs/git/dataModelCommit.png" width="500" />
</figure>

1. id
    A 40 char long String that is used to identify the commit. 
    
    Eg. "cf23df2207d99a74fbe169e3eba035e633b65d94"

2. Author
    Developer name that created the commit

3. Parent
    id of the preceeding / parent commit

4. Commit Message
    Meaningful message that the developer wrote to describe the commit
    
5.  Snapshot
    The id of the tree / folder which contains files / blobs.

!!! note "Key takeaways"
    Every commit has information regarding the state of files when the commit was created. It also knows which commit preceeds it, has a message to describe the purpose of the commit and has a unique identifier (40 character long string) like "cf23df2207d99a74fbe169e3eba035e633b65d94" to identify it.

!!! note "Side note"
    With each commit being able to be identified by their id. This makes identifying them difficult as the 40 long char strings are meaningless and not useful to humans. Therefore, git uses branch names which will map a human readable String to the commit's id.

    A commit / snapshot can have a branch name that can be mapped to locate which commit the branch name refers to. This gives a commit a meaningful name instead of "cf23df2207d99a74fbe169e3eba035e633b65d94"

    **Branch names and branching will be covered later on but this should give you a glimpse as to why we need branch names.**
    
    Example as follows:
    <figure>
      <img src="../imgs/git/dataModelCommitWithBranchName.png" width="500" />
    </figure>



