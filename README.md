<div align="center" border="0">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="ansible/files/logo.png">
    <source media="(prefers-color-scheme: light)" srcset="ansible/files/logo.png">
    <img alt="basejump logo" src="logo.png">
  </picture>
</div>

# basejump

Basejump is a bash script that runs on Linux hosts that checks if [Ansible](https://www.ansible.com) is installed, if not it will install `ansible`, along with `ansible-lint`, and then run `ansible` to automate the setup and configuration of the host. Look in the [ansible directory](https://github.com/philcryer/basejump/tree/main/ansible) at `main.yml` and the files in `tasks/` to see what it does to start.

Currently command-line setup and configuration, focusing on things like:

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

This creates a consistent base environment in Linux, regardless of the distribution. Since some current distros have an older version of `neovim` in their repositories which `lazyVim` doesn't support, basejump currently targets:

* Alpine Linux (3.23+)
* CachyOS, based on Arch Linux (any)
* Debian (forky/testing/14+)
* Fedora (42+)

Soon Ansible modules for setting up and configuring a desktop will be available.

__NOTICE__ if you don't have Ansible installed, basejump will do that first via Pip, automatically!

## requirements

* A supported version of Linux, with packages:
  * bash
  * sudo -or- doas

## usage

Checkout the code, change into the directory:

```
git clone https://github.com/philcryer/basejump.git
cd basejump
```

(optional) define your SSH and/or BECOME password in `$HOME/.ansible/become-pass`

(optional) edit `ansible/group_vars/all.yml`, uncomment the GitHub related variables, and set your git username and email variables

Look over what's going to be done by reading `ansible/tasks/main.yml`, then run `basejump`, which will automatically install Ansible if it's not already, and then hand it off to Ansible to do the syncing work.

```
./basejump
```

## license 

The MIT [License](LICENSE)

### thanks
