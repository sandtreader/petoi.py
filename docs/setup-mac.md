---
title: "Petoi.py MacOS setup"
author: "Paul Clark"
fontsize: 10pt
disable-header-and-footer: true
pagestyle: empty
geometry: margin=1cm
listings-disable-line-numbers: true
---

# How to set up to program Petoi on MacOS

## Install and set up PyCharm

1. Install PyCharm Community Edition (unless you feel like paying!) from here:

   https://jetbrains.com/pycharm/download/other.html

   Download the latest macOS version (dmg).  If you have a MacBook Air
   (M1/M2 chips) you'll need the Apple Silicon version.
   Beware, these are 600MB+!

2. Run the installer - it'll give you an icon to drag into your
   Applications folder like most MacOS applications

3. On the "open project" popup, select the right-hand entry "Get from
   VCS" (version control system), make sure 'Version control' is set
   to 'Git' and enter this project's URL:
   `https://github.com/sandtreader/petoi.py` and click "Clone".  By
   default it will create a directory called "petoi.py" in your home
   directory "PycharmProjects" but you can change this if you prefer.

4. Find the "Python Packages" icon on the right hand side (like a
   stack of plates) and search for "pyserial".  This is the module
   that allows you to talk to the Petoi dogs, either by USB cable or
   Bluetooth (we'll come to that!).  Just install the latest one, 3.5
   or whatever is latest.

## Setting up Bluetooth

We are going to be communicating with the robot dogs over Bluetooth -
the same way your headphones or cordless mouse works, but using a
"serial" protocol, which mimics the 1980's technology of serial cables
with more modern wireless communications.  To do this, we need to
'pair' with a dog:

Go to "System Settings" and click on "Bluetooth" on the left hand side.
Make sure it's turned on, and you should see a BittleXX_SSP in "Nearby
Devices" - click on "Connect".

You'll need to find the device that MacOS has created for the dog.  Open
a terminal and do:

```
ls /dev/tty.*
```

You should see a bunch of 'tty' files (nodes), one or more of which should
be `tty.BittleXX_SSP` where XX is two digits or letters.  Remember this
for the next part!

## Run your first test

Go back to PyCharm and click on "example.py" in the file listing on the
right.  Where it says

```
dog = Dog("fake")
```

change the `fake` to `/dev/tty.BittleXX_SSP` where XX is the one you saw
above (and it should be marked on the dog)

Then click on the green triangle at the top to run it!

If your dog sits up, shakes its head and waves its paw, you're ready
to program!  If not, ask your friendly helper...  Check the console at
the bottom to see what it's doing.  Like most dogs it will carry on
all day if you let it, so click on the red square to stop it.  It'll
produce a long-winded error but this is normal!


