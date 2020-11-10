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

cp -nPR $DIR $SF/$NAME
cd $SF/$NAME

echo "Downloading..."
HW=HW-Relocation
NM=relocation
wget http://pages.cs.wisc.edu/~remzi/OSTEP/Homework/$HW.tgz

echo "Decompressing..."
tar xf $HW.tgz

echo "Patching it so it actually works..."
sed -i.original '0,/python/s//python2/' $NM.py

echo "Renaming the README for Windows users..."
mv README-$NM README-$NM.txt

echo
echo "*** $NAME should now be ready in $SF/$NAME ***"
