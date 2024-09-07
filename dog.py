""" Simple Bluetooth interface to a Petoi Bittle dog
    By Paul Clark paul@sandtreader.com, MIT licence
"""

import bluetooth
import socket
import time

class Dog:
    """ Interface to a Petoi BittleX robot dog over Bluetooth """
    def __init__(self):
        self.socket = None

        print(f"Looking for a Bittle dog on Bluetooth")
        foundAddress = ''
        while not foundAddress:
            devices = bluetooth.discover_devices(duration = 5,
                                                 flush_cache = True,
                                                 lookup_names = True)
            for address, name in list(devices):
                print(f"Found {name} at {address}")
                if "Bittle" in name:
                    foundAddress = address
                    break;

            if not foundAddress:
                print("Not found yet - trying again")

        print(f"Found a dog at address {foundAddress}")

        print("Connecting...")
        self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.socket.connect((foundAddress, 1))
        print("Connected")

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

# Helpers
def wait(n):
    """ Sugar for time.sleep() """
    time.sleep(n)

