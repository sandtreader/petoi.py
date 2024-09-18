---
title: "Petoi.py Library Reference"
author: "Paul Clark"
fontsize: 10pt
disable-header-and-footer: true
pagestyle: empty
geometry: margin=1cm
listings-disable-line-numbers: true
---

# Petoi.py Library Reference

The `dog.py` module provides a Dog class to control a Petoi robot dog.  It's
constructed with a serial device name, a Bluetooth MAC address or "fake":

```
dog = new Dog("COM5")
```

## Methods

A `Dog` has the following methods:

| Method              | Action                                  |
|---------------------|-----------------------------------------|
| `down()`            | Go to rest position and save power      |
| `up()`              | Stand up                                |
| `sit()`             | Sit down                                |
| `walk()`            | Walk forward                            |
| `do(skill)`         | Do a named skill (see list below)       |
| `set(index, angle)` | Set a numbered servo to the given angle |
| `pose(servos)`      | Do a multi-servo pose                   |

\newpage
### Skills

The skills available are:

#### Positions:

These are basic static positions:

| Skill name        | Action               |
|-------------------|----------------------|
| `balance` or `up` | Stand up             |
| `rest`            | Same as `down()`     |
| `str`             | Stretch out          |
| `lnd`             | Landing pose         |
| `buttUp`          | Backside upwards     |
| `dropped`         | Dropped by back legs |
| `lifted`          | Lifted by neck       |

#### Movement:

Each movement (gait) should be followed by a direction "F" (forward), "L" or "R" - e.g. `wkF` (which is what `walk()` does).

| Skill name | Action       |
|------------|--------------|
| `wk`       | Walk         |
| `bd`       | Bound        |
| `bk`       | Backward     |
| `cr`       | Crawl        |
| `gp`       | Gap          |
| `hlw`      | Halloween ?! |
| `jp`       | Jump         |
| `ph`       | Push         |
| `tr`       | Trot         |
| `vt`       | Steps        |

\newpage
#### Behaviour

These are more complex behaviours, some with sound effects!

| Skill name | Action              |
|------------|---------------------|
| `ang`      | Angry               |
| `bf`       | Backflip            |
| `bx`       | Boxing              |
| `chr`      | Cheers              |
| `ck`       | Check               |
| `cmh`      | Come here           |
| `dg`       | Dig                 |
| `ff`       | Front flip          |
| `fiv`      | High five           |
| `gdb`      | Good Boy!           |
| `hds`      | Handstand           |
| `hg`       | Hug                 |
| `hi`       | Hi!                 |
| `jmp`      | Jump                |
| `kc`       | Kick                |
| `lpov`     | Leap over           |
| `mw`       | Moonwalk            |
| `nd`       | Nod                 |
| `pd`       | Play dead           |
| `pee`      | Pee                 |
| `pu`       | Push-ups            |
| `pu1`      | One-handed push-ups |
| `rc`       | Recover             |
| `rl`       | Roll                |
| `scrh`     | Scratch             |
| `snf`      | Sniff               |
| `tbl`      | Be a table          |
| `ts`       | Test                |
| `wh`       | Wave head           |

\newpage
## Servo properties

To save remembering servo numbers, the Dog class provides properties which
hold a Servo object, which you can call `angle(n)` on to set the angle:

| Servo property     | Action               | Servo number |
|--------------------|----------------------|--------------|
| `head`             | Head                 | 0            |
| `leg.front.left`   | Front left shoulder  | 8            |
| `leg.front.right`  | Front right shoulder | 9            |
| `leg.rear.left`    | Rear left hip        | 11           |
| `leg.rear.right`   | Rear right hip       | 10           |
| `knee.front.left`  | Front left knee      | 12           |
| `knee.front.right` | Front right knee     | 13           |
| `knee.rear.left`   | Rear left knee       | 15           |
| `knee.rear.right`  | Rear right knee      | 14           |

For example, to see the rear left knee to 30 degrees:

```
dog.knee.rear.left.angle(30)
```

Typical angle values are between -50 and 50.

## Multi-servo poses

To set multiple servos at the same time, you can create a pose object, using
the above properties as keys and the angles as values - e.g.

```
crunch = {
    dog.leg.front.left: 50,
    dog.leg.front.right: 50,
    ... etc ...
}

dog.pose(crunch)
```

## Helper functions

The library provides just one helper function:

| Method    | Action                                         |
|-----------|------------------------------------------------|
| `wait(n)` | Wait for `n` seconds (which can be a fraction) |

