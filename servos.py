from dog import *

dog = Dog() # or e.g. Dog("5A:A6") to choose a specific one

while True:
    dog.down()
    wait(1)

    dog.leg.front.left.angle(0)
    wait(2)
    dog.leg.front.right.angle(0)
    wait(2)

    dog.knee.front.left.angle(0)
    wait(2)
    dog.knee.front.right.angle(0)
    wait(2)
