#Ant keyboard control, has user keyboard input etc.

import serial
import time
import keyboard

baud = 9600
text = ' '
port = 'COM3' #COM* for Windows, ttyACM* for Ubuntu

arduino = serial.Serial(port, baud, timeout=.1)
time.sleep(1)

print("Press 'Q' to quit")
while True:
	text = keyboard.read_key()
	text = bytes(text, 'utf-8')
	if(keyboard.read_key()=='q'):
		break
	arduino.write(text)
	time.sleep(1)
	print(text)