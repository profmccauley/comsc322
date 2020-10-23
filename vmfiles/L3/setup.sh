#!/bin/bash

set -e
LEC=L3
SF=~/shared
HF=~/shared/.cs322_lecture_code

if [ ! -e $SF ]; then
  echo "Shared folder not found."
fi
if [ ! -e $HF ]; then
  echo "Creating hidden folder for lecture code."
  mkdir $HF
fi
if [ -e $SF/$LEC ]; then
  if [ -e $HF/$LEC ]; then
    echo "It looks like lecture $LEC was already set up."
    exit
  fi
  echo "It looks like lecture $LEC was already *partially* set up?"
  exit
fi
if [ -e $HF/$LEC ]; then
  echo "It looks like lecture $LEC was already partially deleted?"
  exit
fi

git clone ~/class/ $HF/$LEC
ln -s $HF/$LEC/vmfiles/$LEC $SF/$LEC
