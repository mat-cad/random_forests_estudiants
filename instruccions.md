
# Version control

This text explains how to start doing version control for the practicum with [Git](https://git-scm.com/) and [Github](https://git-scm.com/). 

Doing version control is not compulsory but highly recommended for any *team* developing software, even for a single developer. Git combined with Github is the most widespread way to do it. So, sooner or later you will end up learning, using and maybe enjoying it, or some other version control tool.

You can play the following short videos to know more:
-  [What is version control ?](https://git-scm.com/video/what-is-version-control) 6 min.
- [What is Git ?](https://git-scm.com/video/what-is-git) 9 min.
- [Learn Git in 15 minutes](https://www.youtube.com/watch?v=USjZcfj8yxE)
- [Learn Github in 20 minutes](https://www.youtube.com/watch?v=nhNq2kIvi9s)


As a plus, with Github you can easily build a portfolio to showcase all of your projects, and reference it in your curriculum vitae. It's just a static web page hosted in Github for free. See how ito do it in [Github pages](https://pages.github.com/), and some (fancy) examples [here](https://education.github.com/pack/gallery?filter=All&sort=newest&tag=Personal+Portfolio). To begin, you can just build a simple web page in plain Html linking to your Github repos.

# Start version control for the practicum

One of the students of the team will 
1. download (not exactly, but *clone* it) an Github [existing repository](http://github.com/mat-cad/random_forests_estudiants) made by us, that is a template for the team's repository that will contain their project
2. create a new repository in his/her Github account and upload (again, the right term is *push*) this template into it
3. invite the other team members to share it

Each of the other members will *pull* this repository to have its local copy. Now all members are in sync and ready to do version control through Git commands.

First, all the students sign-up into github.com (create an account) and make sure they have Git installed in their computers.

One of the students follows these steps:

1. Sign-in to github.com and create a new repository, for instance by clicking at the ``+`` sign at upper-right corner

1. Name the repository ``random_forests`` and specify it's **private**

1. Invite his/her team mates with at least "Write" role

1. visit http://github.com/mat-cad/random_forests_estudiants to see the template you are going to download. Actually you could also download it as a zip (green button ``Code``) but then you won't be doing version control as we intend.

1. download somewhere in his/her file system, the starting files from this Github repository :

```
$ cd ~/Documents/POO/
$ git clone http://github.com/mat-cad/random_forests_estudiants
Cloning into 'random_forests_estudiants'...
warning: redirecting to https://github.com/mat-cad/random_forests_estudiants/
remote: Enumerating objects: 13, done.
remote: Counting objects: 100% (13/13), done.
remote: Compressing objects: 100% (13/13), done.
remote: Total 13 (delta 0), reused 13 (delta 0), pack-reused 0
Unpacking objects: 100% (13/13), done.
```

this will create a directory ``~/Documents/POO/random_forests_estudiants`` and populate it with the files in that repository. 

It has a .git folder, so you are already able to do control version with git *locally*. In order to work with github you need some additional steps.

6. rename to a better name for your project, the same as the repository previously created in github

```
$ mv random_forests_estudiants random_forests
```

7. now upload the cloned repo into the team's github repository

```
$ cd random_forests
$ git push http://github.com/mat-cad/random_forests master
```

9. some messages appear and you are done. You can check the status and see the number of the first version of the repository

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
