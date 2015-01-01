import numpy as np
import cv2
import zbar
from PIL import Image

from encode import decode
from pynetworktables import NetworkTable as nt
import time

# CHANGE THIS TO BE YOUR TEAM'S cRIO IP ADDRESS!
HOST = "10.21.75.2"

# The name of the application window:
WINDOW_NAME = "CheatyVision"

# The rate at which updates are sent to the cRIO:
UPDATE_RATE_HZ = 40.0
PERIOD = (1.0 / UPDATE_RATE_HZ) * 1000.0

def get_time_millis():
	''' Get the current time in milliseconds. '''
	return int(round(time.time() * 1000))

def main():
	''' The main application '''

	# Open the webcam (should be the only video capture device present).
	capture = cv2.VideoCapture(0)
	
	# Initialize the arrays for the buttons and axes
	btns = [False, False, False, False, False, False, False, False, False, False, False, False]
	axes = [0, 0, 0, 0, 0, 0]
	
	# Initialize Network Tables
	nt.SetIPAddress(HOST)
	nt.SetClientMode()
	nt.Initialize()
	table = nt.GetTable('SmartDashboard')
	connected = False
	
	# Initialize ZBar
	scanner = zbar.ImageScanner()
	scanner.parse_config('enable')

	# Keep track of time so that we can provide the cRIO with a relatively constant
	# flow of data.
	last_t = get_time_millis()
	
	while True:
		# Read a new frame the webcam and convert it as necessary
		ret, frame = capture.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow(WINDOW_NAME,gray)
		pil_img = Image.fromarray(gray)
		width, height = pil_img.size
		raw = pil_img.tostring()
		
		# Scan the new frame using ZBar
		zImage = zbar.Image(width, height, 'Y800', raw)
		scanner.scan(zImage)
		
		# Process the data within the scanned code
		for symbol in zImage:
			btns, axes = decode(symbol.data)
			# Uncomment the following lines to see the decoded data in the console:
			print(btns)
			# print(axes)
			
		# Output values to the cRIO
		cur_time = get_time_millis()
		if last_t + PERIOD <= cur_time:
			# PyNetworkTables doesn't play nicely with arrays, so pull
			# out the values you need and send them individually. It will look like:
			# 
			# table.PutBoolean('name',btns[index])
			# table.PutNumber('name',axes[index])
			# 
			table.PutBoolean('first_btn',btns[0])
			table.PutNumber('first_axis',axes[0])
			
			last_t = cur_time
		
		# Capture a keypress
		key = cv2.waitKey(10) & 255
		# Escape key:
		if key == 27:
			break

if __name__ == '__main__':
	main()
