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

make

if [ -e memory_thing.c ]; then
  echo
  less -P " ?f%f - %pB\% - Use arrows to scroll and 'q' to quit. " --quit-if-one-screen memory_thing.c
fi

echo
echo "*** Setup complete.  Check your shared/$NAME directory. ***"
