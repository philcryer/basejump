<div align="center" border="0">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="imgs/logo.png">
    <source media="(prefers-color-scheme: light)" srcset="imgs/logo.png">
    <img alt="basejump logo" src="imgs/logo.png">
  </picture>
</div>

# basejump

Basejump is a bash script that runs on Linux hosts that checks if [Ansible](https://www.ansible.com) is installed, if not it will install `ansible`, along with `ansible-lint`, and then run `ansible` to automate the setup and configuration of the host. Look in the [ansible directory](https://github.com/philcryer/basejump/tree/main/ansible) at `main.yml` and the files in `tasks/` to see what it does to start.

## what does it do?

Once run, `basejump` checks for, and then installs if they'er not present: `ansible` and `ansible-lint`, then `ansible` takes over and runs the following:

* [ansible/main.yml](https://github.com/philcryer/basejump/blob/main/ansible/main.yml)
  * Install base packages, generic across all Linuxes ([see packages_installed](https://github.com/philcryer/basejump/blob/main/ansible/group_vars/all.yml)) 
  * Install base packages, specifically for Alpine Linux ([see packages_installed_alpine](https://github.com/philcryer/basejump/blob/main/ansible/group_vars/all.yml)) 
  * Install base packages, specifically for Arch Linux ([see packages_installed_arch](https://github.com/philcryer/basejump/blob/main/ansible/group_vars/all.yml)) 
  * Install base packages, specifically for GNU/Debian Linux ([see packages_installed_debian](https://github.com/philcryer/basejump/blob/main/ansible/group_vars/all.yml)) 
  * Install base packages, specifically for Fedora Linux ([see packages_installed_fedora](https://github.com/philcryer/basejump/blob/main/ansible/group_vars/all.yml)) 
  * This then calls the specific `tasks`

* [tasks/](https://github.com/philcryer/basejump/tree/main/ansible/tasks)
  * [user.yml](https://github.com/philcryer/basejump/blob/main/ansible/tasks/user.yml) - setup the base user with the same groups and configuration, while varying details for different distros via
  * [base-config.yml](https://github.com/philcryer/basejump/blob/main/ansible/tasks/base-config.yml) - handles the setup of user specific dotfiles and configurations:
    * gitconfig: install configuration file [.gitconfig](https://github.com/philcryer/basejump/blob/main/ansible/templates/gitconfig.j2) TIP - define `gitconfig_email` and `gitconfig_name` in group_vars/all.yml, then uncomment the two lines in this file to have it automatically populate  
    * profile: install `.profile` to user's home directory to define new `$PATH`
    * fish functions: define functions for the `fish` shell, mainly to use `neovim` in place of `vi`, `vim`, and even `nvim`
  * [neovim.yml](https://github.com/philcryer/basejump/blob/main/ansible/tasks/neovim.yml) - install and configuration via `.config/nvim` using LazyVim goodness
  * [lazyvim.yml](https://github.com/philcryer/basejump/blob/main/ansible/tasks/user.yml) - install and configure [LazyVim](https://www.lazyvim.org/) for neovim to have a great base to start with
  * Nerd Font: install the [Fira Code](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/FiraCode) font from [Nerd Fonts](https://www.nerdfonts.com), then update the system's font cache so it's usable with Starship
  * Starship: install and configure [Starship](https://starship.rs), my favorite shell prompt

This creates a consistent base environment in Linux, regardless of the distribution. 

## what does it support?

NOTE: Since some current distros have an older version of `neovim` (0.11.2 and prior) in their repositories which `lazyVim` doesn't support, basejump currently targets:

* Alpine Linux (3.23+)
* CachyOS, based on Arch Linux (any)
* Debian (forky/testing/14+)
* Fedora (42+)

![](logo_alpine.png) ![](logo_arch.png) ![](logo_debian.png) ![](logo_fedora.png)

Soon I want to add more Ansible logic for setting up and configuring a desktop environment, as my current [Hyprland](https://github.com/hyprwm/Hyprland) desktop manager's configs are very many and customized, not something I want to do over, and over, again across multiple hosts!

## requirements

To run `basejump` you only need a supported version of Linux, with only minimal packages required:
  * bash
  * sudo -or- [doas](https://en.wikipedia.org/wiki/Doas), which stands for "dedicated openbsd application subexecutor, but like anything developed by the [OpenBSD](https://openbsd.org) team it's minimal, secure and preferred over the bloated sudo, which I rarely see anyone using fully anyway. Look sudo is useful, it can do a ton, but 99% of the time it's a blanket "use sudo, it's setup with NOPASSWD" which hardly seems smart.

## usage

Checkout the code, change into the directory:

```shell
git clone https://github.com/philcryer/basejump.git
cd basejump
```

(optional) define your SSH and/or BECOME password in `$HOME/.ansible/become-pass`

(optional) edit `ansible/group_vars/all.yml`, uncomment the GitHub related variables, and set your git username and email variables

Look over what's going to be done by reading `ansible/tasks/main.yml`, then run `basejump`, which will automatically install Ansible if it's not already, and then hand it off to Ansible to do the syncing work.

```shell
./basejump
```

## action!

Check out the action! See the useless ascii art header! See how I've evolved over the years to (try) and make bash script output more palatable! Marvel at the multiple Linux distros supported out of the box! (Pull requests welcome ) 

<div align="center" border="0">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="imgs/screenshot.png">
    <source media="(prefers-color-scheme: light)" srcset="imgs/screenshot.png">
    <img alt="basejump script" src="imgs/screenshot.png">
  </picture>
</div>

## license 

The MIT [License](LICENSE)

### thanks
