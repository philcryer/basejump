<div align="center" border="0">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="ansible/files/logo.png">
    <source media="(prefers-color-scheme: light)" srcset="ansible/files/logo.png">
    <img alt="basejump logo" src="logo.png">
  </picture>
</div>

# basejump

Basejump is a shell script that runs on a new Linux host, it will check if [Ansible](https://www.ansible.com) is installed, if not it will install `ansible` and `ansible-lint, and then hand it off to ansible to automate the setup of a new Linux host. Look in the [ansible directory](https://github.com/philcryer/basejump/tree/main/ansible) to see what it does to start, by default it only deals with command-line setup, focusing on things like:

* ssh
  * user configuration (~/.ssh/config`)
* git
  * install
  * configuration (~/.git_config)
* neovim
  * install
  * configuration (~/.config/nvim)
* user profile
  * configuration (~/.profile)

This creates a consistent base environment in Linux, regardless of which distribution is running, currently targeting:

* Alpine Linux
* CachyOS (based on Arch Linux)
* Debian
* Fedora

Soon Ansible modules for setting up and configuring a desktop will be available.

__NOTICE__ if you don't have Ansible installed, basejump will do that first via Pip, automatically!

## requirements

* Linux, with packages:
  * wget
  * sudo -or- doas

## optional

* Define your BECOME password in `$HOME/.ansible/become-pass
## usage

Checkout the code, change into the directory:

```
git clone https://github.com/philcryer/basejump.git
cd basejump
```

Edit `ansible/group_vars/all.yml` and set your git username and email variables

Look over what's going to be done by reading `ansible/tasks/main.yml`, then run `basejump`, which will automatically install Ansible if it's not already, and then hand it off to Ansible to do the syncing work.

```
basejump
```

Do you want to just AUTORUN this *without prompts?* I always say you shouldn't do this, it's a security risk, but look, I'm not your boss, and yolo, so why the hell not?

```
```
sh -c "$(wget -qO- https://raw.githubusercontent.com/philcryer/basejump/refs/heads/main/basejump.sh)"
```

When it's done, close your terminal session, log back in and you should be all set. YMMV, Not responsible for lost or stolen articles, this offer not valid in Tennessee. Sorry Tennessee! 

## license 

The MIT [License](LICENSE)

### thanks
