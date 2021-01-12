# Environment Setup Guide

## Accounts

### Google Account
You will need a google account for the python lessons as we are going to use google collab.
<a href="https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjvt_qUzZbuAhWdqksFHeAaDvEQjBAwAXoECAUQAQ&url=https%3A%2F%2Faccounts.google.com%2Fsignup%3Fhl%3Den&usg=AOvVaw3FJJxI-qjWUb2bq_B0_q6t
" target="_blank">Link to create google account</a>

### Github Account
We will be going through the basics of git. Please create an account if you do not have one.
<a href="https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwik0YSwzZbuAhWZfH0KHeipAMAQFjAAegQIAxAC&url=https%3A%2F%2Fgithub.com%2Fjoin&usg=AOvVaw0H9TK-nu7JfXaoNeNMgJEk" target="_blank">Link to create github account</a>

## Python

### mac OS
Use the following link to download and follow the on screen instructions.
<a href="https://www.python.org/downloads/" target="_blank">Link to Download python for macOS</a>

!!! note "Using Homebrew"
    If you are using Homebrew, run the following command:
        `brew install python`

### Windows
Use the following link to download and follow the on screen instructions.
<a href="https://www.python.org/downloads/" target="_blank">Link to Download python for windows</a>

<a name="python/packages"></a>

### Python Packages
Open `terminal for macOS` or `windows prompt for Windows` and run the following commands:

#### jupyter notebook
`pip install notebook`
#### requests
`pip install requests`
#### beautifulsoup
`pip install beautifulsoup4`

!!! note "What's going on?"
    We are now installing packages using `pip` which is the Python Package Manager.
    Since python is an open sourced programming language, many other developers have come up with amazing tools to enhance the use of python. These tools are what we call `packages` in which we use `pip` to manage those packages.
    To download a package using pip, we use a shell to interact with the computer.
    Opening `terminal` for macOS or `command prompt` for Windows:
        We run commands that look like this: `pip install <name of package>`
    TLDR: We download other people's code to use for our own so that we don't have to code out the same thing over and over again.

!!! note "Wait what is a shell?"
    Computers you use now have graphical interface in which we press buttons to make the computer do stuff.
    However, what if we want to do more than what the buttons can do?
    That's why we have a shell, a texted based interface which we use to interact with the computer.

<a name="git"></a>

## Git

### mac OS
<a href="https://sourceforge.net/projects/git-osx-installer/" target="_blank">Link to Download Git for macOS</a>

!!! note "Using Homebrew"
    If you are using Homebrew, run the following command:
        `brew install git`

### Windows
<a href="https://git-scm.com/download/win" target="_blank">Link to Download Git for windows</a>

!!! note "To test if git is installed"
    1. macOS : Open your `Terminal` application and type the following command: `git --version`
    2. windows : Open your `git bash` application and type the following command: `git --version`