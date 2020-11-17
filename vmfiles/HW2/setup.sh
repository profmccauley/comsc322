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
if [ -e $SF/$NAME ]; then
  echo "It looks like $NAME was already set up."
  exit
fi

cp -iPR $DIR $SF/$NAME
cd $SF/$NAME
git init
git config user.name "comsc322student"
git config user.email "comsc322student@example.com"
git add .
git commit -m "Initial commit of $NAME"
git config --unset user.name
git config --unset user.email

if [ -e README.md ]; then
  echo
  less -P " ?f%f - %pB\% - Use arrows to scroll and 'q' to quit. " --quit-if-one-screen README.md
fi

echo
echo "*** Setup complete.  Check your shared/$NAME directory. ***"
