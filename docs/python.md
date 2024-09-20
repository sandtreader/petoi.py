---
title: "Simple Python for dogs"
author: "Paul Clark"
fontsize: 10pt
disable-header-and-footer: true
pagestyle: empty
geometry: margin=1cm
listings-disable-line-numbers: true
---

# Simple Python for dogs

Create a dog:

```
from dog import *
dog = Dog("COM5")

# optional: dog.debug = True
```

Call a function

```
dog.sit()
```

Call a function with a value

```
dog.head.angle(50)
```

Repeat something a number of times

```
for i in range(2):
    dog.sit()
    wait(2)
    dog.up()
    wait(2)
```

Repeat something forever

```
while True:
    dog.sit()
    wait(2)
    dog.up()
    wait(2)
```

Choice of things to do

```
for i in range(10):           # note 0..9 - could use range(1, 10)
    if i > 4:                 # Also < == != <= >=
        dog.head.angle(-50)
    else:
        dog.head.angle(50)
    wait(1)
    dog.head.angle(0)
    wait(1)
```

Define and run your own function:

```
def dance():
    dog.sit()
    wait(2)
    dog.up()
    wait(2)

dance()
```

Function with a parameter:

```
def shake(angle):
    dog.head.angle(angle)
    wait(1)
    dog.head.angle(-angle)
    wait(1)

while True:
    shake(20)
```
