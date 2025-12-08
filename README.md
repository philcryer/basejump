<div align="center" border="0"><img src="src/logo.png" alt="dotfiles"></div>

# basejump

Basejump uses [Ansible](https://www.ansible.com) to automate the setup of new hosts with applications, dotfiles, configs, and handly-dandy one-liners on Linux and macOS systems. I needed one command I could run to get the game going from scratch, so this script installs Ansible via Pip, then gets my preferred setups from my [philcryer/dotfiles](https://github.com/philcryer/dotfiles) project, and puts them in place so I have an identical setup on all of the hosts I work on. Easy peasy lemon squeezy.

Some of installed software (see full list for [Linux](/ansible/group_vars/linux.yml) and [macOS](/ansible/group_vars/darwin.yml#L15) and add/remove what you want)  

* networking tools: nc, iperf, nmap
* monitoring: htop
* applications: nginx, vlc
* development: [SpaceVim](https://spacevim.org/), font-hack-nerd-font, VS Code (macOS), iTerm 2 (macOS)

__NOTICE__ if you don't have Ansible installed, basejump will do that first via Pip, automatically!

## requirements

* Linux or macOS (10.12+)
* python
* pip
* git
* sudo

## usage

Checkout the code, change into the directory:

```
git clone https://github.com/philcryer/basejump.git
cd basejump
```

Edit `ansible/group_vars/all.yml` and set your git username and email variables

Look over what's going to be done by reading `ansible/tasks/main.yml`, then run `basejump`, which will automatically install Ansible if it's not already installed, via Pip, and then setup all of applications and dot files I can't live without

```
basejump
```

Do you want to just AUTORUN this *without prompts?* using one of those `curl` methods? I always say you shouldn't do this, it's a security risk, but look, I'm not your boss, and yolo, so why the hell not?

```
curl -s -L https://raw.githubusercontent.com/philcryer/basejump/master/src/auto.sh -O; chmod 755 auto.sh; ./auto.sh
```

or via wget

```
sh -c "$(wget -qO- https://raw.githubusercontent.com/philcryer/basejump/refs/heads/main/basejump)"
```

When it's done, close your terminal session, log back in and you should be all set. YMMV, Not responsible for lost or stolen articles, this offer not valid in Tennessee. Sorry Tennessee! 

## screenshot

<div align="center" border="0"><img src="src/screenshot.png" alt="basejump in action!"><br /><font size="1">Can it really be something I wrote if there's no ascii-art? That's a retorical question, the answer is no.</font></div>

## issues

* Linux: if you're not running Debian/GNU Linux _(recommended)_ or Ubuntu Linux, reach out, I'd like this tested on more Linux distros.

* macOS: if you see errors about Vim not having Lua support you can fix it by installing a "better" vim than stock via `homebrew`:

```
brew install macvim --with-cscope --with-lua --override-system-vim
sudo brew linkapps
```

If you are and are having other issues or have suggestions, let me know by opening an [issue](https://github.com/philcryer/basejump/issues) or making a [pull request](https://github.com/philcryer/basejump/pulls).

## license 

The MIT License (MIT)

Copyright (c) 2019 philcryer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

### thanks
