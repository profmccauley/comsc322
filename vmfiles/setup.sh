#!/bin/bash

set -e

if [ "$(uname)" != "Linux" ]; then
  echo "Not on Linux!"
  echo "Maybe you're not in your VM?"
  exit
fi

# dir name from stackoverflow 59895
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR

NAME="$(basename $DIR)"
SF=~/shared

if [ -z "$1" ]; then
  echo "Please include a task name as an argument (e.g. ./setup L3)."
  exit 1
fi

echo "Updating..."
sudo git fetch
sudo git merge --ff-only
echo "Updated."
echo

if [ ! -d "$1" ]; then
  echo "Invalid task name: $1"
  exit 2
fi

if [ ! -f "$1/setup.sh" ]; then
  echo "Not a task: $1"
  exit 2
fi

$1/setup.sh
