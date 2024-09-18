from dog import *

# Change to your outgoing serial port:
#   COMX (win)
#   /dev/tty.BittleXX_SSP (mac)
#   /dev/rfcommX (Linux)
#or fake to just pretend

dog = Dog("fake")

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


