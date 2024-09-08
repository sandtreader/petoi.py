from dog import *

dog = Dog()
if not dog.alive:
    quit()

tiptoe = {
    dog.leg.front.left: -10,
    dog.leg.front.right: -10,
    dog.leg.rear.left: 10,
    dog.leg.rear.right: 10,

    dog.knee.front.left: 90,
    dog.knee.front.right: 90,
    dog.knee.rear.left: 90,
    dog.knee.rear.right: 90
}

flat = {
    dog.leg.front.left: -90,
    dog.leg.front.right: -90,
    dog.leg.rear.left: 90,
    dog.leg.rear.right: 90,

    dog.knee.front.left: 90,
    dog.knee.front.right: 90,
    dog.knee.rear.left: 90,
    dog.knee.rear.right: 90
}


while True:
    dog.down()
    wait(2)

    dog.pose(tiptoe)
    wait(2)

    dog.pose(flat)
    wait(2)
