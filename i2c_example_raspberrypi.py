import smbus
import time
import sys
bus = smbus.SMBus(1)
address = 0x04              # Arduino I2C Address
def main():
    i2cData = False
    while 1:
        # send data
        i2cData = not i2cData
        bus.write_byte(address,i2cData)
        
        # request data
        print ("Arduino answer to RPi:", bus.read_byte(address))
        
        time.sleep(1)
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        gpio.cleanup()
        sys.exit(0)
