# Home Assignments Submission Guide

Most home assignments in OpsSchool are submitted to Github using git.

In order to submit the home assignments, a specific submission flow must be used.

## About the home assignments flow

In OpsSchool, we use the standard [Pull request code reviews](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/about-pull-request-reviews) flow used by most cutting edge hi-tech companies.

This flow requires specific git knowledge and expertise. 

## Guide - How to submit a home assignment?
**Use the below steps in order to submit home assignments via Github using git**

### Do you know git? Sure?
Go over the 2 sessions of the OpsSchool git workshop - make sure you understand and able to perform all activities discussed in this workshop
> The git workshop is a hands-on workshop. We highly recommend you actively run the hands on content in the sessions instead of just being a passive viewer

1. [Source control introduction and git local](https://www.youtube.com/watch?v=0K7H1IZYBbY&feature=youtu.be) (use [this link](https://www.youtube.com/watch?v=0K7H1IZYBbY&feature=youtu.be&t=1017) to skip ⏭️ the source control introduction)
1. [git remote](https://youtu.be/9oQbt5YQgP4)


### The Pull request review flow explained
The steps below will be used to submit home assignments in OpsSchool in order of precedence. 

As there are steps that should be taken continously (as you make more changes and more home assignments) use the legend below to understand when each step should be used:

* 🔂 Step that should be taken once during the course
* 🔁 Step that shoukd be taken on each new home assignment/project/feature added.
* 🔁🔁🔁 Step that should be taken continously for EVERY chnage you make


### The flow

* [Setup 🔂](#initial-setup)
* [Add collaborators 🔂](#add-collaborators)
* [Before starting a new change 🔁](#before-starting-a-new-change)
* [Local + remote flow 🔁🔁🔁](#basic-local--remote-flow)
* [Pull request 🔁](#how-to-open-a-pull-request)
* [Making changes 🔁🔁🔁](#making-changes)
* [Merge! 🔁](#merge)


#### Initial setup
1. Make sure you have git installed. In your terminal, run:
    ```$sh
    $ git --version
    ```
   > Any version >2.22 will be good enough
1. Make sure your git configuration is set:
    ```sh
    $ git config --global user.name "YOUR_NAME_OR_GITHUB_USER"
    $ git config --global user.email "YOUR_EMAIL_ON_GITHUB"

    ```
    > **IMPORTANT NOTE:** The `--global` flag means this would be your git configuration in EVERY git repository you will work on in this PC. \
    > If you are using addtional git user on your PC (work related for example) you can use `git config --local` on a specific repository to have thiד configuration only apply to it and not the entire PC.
1. Go to Github.com, Fork the repository your are aksed to submit homework to. once forked, the new repo will appear under your user. [Read here](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo) for more information on forking a repo on Github.
1. Clone the new repo to your pc

#### Add collaborators
In order for another user to review your code, the user must first be added as a collaborator in your personal repo.
1. On your personal repo page on Github.com click `:gear: settings` --> `Manage access`
1. Click on  `Invite a collaborator`
1. Find each of the users of your fellow student reviewer & instructor reviewer and add them as collaborators

#### Before starting a new change
1. Make sure your master branch is up to date:
    ```shell script
    # Option #1
    $ git checkout master
    $ git pull origin master
   
    #Option #2 
    $ git checkout master
    $ git fetch
    $ git rebase origin/master
    ```
1. Create a new branch from master (use hyphens *(-)* to separate words):
    ```
   $ git checkout -b mickey-home-assignment-3
   ```
   
> :repeat: Remember: this flow should be repeated for each home assignment/project/feature you wish to submit.
   
#### Basic local + remote flow

> :warning: **Always make sure the following:** 
> * You are checked out on the right branch. use the `git branch` command. The checked out branch (the one HEAD points to) will be marked in an asterisk *(*)*
> * Your branch is up to date. No further changes are on the remote branch. try running `git pull` to see if you can merge any changes in order to avoid future conflicts.


1. Code! Make changes, add files, write your best solution possible!
1. Ready to have your code reviewed? first run `git status` and use `git add` to select only the files that are relevant for this assignment
1. Run `git commit` command with the `-m` flag and provide a MEANINGFUL description of your change
    ```$sh
    $ git commit -m "Full running solution for coidng home assignment #3"
    ```
      > If you're not sure whether you commit was ok use the `git log` &  `git show` commands to take a closer look at your commits
1. Run `git push` command to push your specific branch to origin
    > 🛑 **Never push to master branch. this just bad practice overall**
    ```$sh
    $ git push origin mickey-home-assignment-3
    ```
1. Yay! now go to Github.com and view your forked Github repo.

#### How to open a Pull request?
Now let's open a Pull request and assign it to your reviewer.
> Usually a typical pull request would be **from** your newly created branch (where you just made changes) **to** your master branch
 
1. On your main repository page, select your branch from the branch menu.
1. Once branch select, click the "pull request" button.
1. On the right pane you select your branch and on the left pane you select your personal repo master branch. 
   > The selected "base repository" will always be *<your-user>/<repo-name>* as we will not merge to the base repo (the one you forked from) in this course.
1. Under "Reviewers" in the right menu, you should put your reviewer username (user must first accept your invitation to collaborate otherwise the user won't appear for selection)
1. Now click "Create pull request". the reviewer would be informed (usually by mail) that he needs to review this Pull request and you will be able to collaborate using comments.


#### Making additional changes
As in many code reviews, you may need to change or adjust your code per the reviewer's comments. this can be easily done simply by making your changes and pushing to your branch as described in [Basic local + remote flow]((#basic-local--remote-flow)) section.

> Don't worry - you do not need to update the Pull request nor open a new one. Once your changes are pushed it will be imiidiately be reflected in the opened Pull request. It is worth thouh to update your reviewer on your changes by mentioning him/her (e.g. `@reviewer_user`) in the Pull request comments.

#### Merge!
Is the code Code review done and approved by the instructor?
1. When you have made all the necessary changes and code review was done your instructor will "Approve" the Pull request.
2. You wll then be able to click on the "Merge pull request" button which will merge your code into your personal repo master branch.

**And that's it :checkered_flag:**
