import sys
import time
import os
from rplidar import RPLidar

PORT_NAME = '/dev/ttyUSB0'
setpoint_angle = 20 #FOV of 20 degrees
setpoint_distance = 3048 #Distance in mm


def process_scan(scan):
	for (_, angle, distance) in scan:
		if angle >= (360 - setpoint_angle) / 2 and angle <= (360 + setpoint_angle) / 2: #Sets the FOV and collects the distance data if there is an object in the FOV
			if distance <= setpoint_distance:
				inches = distance/25.4 #Converts distances to inches
				roundedInches = round(inches, 2)
				print(f'Distance in inches: {roundedInches}')
			else:
				os.system('clear') #Clears system output if object is beyond the setpoint distance of 10 feet
				
lidar = RPLidar(PORT_NAME)
time.sleep(1)
try:
	lidar.start_motor()
	lidar.connect()
	for scan in lidar.iter_scans():
		process_scan(scan)
		if len(scan) == 0:
			print("invalid")
except Exception as e:
	print(e)
finally:
	lidar.stop()
	lidar.disconnect()
