CheatyVision
============

CheatyVision is a way for FIRST teams to have full teleoperated control during the autonomous period, without actually connecting to their operator console. cheatyvision_encoder.py generates QR codes based on the state of any USB game controller and then cheatyvision_decoder.py reads that code and sends the data to the robot.

Requirements
------------

Make sure to install these in the order given.

#### Encoder

1. Python 2.7.6 32-bit for Windows (https://www.python.org/ftp/python/2.7.6/python-2.7.6.msi)
2. Setup Tools (https://pypi.python.org/pypi/setuptools)
3. Pillow 2.4.0 32-bit for Python 2.7 on Windows (https://pypi.python.org/packages/2.7/P/Pillow/Pillow-2.4.0.win32-py2.7.exe)
4. QRCode 4.0.4 (https://github.com/lincolnloop/python-qrcode/archive/v4.0.4.zip)
5. PyGame 1.9.1 32-bit for Windows (http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi)

#### Decoder

1. Python 2.7.6 32-bit for Windows (https://www.python.org/ftp/python/2.7.6/python-2.7.6.msi) (same as above)
2. Setup Tools (https://pypi.python.org/pypi/setuptools) (same as above)
3. OpenCV-Python (follow instructions at http://docs.opencv.org/trunk/doc/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html)
4. ZBar 0.10 for Windows (http://sourceforge.net/projects/zbar/files/zbar/0.10/zbar-0.10-setup.exe/download)
5. ZBar for Python 2.7 (I can't find what I used, but you can try [this installer](https://github.com/jacobvalenta/zbar-py27-msi) or compiling it yourself [from the source](https://pypi.python.org/pypi/zbar))
6. pynetworktables (https://github.com/robotpy/pynetworktables)

Warnings
--------

CheatyVision was never legal to begin with, thanks to rule T22 which permits only non-powered signaling devices during autonomous. CheatyVision has never been thoroughly tested and I'm still not quite sure how ZBar really works, or what version of ZBar you need. Use at your own risk! Or your own frustration, anyway.
