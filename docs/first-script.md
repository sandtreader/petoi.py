---
title: "Petoi.py First script"
author: "Paul Clark"
fontsize: 10pt
disable-header-and-footer: true
pagestyle: empty
---

# Your first Petoi dog script

This is where you get to write some code to control a Petoi robot dog!

## Create your script file

First create a new file in the 'petoi.py' directory or project, called
"start.py".

Then add these lines:

```
from dog import *

dog = Dog("fake")

if not dog.alive:
    quit()

dog.up()
wait(3)
dog.down()
```

Watch out for the punctuation and indentation!  Python is easier than many
languages in that regard, but it still matters...  The `quit()` should be
indented with one TAB.

We're creating a 'fake' dog here, which doesn't actually connect to a real one,
but does show you what it is doing on the console.  This is great if you are
sharing dogs between multiple people; you can test your code before running it
on the real dog.

Then run it (in PyCharm, click the green triangle).  You should see this on
the console:

```
Disabling voice control
Disabling gyro control
Ready!
Up!
Wait 3s
Down!
```

Don't worry about the first part - the important thing is the `Up!`, which comes
from your `dog.up()` line, and what follows.

## Explaining the code

Let's pick apart the code:

```
from dog import *
```

This reads the `dog.py` script (or module) that I've provided, and gives you
a Dog class and a few other things (the `*` means everything in the module)

```
dog = Dog("fake")
```

This creates an instance of the class `Dog`, called `dog` (notice the difference
in casing), passing it how to connect to the physical dog.  `"fake"` means don't
actually connect - we'll change this in a minute.

```
if not dog.alive:
    quit()
```

The Dog class has a property `alive` which indicates whether it managed to
connect to it.  Fake ones always connect, but if it failed it would `quit()`,
ending the program here.  Notice how Python expresses blocks of code with
indentation rather than `{ ... }` that you might be used to in other languages.

```
dog.up()
```

This calls the `up` method (function) of the dog, which sends it the command
to stand up.  The `()` indicates you are calling a function, and there's no
extra information (parameters) being provided.

There are lots of different methods you can call, as we'll see.

```
wait(3)
```

This calls a useful function provided by the `dog.py` library which just waits
for the number of seconds provided in the brackets before continuing.

```
dog.down()
```

This is calling another `down` method which returns the dog to its resting
position.

## Connect to a real dog

In the setup instructions you should have got a device name - on Windows it
will be `COMX` (where X is a digit), on Mac `/dev/tty.BittleXX_SSP` where XX are
two digits or letters.  On Linux, it depends - ask!

Change the 'fake' to the device, so it is something like:

```
dog = Dog("COM5")
```

Then rerun the script and your dog should stand up for a while, and sit down
again!
