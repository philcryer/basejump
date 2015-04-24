basejump
=====

![](baseJumping.png) Basejump automates my deploying my customized console config on new systems. I needed one command I could run to get the game going on new hosts that I administrate. This script will install the needed `zsh` setup ([sbusso/zprezto](https://github.com/sbusso/zprezto) then checkouts my dotfiles repo ([philcryer/dotty](https://github.com/philcryer/dotty)) and put all of those config files in place so I have the same setup on all of the hosts I work on. Easy cheesy.


## requirements

* Linux (Debian (recommended) or Ubuntu, I'm not using CentOS or RHEL currently, so 'that's not supported')
* git
* zsh
* vim-nox

```
sudo apt-get install git zsh vim-nox
```

* a sense of humor

## usage

run `basejump` to automatically setup all of the dot files w/o prompts. (note, if you are not `philcryer`, you should _read the code_ (amiright Mike?) before blindy running this so you konw what's going to happen)

```
./basejump
```

When it's done, close/reopen your terminal session and you should be all set

## issues?

YMMV if you're not running Debian (recommended) or Ubuntu.

### thanks
