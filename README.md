basejump
=====

![](baseJumping.png) Basejump automates the deployment of my customized console configs on new systems. I needed one command I could run to get the game going from scratch, this script will install the needed `zsh` setup ([sbusso/zprezto](https://github.com/sbusso/zprezto)) then checkout my dotfiles repo ([philcryer/dotty](https://github.com/philcryer/dotty)) and put all of those in place so I have the identical setup on all of the hosts I work on. Easy cheesy.


## requirements

* Linux (Debian _(recommended)_ or Ubuntu - not using CentOS or RHEL currently, so 'that's not supported')
* git
* zsh
* vim-nox

Missing any of those? No problem, just:

```
sudo apt-get install git zsh vim-nox
```

* a sense of humor

Missing that? I can't help you.

## usage

run `basejump` to automatically setup all of applications and dot files *without prompts*! So, if you are not `philcryer`, you should _read the code_ (amiright Mike?) before blindy running this so you know what's going to happen.

```
./basejump
```

When it's done, close/reopen your terminal session and you should be all set. YMMV, Not responsible for lost or stolen articles, offer not valid in Tennessee. Sorry Tennessee! 

## issues?

You might have them if you're not running Debian _(recommended)_ or Ubuntu. If you are and are still having issues, let me know by opening an [issue](https://github.com/philcryer/basejump/issues) or making a [pull request](https://github.com/philcryer/basejump/pulls).

### thanks
