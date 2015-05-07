basejump
=====
![](basejump.png)

Basejump automates the deployment of my customized console configs on new systems. I needed one command I could run to get the game going from scratch, so this script installs my preferred `zsh` setup ([sbusso/zprezto](https://github.com/sbusso/zprezto)) then checks out my dotfiles repo ([philcryer/dotty](https://github.com/philcryer/dotty))i and puts them in place so I have an identical setup on all of the hosts I work on. Easy peasy lemon squeezy.

## requirements

* Linux (Debian or Ubuntu. Using something else? "that's not supported")
* git
* rsync
* vim-nox
* zsh

Missing any of those? No problem, just:

```
sudo apt-get install git rsync vim-nox zsh
```

* a sense of humor

Missing that? I can't help you.

## usage

Run `basejump` to automatically setup all of applications and dot files *without prompts*! So, if you are not `philcryer`, you should _read the code_ (amiright Mike?) before blindy running this so you know what's going to happen.

```
./basejump
```

Do you want to just AUTORUN this without prompts? Of course you do!

``
git clone https://github.com/philcryer/basejump.git && cd basejump && source basejump -f
``

When it's done, it will close your terminal session, log back in and you should be all set. YMMV, Not responsible for lost or stolen articles, this offer not valid in Tennessee. Sorry Tennessee! 

## issues?

You might have them if you're not running Debian _(recommended)_ or Ubuntu. Using OSX? I told you that was "not supported", but if you see errors about Vim not having Lua support you can fix it by installing a "better" vim than stock with `homebrew`:

```
brew install macvim --with-cscope --with-lua --override-system-vim
(sudo) brew linkapps
```

If you are and are still having issues, let me know by opening an [issue](https://github.com/philcryer/basejump/issues) or making a [pull request](https://github.com/philcryer/basejump/pulls).

### thanks
