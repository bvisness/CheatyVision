CheatyVision
============

CheatyVision is a way for FIRST teams to have full teleoperated control during the autonomous period, without actually connecting to their operator console. cheatyvision_encoder.py generates QR codes based on the state of any USB game controller and then cheatyvision_decoder.py reads that code and sends the data to the robot.

Requirements
------------

Make sure to install these in the order given.

Encoder

1. Python 2.7.6 32-bit for Windows (https://www.python.org/ftp/python/2.7.6/python-2.7.6.msi)
2. Setup Tools (https://pypi.python.org/pypi/setuptools)
3. Pillow 2.4.0 32-bit for Python 2.7 on Windows (https://pypi.python.org/packages/2.7/P/Pillow/Pillow-2.4.0.win32-py2.7.exe)
4. QRCode 4.0.4 (https://github.com/lincolnloop/python-qrcode/archive/v4.0.4.zip)
5. PyGame 1.9.1 32-bit for Windows (http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi)
