# Petoi.py

This is a minimal Python interface to [Petoi](https://petoi.com) BittleX
robot dogs, created for a fun half-day workshop.

It will automatically connect through either a serial port (if there are any)
or Bluetooth.  You can specify specific serial or Bluetooth devices in
the Dog() constructor if you need to (for example, to run multiple dogs)

```
$ pip3 install pybluez
$ git clone https://github.com/sandtreader/petoi.py.git
$ cd petoi.py
$ python test.py
```
## Note on broken pybluez
The pip package for pybluez seems to be broken at the moment, so you may have to build and install from source.  In Linux:

```
sudo apt install libbluetooth-dev
pip3 install git+https://github.com/pybluez/pybluez.git#egg=pybluez
```

## Note on Debian managed Python
To do the above in Debian, you'll need to create a managed environment and run pip3 and python from that:

```
$ python3 -m venv localpy
$ cd localpy
$ bin/pip3 ...
```


