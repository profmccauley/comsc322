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
if [ ! -e $SF/PA3 ]; then
  echo "It looks like PA3 was not set up yet."
  exit
fi

echo
echo "We will now replace the test_mhcsh.py file..."
cp -i $DIR/test_mhcsh.py $SF/PA3/test_mhcsh.py

if [ -e README.md ]; then
  echo
  less -P " ?f%f - %pB\% - Use arrows to scroll and 'q' to quit. " --quit-if-one-screen README.md
fi
