from dog import *

dog = Dog("COM5") # Change to your Outgoing COM port!
if not dog.alive:
    quit()
#dog.debug = True

while True:
    dog.sit()
    dog.up()

    for i in range(2):
        dog.head.angle(-50)
        dog.head.angle(50)
    dog.head.angle(0)

    dog.do("hi")
    dog.down()
    wait(10)


