from dog import *

dog = Dog()
if not dog.alive:
    quit()

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

    dog.pose({
        dog.leg.front.left: 50,
        dog.leg.front.right: 50
    })
    wait(2)
