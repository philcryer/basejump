#!/usr/bin/env sh

#===============================================================================
# basejump: a shell script that installs Ansible, then uses it to automate the
#   base setup of hosts via the `ansible/main.yml` playbook, supported by any
#   playbooks from the `ansible/requirements.txt` file
#
# Supported Linux distros and versions tested:
# 	* Alpine Linux (3.22.1)
# 	* CachyOS Linux (rolling)
# 	* Debian GNU/Linux (13 (trixie))
#	* Fedora Linux (42)
#
# Source:  https://github.com/philcryer/basejump
# Author: philcryer < phil at philcryer dot com >
# License: MIT
#=============================================================================

set -e
os=$(uname)
distro=$(cat /etc/os-release | grep ^ID= | cut -d= -f2)

msg_status() {
  echo -e "\x1B[01;34m[*]\x1B[0m $1"
}
msg_good() {
  echo -e "\x1B[01;32m[*]\x1B[0m $1"
}
msg_error() {
  echo -e "\x1B[01;31m[*]\x1B[0m $1"
}
msg_notification() {
  echo -e "\x1B[01;33m[*]\x1B[0m $1"
}

kick_off() {
  clear
  echo " b     a     s     e     j     u     m     p"; echo
  echo " |     |     |     |     |     |     |     |"
  echo " v     v     v     v     v     v     v     v"; echo
  echo " B     A     S     E     J     U     M     P"; echo
}

become_check() {
  msg_notification "checking for become scheme (sudo or doas)"
  if type sudo >/dev/null 2>&1; then
    become_scheme=sudo
  fi
  if type doas >/dev/null 2>&1; then
    become_scheme=doas
  fi
  msg_good "found $become_scheme, will use it for become scheme"
}

os_check() {
  msg_notification "checking operating system"
  if [ "$distro" == "alpine" ]; then
    msg_good "$os ($distro) is supported, continuing"
  elif [ "$distro" == "cachyos" ]; then
    msg_good "$os ($distro) is supported, continuing"
  elif [ "$distro" == "debian" ]; then
    msg_good "$os ($distro) is supported, continuing"
  elif [ "$distro" == "fedora" ]; then
    msg_good "$os ($distro) is supported, continuing"
  else
    msg_good "$os ($distro) is NOT supported. Exiting"
    exit 1
  fi
}

ansible_install() {
  msg_notification "checking if ansible and ansible-lint is installed"
  for cli in ansible ansible-lint; do
    if ! type "$cli" >/dev/null 2>&1; then
      msg_notification "installing Ansible on ${distro} via ${become_scheme}"
      if [ "$distro" == "alpine" ]; then
        $become_scheme apk --no-interactive update
        $become_scheme apk add --no-interactive git curl ansible ansible-lint
      fi
      if [ "$distro" == "cachyos" ]; then
        $become_scheme pacman -Sy --noconfirm git curl ansible ansible-lint
      fi
      if [ "$distro" == "debian" ]; then
        $become_scheme apt install -y git curl ansible ansible-lint
      fi
      if [ "$distro" == "fedora" ]; then
        $become_scheme yum install -y git curl ansible ansible-lint
      fi
    fi
  done
  msg_good "Ansible version $(ansible --version | grep "ansible \[core" | cut -d " " -f3 | cut -d "]" -f1) installed"
}

run_ansible() {
  msg_notification "handing off to Ansible, installing packages from Ansible Galaxy"
  cd ansible; ansible-galaxy install -r requirements.yml &> /dev/null
  msg_good "Ansible Galaxy packages installed"
  if [ ! -f "$HOME/.ansible/become-pass" ]; then
	msg_notification "$HOME/.ansible/become-pass NOT FOUND, prompting for password to run Ansible" 
	ansible-playbook main.yml -i inventory.yml --become-method=$become_scheme -K
  else
	msg_good "$HOME/.ansible/become-pass FOUND, using it to run Ansible" 
	ansible-playbook main.yml -i inventory.yml --become-method=$become_scheme --become-password-file=$HOME/.ansible/become-pass
  fi
}

kick_off
become_check
os_check
ansible_install
run_ansible

exit 0
