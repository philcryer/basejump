#!/usr/bin/env sh

#===============================================================================
# basejump -- a script that installs Ansible, then uses it to automate the setup
#   hosts playbooks from the ansible/requirements.txt file 
#
# Source:  https://github.com/philcryer/basejump
# Author: philcryer < phil at philcryer dot com >
# License: MIT
#=============================================================================

set -e
os=$(uname)
distro=$(cat /etc/os-release | grep ^ID= | cut -d= -f2)

function msg_status () {
    echo -e "\x1B[01;34m[*]\x1B[0m $1" 
}
function msg_good () { 
    echo -e "\x1B[01;32m[*]\x1B[0m $1" 
}
function msg_error () { 
    echo -e "\x1B[01;31m[*]\x1B[0m $1" 
}
function msg_notification () { 
    echo -e "\x1B[01;33m[*]\x1B[0m $1"
}

kick-off(){
  clear
  echo "|     |     |     |     |     |     |     |"	
  echo " |     |     |     |     |     |     |     |"
  echo "  |     |     |     |     |     |     |     |"
  echo "   B     A     S     E     J     U     M     P"
	echo; msg_status "ohai, let's basejump!"
}

become-check(){
    msg_notification "checking for become scheme (sudo or doas)"
    if type sudo > /dev/null 2>&1; then
        become_scheme=sudo
    fi
    if type doas > /dev/null 2>&1; then
        become_scheme=doas
    fi
    msg_good "found $become_scheme, will use it for become scheme"
}

os-check(){
    msg_notification "checking operating system"
        if [ "$distro" == "alpine" ]; then
            msg_good "$os ($distro) is supported, continuing"
        #fi
        elif [ "$distro" == "cachyos" ]; then
            msg_good "$os ($distro) is supported, continuing"
        else
            msg_good "$os ($distro) is NOT supported. Exiting"; exit 1
        fi
}

ansible-install(){
    msg_notification "checking if ansible and ansible-lint is installed"
    for cli in ansible ansible-lint; do
      if ! type "$cli" > /dev/null 2>&1; then
        msg_notification "installing Ansible on ${distro} via ${become_scheme}"
        if [ "$distro" == "alpine" ]; then
          $become_scheme apk --no-interactive update
          $become_scheme apk add --no-interactive git curl ansible ansible-lint
        fi
        if [ "$distro" == "cachyos" ]; then
          $become_scheme pacman -Sy --noconfirm git curl ansible ansible-lint
        fi
	    fi
    done
    msg_good "ansible installed"
}

run-ansible(){
    msg_status "handing off to ansible"
    cd ansible
    ansible-galaxy install -r requirements.yml
    ansible-playbook main.yml -i inventory
}

main(){
    kick-off;
    become-check;
    os-check;
    ansible-install;
    #run-ansible;
}

main;

exit 0

#OLD
neovim-install(){
    msg_notification "installing and configuring"
    if [ "$distro" == "alpine" ]; then
      $become_scheme  apk add neovim tree-sitter-lua hunspell hunspell-en-us 
    fi
    if [ "$distro" == "cachyos" ]; then
      $become_scheme pacman -Sy --noconfirm neovim tree-sitter-lua hunspell hunspell-en_us 
    fi
    mkdir -p $HOME/.config 
    #cp -R config/nvim $HOME/.config/
}


# old
      #msg_notification "installing zsh and supporting software"
      #$become_scheme apk add zsh wl-clipboard
      ##alpine-zsh-config
      #msg_notification "installing and configuring starship.rs"
      #$become_scheme apk add starship starship-zsh-completion starship-zsh-plugin
      #cp config/zshrc $HOME/.zshrc
      #zsh
      #source $HOME/.zshrc

install-dotfiles(){
    msg_good "installing dotfiles"
    if [ -d "dotfiles" ]; then
	rm -rf dotfiles
    fi
    git clone https://github.com/philcryer/dotfiles.git
    cd dotfiles/
    if [ ! -f "$HOME/.gitconfig" ]; then
        cp .gifconfig ${HOME}
    fi
    cp -R .gitignore .wgetrc .screenrc .tmux.conf .hushlogin .curlrc .abcde.conf .aliases ${HOME}
    cd ..; rm -rf dotfiles
}

todo(){
    cp config/zshrc ~/.zshrc
    cp -R config/terminfo ~/.terminfo
    cp -R config/nvim ~/.config/
    cp -R config/wofi ~/.config/
}

