""" Simple Bluetooth interface to a Petoi Bittle dog
    By Paul Clark paul@sandtreader.com, MIT licence
"""

import bluetooth
import socket
import time
from types import SimpleNamespace

class Dog:
    """ Interface to a Petoi BittleX robot dog over Bluetooth """
    def __init__(self, addressMatch=""):
        self.socket = None

        print(f"Looking for a Bittle dog on Bluetooth")
        if addressMatch:
            print(f"Specifically one with {addressMatch} in the address")

        foundAddress = ''
        while not foundAddress:
            devices = bluetooth.discover_devices(duration = 5,
                                                 flush_cache = True,
                                                 lookup_names = True)
            for address, name in list(devices):
                print(f"Found {name} at {address}")
                if "Bittle" in name:
                    if not addressMatch or addressMatch in address:
                        foundAddress = address
                        break;

            if not foundAddress:
                print("Not found yet - trying again")

        print(f"Found a dog at address {foundAddress}")

        print("Connecting...")
        self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.socket.connect((foundAddress, 1))
        print("Connected")

        # Set up servos (BiBoard BittleX)
        self.head = Servo(self, "head", 0)

        self.leg = SimpleNamespace(
            front = SimpleNamespace(
                left = Servo(self, "leg.front.left", 8),
                right = Servo(self, "leg.front.right", 9)
                ),
            rear = SimpleNamespace(
                left = Servo(self, "leg.rear.left", 11),
                right = Servo(self, "leg.rear.right", 10)
            )
        )

        self.knee = SimpleNamespace(
            front = SimpleNamespace(
                left = Servo(self, "knee.front.left", 12),
                right = Servo(self, "knee.front.right", 13)
                ),
            rear = SimpleNamespace(
                left = Servo(self, "knee.rear.left", 15),
                right = Servo(self, "knee.rear.right", 14)
            )
        )

    def __del__(self):
        if self.socket:
            self.socket.close()

    def send(self, msg):
        """ Send a raw message """
        print(f">> {msg}")
        self.socket.send(msg)

    def down(self):
        """ Go to rest position """
        print("Down!")
        self.send("d")

    def do(self, skill):
        """ Do a skill ('sit', 'up' etc.) """
        self.send('k'+skill)

    def sit(self):
        """ Sit up """
        print("Sit!")
        self.do("sit")

    def up(self):
        """ Stand up """
        print("Up!")
        self.do("up")

class Servo:
    """ Represents a single servo motor on a dog """
    def __init__(self, dog, name, index):
        self.dog = dog
        self.name = name
        self.index = index

    def angle(self, a):
        print(f"Servo {self.name} -> {a}")
        self.dog.send(f"m{self.index} {a}")

# Helpers
def wait(n):
    """ Sugar for time.sleep() """
    time.sleep(n)

