
# Version control

This text explains how to start doing version control for the practicum with [Git](https://git-scm.com/) and [Github](https://git-scm.com/). 

Doing version control (VC) is not compulsory but highly recommended for any *team* developing software, and even for a developer working in isolation. Git combined with Github is the most widespread way to do *distributed* VC. Distributed means to share a project files with other programmers which change them simultaneously, the normal way to develop software. So, sooner or later you will end up learning, using and maybe enjoying Git + Github, or some other version control tool and platform.

Play the following short videos to know more:
-  [What is version control ?](https://git-scm.com/video/what-is-version-control) 6 min.
- [What is Git ?](https://git-scm.com/video/what-is-git) 9 min.
- [Learn Git in 15 minutes](https://www.youtube.com/watch?v=USjZcfj8yxE)
- [Learn Github in 20 minutes](https://www.youtube.com/watch?v=nhNq2kIvi9s)


As a plus, you can easily build a portfolio to showcase your projects, and reference it in your curriculum vitae. It's just a static web page hosted in Github for free. See how ito do it in [Github pages](https://pages.github.com/), and some (fancy) examples [here](https://education.github.com/pack/gallery?filter=All&sort=newest&tag=Personal+Portfolio). To begin, you can just build a simple web page in plain Html linking to your Github repos.

# Start version control for the practicum

First, all the students sign-up into github.com (create an account) and make sure they have Git installed in their computers.

One of the students of the team will copy (*fork* in Github words) a Github [existing repository](http://github.com/mat-cad/random_forests_estudiants) made by us to his/her Github account. It is a template for the practicum repository. Once done, this student invites the other team members to share it.

Each member *clones* this repository to have his/her own local copy in the computer. Now all members are in sync and ready to do version control through Git commands. 

Now, in detail:


One of the students, with Github user ``pere-grau`` for example, follows these steps:

1. Sign-in (login) to github.com and fork repository http://github.com/mat-cad/random_forests_estudiants

1. Go to Settings, rename the repository to ``random_forests`` and specify it's **private**

1. Go to Settings -> Collaborators and invite the team mates with at least "Write" role

Now each team member downloads the repository files somewhere in the file system, in such a way that the directory where they are copied is subject to version control and becomes connected to the Github repository. This is *cloning* the repository:

```
$ cd ~/Documents/POO/
$ git clone http://github.com/pere-grau/random_forests
Cloning into 'random_forests'...
warning: redirecting to https://github.com/mat-pere-grau/random_forests/
remote: Enumerating objects: 13, done.
remote: Counting objects: 100% (13/13), done.
remote: Compressing objects: 100% (13/13), done.
remote: Total 13 (delta 0), reused 13 (delta 0), pack-reused 0
Unpacking objects: 100% (13/13), done.
```

this will create a directory ``~/Documents/POO/random_forests`` and populate it with the files in the Github repository. 

It has a ``.git`` folder, so you are already able to do control version with git *locally*. In order to work with Github you need some additional steps.


You can check the status and see the number of the first version of the repository

```
$ git status
On branch master
nothing to commit, working tree clean
$ git log
commit fe65474cd25c411b244a4d44f6c01675695e123a (HEAD -> master)
Author: joan-s <joans@cvc.uab.es>
Date:   Fri Jan 22 14:28:08 2021 +0100

    initial commit
```