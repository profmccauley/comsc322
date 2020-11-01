#!/bin/bash

set -e
if ! command -v tcsh &> /dev/null ; then
  sudo apt install -y tcsh
  echo
fi

if command -v tcsh &> /dev/null ; then
  echo "You should be good to go for HW1."
  if [[ "$PWD" != "/home/vagrant/shared" ]]; then
    echo
    echo "Before you get started, switch to your shared directory with:"
    echo "  cd ~/shared"
  fi
else
  echo "There seems to have been a problem."
fi
