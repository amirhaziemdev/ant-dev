#!/usr/bin/python
#Ant keyboard control, has user keyboard input etc.

import serial
import time
import keyboard

baud = 115200
text = ' '
ino_stop = bytes('e')
port = '/dev/ttyACM0' #COM* for Windows, /dev/ttyACM* for Ubuntu

arduino = serial.Serial(port, baud, timeout=.1)
time.sleep(1)

print "Press 'Q' to quit"
while True:
    print "in the loop"
    text = keyboard.read_key()
    if(text=='q'):
        break
    text = bytes(text)
    
    arduino.write(text)
    time.sleep(2)
    arduino.write(ino_stop)
    print text
