""" Simple Bluetooth/Serial interface to a Petoi Bittle dog
    By Paul Clark paul@sandtreader.com, MIT licence
"""

try:
    import bluetooth
except ImportError:
    bluetooth = None

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
        self.buffer = ''
        self.debug = False

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
                self.serial.timeout = 0  # Non-blocking
                self.serial.open()
            else:
                print("No serial ports found")

        if not self.serial and bluetooth:
            print(f"Looking for a dog on Bluetooth")
            if device:
                print(f"Specifically one with {device} in the address")

            foundAddress = ''
            # Seems to take 2 hits to find anything
            for i in range(2):
                self.printd(f"Try {i+1}")
                devices = bluetooth.discover_devices(duration = 2,
                                                     flush_cache = True,
                                                     lookup_names = True)
                for address, name in list(devices):
                    self.printd(f"Device {name} at {address}")
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
                self.socket.setblocking(False)
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

        self.disable_voice()
        self.disable_gyro()
        print("Ready!")

    def __del__(self):
        if self.socket:
            self.socket.close()
        if self.serial:
            self.serial.close()

    def printd(self, msg):
        if self.debug:
            print(msg)

    def send(self, msg):
        """ Send a raw message """
        if self.buffer:
            self.printd(f"## {self.buffer}")
            self.buffer = ''             # Flush cruft from previous command
        self.printd(f">> {msg}")
        if self.socket:
            self.socket.send(msg)
        elif self.serial:
            self.serial.write(msg.encode())
        self.wait_for_response(msg[0]);

    def wait_for_response(self, token):
        while True:
            if self.socket:
                line = self.get_bluetooth_line()
            elif self.serial:
                line = self.get_serial_line()
            if line:
                self.printd(f"<< {line}")
                if line[0].lower() == token.lower():
                    break;

    def get_bluetooth_line(self):
        try:
            data = self.socket.recv(1024).decode()
            if data:
                self.buffer += data
        except socket.error as e:
            pass

        return self.get_line()

    def get_serial_line(self):
        if self.serial.in_waiting > 0:
            data = self.serial.read(1024).decode()
            if data:
                self.buffer += data

        return self.get_line()

    def get_line(self):
        """ Get and remove a single line from the buffer """
        if '\n' in self.buffer:
            lines = self.buffer.split('\n', 1)
            self.buffer = lines[1]
            return lines[0].strip()
        return None

    def down(self):
        """ Go to rest position """
        print("Down!")
        self.send("d")

    def do(self, skill):
        """ Do a skill ('sit', 'up' etc.) """
        print(f"Do '{skill}'")
        self.send('k'+skill)

    def sit(self):
        """ Sit up """
        print("Sit!")
        self.send("ksit")

    def up(self):
        """ Stand up """
        print("Up!")
        self.send("kup")

    def walk(self):
        """ Walk """
        print("Walkies!")
        self.send("kwkF")

    def set(self, index, angle):
        """ Set an individual servo """
        self.send(f"m{index} {angle}")

    def pose(self, servos):
        """ Set a pose on multiple servos simultaneously

        servos is dict of Servo -> angle
        """
        print("Pose:")
        command = ''
        sep = 'i'
        for servo, angle in servos.items():
            print(f"  {servo.name} -> {angle}")
            command = command + f"{sep}{servo.index} {angle}"
            sep = ' '
        self.send(command)

    def disable_voice(self):
        """ Disable voice control """
        print("Disabling voice control")
        self.send("XAd")

    def disable_gyro(self):
        """ Disable gyro """
        print("Disabling gyro control")
        self.send("G")

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
        print(f"Servo {self.name} ({self.index}) -> {a}")
        self.dog.set(self.index, a)

# Helpers
def wait(n):
    """ Sugar for time.sleep() """
    print(f"Wait {n}s")
    time.sleep(n)

