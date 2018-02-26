import RPi.GPIO as GPIO
import time
import math
from lidar_lite import Lidar_Lite

lidar = Lidar_Lite()
connected = lidar.connect(1)
if connected < -1:
	print "Lidar fail to initialize"
else:
	print "Lidar initialize successful"

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

# pwm1 = GPIO.PWM(23, 100)
# pwm1.start(5)
# for i in range(0,180):
	# DC= 1./8.*(i)+2
	# pwm1.ChangeDutyCycle(DC)
	# time.sleep(1)
# pwm1.stop
# GPIO.cleanup()


pwm1 = GPIO.PWM(23, 100)
pwm1.start(5)
pwm2 = GPIO.PWM(18, 100)
pwm2.start(5)
Count=0; 
points = []

for phi_degrees in range(0,60,2):
	
	#Set Vertical Lidar (PHI DEGREES)
	DC_set1= 1./8.*(0)+2
	time.sleep(1)
	DC_set2 = 1./8.*(90-phi_degrees) + 2
	pwm2.ChangeDutyCycle(DC_set2)
	time.sleep(0.5)
		
	for theta_degrees in range (1,180,1):
		#horizontal motor control
		DC_set1= 1./9.*(theta_degrees)+2
		pwm1.ChangeDutyCycle(DC_set1)
		time.sleep(0.02)
			
		# GET LIDAR READING
		distance=lidar.getDistance()
		theta_radians=(theta_degrees)*(3.14159/180)
		phi_radians = (phi_degrees)*(3.14159/180)
		x = distance * math.sin(phi_radians) * math.cos(theta_radians)
		y = distance * math.sin(phi_radians) * math.cos(theta_radians)
		z = distance * math.cos(phi_radians)
	
		
		points.append([])
		points[Count].append(x)
		points[Count].append(y)
		points[Count].append(z)
		Count=Count+1
			
		
file=open("PointCloud.txt","w")
		
for row in points:
	for j in row:
		file.write("%s "% j)
	file.write("\n")
	

file.close()
	
		
		
		
pwm2.stop()			
pwm1.stop()	
GPIO.cleanup()