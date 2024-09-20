# Test dog discovery and initial startup

from dog import *
dog = Dog("", True)  # with debug
if not dog.alive:
    quit()

dog.walk()
wait(10)
dog.down()

