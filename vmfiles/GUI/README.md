# Setting up a Graphical User Interface

This attempts to install a pretty minimal but usable graphical interface.

It needs to download and install somewhere around one or two gigabytes.  It
may take a while!

Once most of the software is installed, you need to do a few steps to finish
setting it up.

1. Exit the VM (with the 'exit' command).
2. Do a 'vagrant halt' to shut the VM down.
3. Back up your shared folder!  (Make a copy somewhere.)
4. Inside your shared/GUI folder is a new Vagrantfile.
   Use Finder or Explorer to replace the one in your base VM directory
   with this new one.  (Or you should be able to do this from the terminal
   with 'cp -i shared/GUI/Vagrantfile .' and then pressing 'y' to confirm
   overwriting the current one.)
5. Run the command 'vagrant plugin install vagrant-vbguest'

You can now do 'vagrant up' as usual to start the VM.  However, this will
now open a new window.  The first time you do it, the 'vagrant up' command
will still be taking a while to complete.  Let it finish.  Once it's done,
log in to the new window (the username and password are both "vagrant"
unless you've changed them).

This will present you with a prompt.  Run the command 'startx'.  This
should launch a basic but usable graphical Linux interface.  Several
nice applications are involved and can be accessed from the Applications
menu in the upper left.  Meld is a great tool for comparing a new
version of file to an old one.  git-cola is an invaluable tool for
working with git.  gvim is a graphical version of the mighty vim text
editor.  And if you chose to, Atom will also be installed.  And Firefox.
There are some others installed too, and you can install many more!
Oh, and there's a terminal program, of course!  Some of these are also
available on the dock at the bottom of the window.

Note that the shutdown option in the Applications menu doesn't work.
Instead, you should use 'vagrant halt' or 'vagrant suspend' the same
as before (from the window where you launched the VM, not from a
terminal inside it!).

To disable the graphical interface, do a 'vagrant halt' and then edit the
Vagrantfile with a text editor, changing the 'v.gui = true' line to be false
instead.  Then do a 'vagrant up' and it should be gone!  You can rerun the
setup script to turn it back on.
