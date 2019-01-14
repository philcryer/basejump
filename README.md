<div align="center" border="0"><img src="src/logo.png" alt="dotfiles"></div>

# basejump

Basejump uses [Ansible](https://www.ansible.com) to automate the deployment of my dotfiles, configs, and handly-dandy one-liners on *nix systems (Linux and macOS). I needed one command I could run to get the game going from scratch, so this script installs Ansible via Pip, then gets my preferred setups from my [philcryer/dotfiles](https://github.com/philcryer/dotfiles) project, and puts them in place so I have an identical setup on all of the hosts I work on. Easy peasy lemon squeezy.

__NOTICE__ if you don't have Ansible installed, basejump will do that first, automatically!

## requirements

* Linux (tested on Debian and Ubuntu, stand by for RHEL testing), macOS (wip, but it's coming along!)
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

Look over what's going to be done by reading `ansible/main.yml`, then run `basejump`, which will automatically install Ansible via Pip (if it's not already installed), and then setup all of applications and dot files I can't live without

```
basejump
```

Do you want to just AUTORUN this *without prompts?* using one of those `curl` methods? I always say you shouldn't do this, it's a security risk, but look, I'm not your boss, and yolo, so why the hell not?

```
curl -s -L https://raw.githubusercontent.com/philcryer/basejump/master/src/auto.sh -o /tmp/base; sh /tmp/base
```

When it's done, close your terminal session, log back in and you should be all set. YMMV, Not responsible for lost or stolen articles, this offer not valid in Tennessee. Sorry Tennessee! 

## screenshot

<div align="center" border="0"><img src="src/screenshot.png" alt="basejump in action!"><br /><font size="1">Can it really be something I wrote if there's no ascii-art? That's a retorical question, the answer is no.</font></div>

## issues

You might have them if you're not running Debian _(recommended)_ or Ubuntu. I'd like to have this tested on other distros, please let me know if you have. 

The macOS support is coming along, try it out. Oh, and in macOS if you see errors about Vim not having Lua support you can fix it by installing a "better" vim than stock via `homebrew`:

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
