# Day 2 - Overview of Git

You may use this youtube playlist to accompany the lecture notes:

<a href="https://www.youtube.com/playlist?list=PL_D88w5Aragp5062QqlgDrUkDl2-kgv79" target="_blank">Link to 
Youtube Playlist</a>

Lecture Notes:
<a href="Day_2/git_lecture.pdf" download="git_workshop_slides.pdf" target="_blank">Download lecture pdf file</a>

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

## How git works?
<figure>
  <img src="../imgs/git/overview.png" width="500" />
</figure>

Git models the history and timeline of a bunch of files and folders using a series of snapshots. Each snapshot can be viewed as a state of the entire folder in which git is tracking. It contains information about every file and folder.

!!! TLDR
    Git works by taking a bunch of snapshots of the state of files. This is like saving your game progress at different checkpoints so you can track your progress or even revert back when needed.
