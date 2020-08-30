#Serial comms with Arduino, to be run on LattePanda

import serial
import time

baud = 9600
text = 'w'
port = 'COM3' #COM* for Windows, ttyACM* for Ubuntu

arduino = serial.Serial(port, baud, timeout=.1)
time.sleep(1)
while True: 
	arduino.write(text)
	time.sleep(2)
