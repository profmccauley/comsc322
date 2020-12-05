#!/bin/bash

set -e

if [ "$(uname)" != "Linux" ]; then
  echo "Not on Linux!"
  echo "Maybe you're not in your VM?"
  exit
fi

# dir name from stackoverflow 59895
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd "$DIR"

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

function replace {
  local SRC="$1"
  local DST="$2"

  if [ ! -e "$DST" ]; then
    echo "ERROR: Expected file $DST does not exist!"
    exit
  fi
  if cmp -s "$SRC" "$DST"; then
    echo "The file $SRC appears to already be up to date."
  else
    echo "We will now replace the $SRC file..."
    cp -i $SRC $DST
  fi
}

replace test_mhcsh.py $SF/PA3/test_mhcsh.py
replace test_common.py $SF/PA3/test_common.py

if [ -e README.md ]; then
  echo
  less -P " ?f%f - %pB\% - Use arrows to scroll and 'q' to quit. " --quit-if-one-screen README.md
fi
