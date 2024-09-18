# How to set up to program Petoi in Windows

## Install and set up PyCharm

1. Install PyCharm Community Edition (unless you feel like paying!) from here:

   https://jetbrains.com/pycharm/download/other.html

   Download the latest Windows (exe).  Beware, it is 450MB+!

2. Run the installer - you don't need to select 'add bin to path',
   'associate .py', 'add shortcut' etc. unless you feel like using it
   on the command line later.

3. On the "open project" popup, select the right-hand entry "Get from
   VCS" (version control system), make sure 'Version control' is set
   to 'Git' and enter this project's URL:
   `https://github.com/sandtreader/petoi.py` and click "Clone".  By
   default it will create a directory called "petoi.py" in your home
   directory "PycharmProjects" but you can change this if you prefer.

5. You'll need to create a 'virtual interpreter' - pick the latest
   version of Python (say 3.12.3) and it will download it for you and
   install it in this project.  That not only gets you the Python
   language installed (Windows doesn't have it out of the box), it
   also avoids conflicting with any other Python install in other
   projects.

6. Find the "Python Packages" icon on the right hand side (like a
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

1. Go to your Settings control panel and select "Bluetooth and other devices"
2. If you've been this way before:
   * Look for any existing Bittle__ devices and remove them
   * In "More Bluetooth options", select the "COM Ports" tab and
     remove any Bittle stuff there too
3. Back at the top of the page, select "Add Bluetooth or other
   device", "Bluetooth (mice, keyboards...)" and select one of the
   Bittle__ ones.  There will probably be more than one, and one will
   ask for a PIN number.  Don't use that one!
4. You should then see two BittleXX_SSP (XX will be a number or
   letters) "Paired" in the Other Devices list
5. Scroll down to "More Bluetooth options" and select the "COM Ports"
   tab.  You should see two COMx ports listed; one is outgoing.
   Remember that one! (e.g. COM5)

## Run your first test

Go back to PyCharm and click on "example.py" in the file listing on the
right.  Where it says

```
dog = Dog("fake")
```
change the `fake` to whatever your outgoing port number was.

Then click on the green triangle at the top to run it!

If your dog sits up, shakes its head and waves its paw, you're ready
to program!  If not, ask your friendly helper...  Check the console at
the bottom to see what it's doing.  Like most dogs it will carry on
all day if you let it, so click on the red square to stop it.  It'll
produce a long-winded error but this is normal!


