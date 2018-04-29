#ServoSpinner3000
#PHI IS PIN 18
#Horizontal is pin 23


import RPi.GPIO as GPIO
import math
from lidar_lite import Lidar_Lite
import logging
import sys
import time
import Adafruit_PCA9685

from Adafruit_BNO055 import BNO055
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(150)

#connect accel, and gyro
bno = BNO055.BNO055(serial_port='/dev/serial0', rst=17)

lidar = Lidar_Lite()
connected = lidar.connect(1)

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(18, GPIO.OUT)
# GPIO.setup(23, GPIO.OUT)

# pwm1 = GPIO.PWM(23, 50)
# pwm1.start(0)
# pwm2 = GPIO.PWM(18, 50)
# pwm2.start(0)
count=0; 
points = []

# do this shit to spam it until it works
# while True:
    # try:
        # # Initialize the BNO055 and stop if something went wrong.
        # if not bno.begin():
            # raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')
        # # Print system status and self test result.
        # status, self_test, error = bno.get_system_status()
        # break
    # except Exception as e:
        # print("Got error: {}".format(e))
        # print("Sleeping 1s before retrying")
        # time.sleep(1)

# print('System status: {0}'.format(status))		
		
# print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
# # Print out an error if system status is in error mode.
# if status == 0x01:
    # print('System error: {0}'.format(error))
    # print('See datasheet section 4.3.59 for the meaning.')

# # Print BNO055 software revision and other diagnostic data.
# sw, bl, accel, mag, gyro = bno.get_revision()
# print('Software version:   {0}'.format(sw))
# print('Bootloader version: {0}'.format(bl))
# print('Accelerometer ID:   0x{0:02X}'.format(accel))
# print('Magnetometer ID:    0x{0:02X}'.format(mag))
# print('Gyroscope ID:       0x{0:02X}\n'.format(gyro))

# print('Reading BNO055 data, press Ctrl-C to quit...')

# while True:
    # # Read the Euler angles for heading, roll, pitch (all in degrees).
	# heading, roll, pitch = bno.read_euler()
    # # Read the calibration status, 0=uncalibrated and 3=fully calibrated.
	# sys, gyro, accel, mag = bno.get_calibration_status()
	# x,y,z = bno.read_accelerometer() 
	# # Print everything out.
	# print('Heading={0:0.2F} Roll={1:0.2F} Pitch={2:0.2F}\tSys_cal={3} Gyro_cal={4} Accel_cal={5} Mag_cal={6} Xaccel={7:0.2F} Yaccel={8:0.2F} Zaccel={9:0.2F} '.format(heading, roll, pitch, sys, gyro, accel, mag,x,y,z))
	# time.sleep(1)

	# if (-0.1<=x<=0.1) and (-1.55<=y<=-0.95) and (9.80<=z<=9.9):
		# break
	
	
	
		


for phi_degree_step in range(0,604,4):
	 #Reset theta rotation to 1 degree
	  pwm.set_pwm(0,0,348)
	  time.sleep(0.01)
	  phi_degrees = (phi_degree_step/4) * 0.596
	 #Set Vertical Lidar (PHI DEGREES)
	  pwm.set_pwm(2,0,348+phi_degree_step)
	 
	  for theta_degree_step in range (0,1212,3):
		#Set Horizontal Rotation
		pwm.set_pwm(0,0,348+theta_degree_step)
		time.sleep(0.01)
		theta_degrees = (theta_degree_step/3)*0.4455
		
		distance=lidar.getDistance()
		
		theta_radians= math.radians(theta_degrees)
		phi_radians = math.radians(phi_degrees)
		x = distance * math.sin(phi_radians) * math.cos(theta_radians)
		y = distance * math.sin(phi_radians) * math.sin(theta_radians)
		z = distance * math.cos(phi_radians)
		
		points.append([])
		points[count].append(x)
		points[count].append(y)
		points[count].append(z)
		count = count+1
	
	
file=open("PointCloud.txt","w")
		
for row in points:
	for j in row:
		file.write("%s "% j)
	file.write("\n")
	

file.close()		