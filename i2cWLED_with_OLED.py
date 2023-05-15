import smbus 
import RPi.GPIO as GPIO
import time
import os
import sys
import busio
import board
import digitalio
from adafruit_ht16k33 import segments
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1305

oled_reset = digitalio.DigitalInOut(board.D4)

WIDTH = 128
HEIGHT = 64
BORDER = 8

bus = smbus.SMBus(1)
time.sleep(1)


address = 0x04


RED_LED = 17
YELLOW_LED = 18
GREEN_LED = 27

i2c = busio.I2C(board.SCL, board.SDA)

oled = adafruit_ssd1305.SSD1305_I2C(WIDTH, HEIGHT, i2c, addr=0x3c, reset=oled_reset)

# Clear the display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)


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
			oled.fill(0)
			oled.show()
			print ("Arduino answer to RPi:", bus.read_byte(address))
			lightOn('yellow')
			draw.polygon((60, 50, 60, 10, 100, 30), outline=1, fill=1)
			draw.rectangle((20, 20, 59, 40), outline=1, fill=1)
			os.system("mpg321 5.mp3")
			oled.image(image)
			oled.show()
			oled.fill(0)
			oled.show()
			time.sleep(1)
			
		# Left Turn (L character)
		elif(bus.read_byte(address) == 3):
			oled.fill(0)
			oled.show()
			print ("Arduino answer to RPi:", bus.read_byte(address))
			lightOn('yellow')
			draw.polygon((60, 50, 60, 10, 20, 30), outline=1, fill=1)
			draw.rectangle((60, 40, 100, 20), outline=1, fill=1)
			os.system("mpg321 2.mp3")
			oled.image(image)
			oled.show()
			oled.fill(0)
			oled.show()
			time.sleep(1)
			
		# Stop! (S character)
		elif(bus.read_byte(address) == 4):
			oled.fill(0)
			oled.show()
			print ("Arduino answer to RPi:", bus.read_byte(address))
			lightOn('red')
			draw.polygon((60, 30, 50, 5, 75, 5), outline=1, fill=1)
			draw.polygon((60, 30, 75, 5, 90, 20), outline=1, fill=1)
			draw.polygon((60, 30, 90, 20, 90, 45), outline=1, fill=1)
			draw.polygon((60, 30, 90, 45, 75, 60), outline=1, fill=1)
			draw.polygon((60, 30, 75, 60, 50, 60), outline=1, fill=1)
			draw.polygon((60, 30, 50, 60, 35, 45), outline=1, fill=1)
			draw.polygon((60, 30, 35, 45, 35, 20), outline=1, fill=1)
			draw.polygon((60, 30, 35, 20, 50, 5), outline=1, fill=1)
			
			# # Load default font.
			font = ImageFont.load_default()

			text = "STOP"
			(font_width, font_height) = font.getsize(text)
			draw.text(
			     (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
			     text,
			     font=font,
			     fill=0,
			 )
			os.system("mpg321 3.mp3")
			oled.image(image)
			oled.show()
			time.sleep(1)
		
		# Neutral or Go (N Character)
		elif(bus.read_byte(address) == 5):
			oled.fill(0)
			oled.show()
			print ("Arduino answer to RPi:", bus.read_byte(address))
			lightOn('green')
			text = "GO"
			(font_width, font_height) = font.getsize(text)
			draw.text(
			     (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
			     text,
			     font=font,
			     fill=255,
			 )
			# os.system("mpg321 4.mp3")
			oled.image(image)
			oled.show()
			time.sleep(1)
			

        	
if __name__ == '__main__':
    try:
        main()
        GPIO.cleanup()
    except KeyboardInterrupt:
        gpio.cleanup()
        sys.exit(0)		
