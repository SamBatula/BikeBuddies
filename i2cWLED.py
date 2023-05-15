# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # lsusb to check device name
# #dmesg | grep "tty" to find port name

import smbus 

import RPi.GPIO as GPIO
import time
import os
import sys
import busio
import board
from adafruit_ht16k33 import segments

bus = smbus.SMBus(1)
time.sleep(1)


address = 0x04


RED_LED = 17
YELLOW_LED = 18
GREEN_LED = 27

i2c = busio.I2C(board.SCL, board.SDA)

# Create the LED segment class.
# This creates a 7 segment 4 character display:
display = segments.Seg7x4(i2c)

# Clear the display.
display.fill(0)


#Setup red LED
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED, GPIO.OUT)

#Setup yellow LED
GPIO.setmode(GPIO.BCM)
GPIO.setup(YELLOW_LED, GPIO.OUT)

#Setup green LED
GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN_LED, GPIO.OUT)

def lightOn(color):
	if color == 'red':
		GPIO.output(RED_LED, GPIO.HIGH)
		GPIO.output(YELLOW_LED, GPIO.LOW)
		GPIO.output(GREEN_LED, GPIO.LOW)
	if color == 'yellow':	
		GPIO.output(YELLOW_LED, GPIO.HIGH)
		GPIO.output(RED_LED, GPIO.LOW)
		GPIO.output(GREEN_LED, GPIO.LOW)
	if color == 'green':
		GPIO.output(GREEN_LED, GPIO.HIGH)
		GPIO.output(RED_LED, GPIO.LOW)
		GPIO.output(YELLOW_LED, GPIO.LOW)	
		
def main():
	i2cData = False
	while True:
	# send data
		i2cData = not i2cData
		bus.write_byte(address,i2cData)

		# Right Turn (R character)
		if(bus.read_byte(address) == 2):
			print ("Arduino answer to RPi:", bus.read_byte(address))
			lightOn('yellow')
			display[0] = '-'
			display[1] = '-'
			display[2] = '-'
			display[3] = '0'
			os.system("mpg321 5.mp3")
			display.fill(0)
			time.sleep(1)
			
		# Left Turn (L character)
		elif(bus.read_byte(address) == 3):
			print ("Arduino answer to RPi:", bus.read_byte(address))
			lightOn('yellow')
			display[0] = '0'
			display[1] = '-'
			display[2] = '-'
			display[3] = '-'
			os.system("mpg321 2.mp3")
			display.fill(0)
			time.sleep(1)
			
		# Stop! (S character)
		elif(bus.read_byte(address) == 4):
			print ("Arduino answer to RPi:", bus.read_byte(address))
			lightOn('red')
			display[0] = 'S'
			display[1] = 't'
			display[2] = '0'
			display[3] = 'P'
			os.system("mpg321 3.mp3")
			display.fill(0)
			time.sleep(1)
		
		# Neutral or Go (N Character)
		elif(bus.read_byte(address) == 5):
			print ("Arduino answer to RPi:", bus.read_byte(address))
			lightOn('green')
			display[1] = 'g'
			display[2] = 'o'
			# os.system("mpg321 4.mp3")
			time.sleep(1)
			display.fill(0)
			

        	
if __name__ == '__main__':
    try:
        main()
        GPIO.cleanup()
    except KeyboardInterrupt:
        gpio.cleanup()
        sys.exit(0)		
