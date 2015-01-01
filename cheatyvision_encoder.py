#!/usr/bin/env python

import pygame
import qrcode
import encode

import Tkinter
import tkMessageBox

# ----------------- INITIALIZE PYGAME -----------------
pygame.init()
w = 640
h = 640
size=(w,h)
screen = pygame.display.set_mode(size) 
screen.fill((0,0,0))

# ---------------- INITIALIZE JOYSTICK ----------------
pygame.joystick.init()
stick = None
if pygame.joystick.get_count() != 0:
	stick = pygame.joystick.Joystick(0)
	stick.init()
else:
	tkMessageBox.showinfo("Error", "No joysticks were found.")	
buttons = [0,0,0,0,0,0,0,0,0,0,0,0]
axes = [0,0,0,0]

while True:
	if pygame.key.get_pressed()[pygame.K_ESCAPE]:
		exit()
	
	# ---------------- GET JOYSTICK INPUTS ----------------
	for i in range(0, stick.get_numbuttons()):
		buttons[i] = stick.get_button(i)
	for i in range(0, stick.get_numaxes()):
		axes[i] = stick.get_axis(i)
	
	data = encode.encode(buttons, axes)
	print(data)
	
	# ------------------ MAKE PIL IMAGE -------------------
	img = qrcode.make(data)
	
	# ---------- CONVERT TO PYGAME IMAGE SURFACE ----------
	size = img.size
	imgData = img.convert("RGB").tostring("raw","RGB")	
	imgSurface = pygame.Surface(size)
	imgSurface = pygame.image.frombuffer(imgData, size, "RGB")
	
	# ------------ DISPLAY THE IMAGE ONSCREEN -------------
	imgSurface = pygame.transform.scale(imgSurface,(w,h))
	screen.blit(imgSurface,(0,0))
	pygame.time.wait(5)
	pygame.display.flip()
	
	# --------------- PROCESS PYGAME EVENTS ---------------
	pygame.event.pump()
	
#	pygame.time.wait(1)