from dog import *

dog = Dog("", True)
if not dog.alive:
    quit()

base = {
    dog.leg.front.left: 50,
    dog.leg.front.right: 50,
    dog.leg.rear.left: 50,
    dog.leg.rear.right: 50,

    dog.knee.front.left: 0,
    dog.knee.front.right: 0,
    dog.knee.rear.left: 0,
    dog.knee.rear.right: 0
}

dog.pose(base)
current = base.copy()

leg_base = 40
leg_swing = 30

knee_base = 0
knee_swing = 20

def set_leg(pose, leg, knee, phase):
    # Reduce phase to 0..1
    phase = phase-int(phase)

    # Convert to linear oscillation
    if phase < 0.5:
        phase = 2*phase
    else:
        phase = 2*(1-phase)

    phase = round(phase, 2)
    pose[leg] = leg_base + phase*leg_swing
    pose[knee] = knee_base + phase*knee_swing

while True:
    for i in range(0,100,10):
        phase = i/100.0
        print(phase)
        set_leg(current, dog.leg.front.right, dog.knee.front.right, phase)
        set_leg(current, dog.leg.rear.left, dog.knee.rear.left, phase + 0.25)
        set_leg(current, dog.leg.rear.right, dog.knee.rear.right, phase + 0.5)
        set_leg(current, dog.leg.front.left, dog.knee.front.left, phase + 0.75)
        dog.pose(current)
        wait(0.1)





