#ServoSpinner3000
#PHI IS PIN 18
#Horizontal is pin 23


import RPi.GPIO as GPIO
import time
import math
from lidar_lite import Lidar_Lite

lidar = Lidar_Lite()
connected = lidar.connect(1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

pwm1 = GPIO.PWM(23, 50)
pwm1.start(0)
pwm2 = GPIO.PWM(18, 50)
pwm2.start(0)
count=0; 
points = []

def SetAngle1(angle,sleep):
	duty = float(angle)/18 + float(2)
	#GPIO.output(23,True)
	pwm1.ChangeDutyCycle(duty)
	time.sleep(sleep)
	#GPIO.output(23,False)
	pwm1.ChangeDutyCycle(0)
	
def SetAngle2(angle,sleep):
	duty = float(angle)/18 + float(2)
	#GPIO.output(18,True)
	pwm2.ChangeDutyCycle(duty)
	time.sleep(sleep)
	#GPIO.output(18,False)
	pwm2.ChangeDutyCycle(0)

for phi_degrees in range(4,90,1):
	 #Reset theta rotation to 1 degree
	  SetAngle1(1,1)
	 #Set Vertical Lidar (PHI DEGREES)
	  SetAngle2(phi_degrees,0.2)
	 
	  for theta_degrees in range (1,180,1):
		#Set Horizontal Rotation
		SetAngle1(theta_degrees,0.02)
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
SetAngle2(5,1)	
pwm2.stop()
pwm1.stop()
GPIO.cleanup()