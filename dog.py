""" Simple Bluetooth interface to a Petoi Bittle dog
    By Paul Clark paul@sandtreader.com, MIT licence
"""

import bluetooth
import socket
import time
import serial
import serial.tools.list_ports

from types import SimpleNamespace

class Dog:
    """
    Interface to a Petoi BittleX robot dog over Bluetooth or serial.

    If device is empty, looks for any serial port first, then tries any
    Bluetooth Bittle* device

    To force Bluetooth specify a portion of a MAC address, or ":"
    To force serial, specify a serial device name - e.g. /dev/rfcomm0
    """
    def __init__(self, device=""):
        self.socket = None
        self.serial = None
        self.alive = False

        # Check for serial first
        if not device or "/dev" in device:
            print(f"Looking for a dog on serial {device}")
            port = device
            if not port:
                # Find the first port
                ports = serial.tools.list_ports.comports()
                for port in ports:
                    port = port.device
                    break

            if port:
                print(f"Using serial port {port}")
                self.serial = serial.Serial()
                self.serial.port = port
                self.serial.baudrate = 115200
                self.serial.parity = serial.PARITY_NONE
                self.serial.timeout = 5
                self.serial.open()

        if not self.serial:
            print(f"Looking for a dog on Bluetooth")
            if device:
                print(f"Specifically one with {device} in the address")

            foundAddress = ''
            # Seems to take 2 hits to find anything
            for i in range(2):
                print(f"Try {i+1}")
                devices = bluetooth.discover_devices(duration = 2,
                                                     flush_cache = True,
                                                     lookup_names = True)
                for address, name in list(devices):
                    print(f"Device {name} at {address}")
                    if "Bittle" in name:
                        if not device or device in address:
                            foundAddress = address
                            break;

                if foundAddress:
                    break

            if foundAddress:
                print(f"Found a dog at Bluetooth address {foundAddress}")

                print("Connecting...")
                self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                self.socket.connect((foundAddress, 1))
                print("Connected")

        if not self.socket and not self.serial:
            print("No dog found!")
            return
        self.alive = True

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
        if self.serial:
            self.serial.close()

    def send(self, msg):
        """ Send a raw message """
        print(f">> {msg}")
        if self.socket:
            self.socket.send(msg)
        elif self.serial:
            self.serial.write(msg.encode())

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

    def set(self, index, angle):
        """ Set an individual servo """
        self.send(f"m{index} {angle}")

    def pose(self, servos):
        """ Set a pose on multiple servos simultaneously

        servos is dict of Servo -> angle
        """
        print("Pose:")
        command = ''
        sep = 'm'
        for servo, angle in servos.items():
            print(f"  {servo.name} -> {angle}")
            command = command + f"{sep}{servo.index} {angle}"
            sep = ' '
        self.send(command)

class Servo:
    """ Represents a single servo motor on a dog """
    def __init__(self, dog, name, index):
        self.dog = dog
        self.name = name
        self.index = index

    # Hash and EQ for dict
    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def angle(self, a):
        print(f"Servo {self.name} -> {a}")
        self.dog.set(self.index, a)

# Helpers
def wait(n):
    """ Sugar for time.sleep() """
    time.sleep(n)

