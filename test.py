from dog import *

dog = Dog()
if not dog.alive:
    quit()

while True:
    dog.sit()
    wait(1)

    dog.up()
    wait(1)

    for i in range(3):
        dog.head.angle(-50)
        dog.head.angle(50)

    dog.do("hi")
    dog.down()
    wait(10)


