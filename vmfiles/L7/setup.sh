#!/bin/bash

set -e
LEC=L7
SF=~/shared

if [ ! -e $SF ]; then
  echo "Shared folder not found."
  exit
fi
if [ -e $SF/$LEC ]; then
  echo "It looks like lecture $LEC was already set up."
  exit
fi

cp -iPR ~/class/vmfiles/$LEC $SF/$LEC
cd $SF/$LEC
git init
git config user.name "comsc322student"
git config user.email "comsc322student@example.com"
git add .
git commit -m "Initial commit"
