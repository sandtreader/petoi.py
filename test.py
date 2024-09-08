from dog import *

dog = Dog()
if not dog.alive:
    quit()

while True:
    dog.sit()
    dog.up()

    for i in range(3):
        dog.head.angle(-50)
        dog.head.angle(50)

    dog.do("hi")
    dog.down()
    wait(10)


