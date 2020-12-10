#!/bin/bash

set -e

if [ "$(uname)" != "Linux" ]; then
  echo "Not on Linux!"
  echo "Maybe you're not in your VM?"
  exit
fi

# dir name from stackoverflow 59895
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

NAME="$(basename $DIR)"
SF=~/shared

if [ ! -e $SF ]; then
  echo "Shared folder not found."
  exit
fi

if [ ! -e $SF/$NAME ]; then
  mkdir $SF/$NAME
fi

cd $SF/$NAME
cat $DIR/README.md | sed -e "s/GUI/$NAME/" > README.md
cat ~/class/comsc322vm/Vagrantfile > Vagrantfile

echo
echo "This will attempt to install a pretty minimal but usable GUI."
echo "This will require downloading and installing about a gigabyte"
echo "of software.  It is also recommended that you double the amount"
echo "of memory the VM uses to 2GiB (you'll be asked about this part"
echo "specifically in a moment)."
echo "You may want to check whether you think your computer is up to it!"
echo -n "Do you want to continue (y/N)? "
read CONFIRM
if [ "$CONFIRM" != "y" ]; then
  echo "Okay.  You can run this script later if you change your mind!"
  exit 0
fi

echo
echo -n "Do you want to install the Atom text editor too (y/N)? "
read ATOM

echo
echo -n "Do you want to install Firefox (y/N)? "
read FIREFOX

echo
echo "GUI programs take up a lot of memory!  You may want to configure your VM"
echo "to have more memory, though this will mean less memory for the rest of"
echo "your computer when the VM is running.  If you have a fair amount of RAM,"
echo "you should probably give more to the VM, especially if you want to run"
echo "big programs like Atom or Firefox inside the VM."
echo -n "Do you want to double the RAM your VM can use to 2GiB (y/N)? "
read MORERAM
if [ "$MORERAM" == "y" ]; then
  cat ~/class/comsc322vm/Vagrantfile \
    | sed -e 's/\( *v\.gui = \)false /\1true /' \
    | sed -e 's/\( *v\.memory = \)1024 /\12048 /' \
    > Vagrantfile
else
  cat ~/class/comsc322vm/Vagrantfile \
    | sed -e 's/\( *v\.gui = \)false /\1true /' \
    > Vagrantfile
fi

echo

sudo apt update
sudo apt-get update
sudo apt-get upgrade -y --with-new-pkgs
sudo apt -y install --no-install-recommends xfce4 vim-gtk git-cola meld xterm gitk
if [ "$FIREFOX" == "y" ]; then
  sudo apt -y install --no-install-recommends firefox
fi
sudo apt -y install xserver-xorg xinit xfwm4-theme-breeze adwaita-icon-theme-full
if [ "$ATOM" == "y" ]; then
  sudo snap install atom --classic
fi


if [ -e README.md ]; then
  echo
  echo "-----------------------------------------------------------------------------"
  less -P " ?f%f - %pB\% - Use arrows to scroll and 'q' to quit. " --quit-if-one-screen README.md
fi

echo
echo "*** Read the instructions above to see how to finish setting up the GUI ***"
echo "    (They're also in the README.md file.)"
