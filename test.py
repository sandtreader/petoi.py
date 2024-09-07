from dog import *

dog = Dog() # or e.g. Dog("5A:A6") to choose a specific one

while True:
    dog.sit()
    wait(2)

    dog.up()
    wait(2)

    dog.do("hi")
    wait(5)

    dog.down()
    wait(2)


