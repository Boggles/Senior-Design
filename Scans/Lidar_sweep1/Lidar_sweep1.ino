

#include <Wire.h>
#include <LIDARLite.h>
#include <Servo.h>
#include <math.h>

LIDARLite lidarLite;
int cal_cnt = 0;
int servoPin = 3;
Servo Servo1;

int servoPin2 = 4;
Servo Servo2;



void setup()
{
  Serial.begin(9600);
  Serial.print("setup start");
  Servo1.attach(servoPin);
  Servo1.write(0);
  Serial.begin(9600); // Initialize serial connection to display distance readings
  lidarLite.begin(0, true); // Set configuration to default and I2C to 400 kHz
  lidarLite.configure(0);

  Servo2.attach(servoPin2);
  Servo2.write(0);
  Serial.begin(9600); // Initialize serial connection to display distance readings
  lidarLite.begin(0, true); // Set configuration to default and I2C to 400 kHz
  lidarLite.configure(0);
  
}



void loop()
{
  float x,y,z;
  float theta;
  float phi_degrees;
  float phi_radians;
  float dist;
  float angle;
  Servo1.write(0);
  Servo2.write(0);
  
for(phi_degrees = 1; phi_degrees< 90 ; phi_degrees=phi_degrees+1){
  Servo1.write(0);
  delay(1);
  for (angle = 0; angle < 181; angle=angle+0.5){ 
    dist = lidarLite.distance();      // With bias correction
    theta = (angle)*((3.14159265)/180);
    phi_radians = (phi_degrees) * ((3.14159265)/180);
    x =dist*sin(phi_radians)*cos(theta);
    y =dist*sin(phi_radians)*sin(theta);
    z =dist*cos(phi_radians);
 
    Serial.print(x);
    Serial.print(' ');
    Serial.print(y);
    Serial.print(' ');
    Serial.println(z);
    Servo1.write(angle);
    delay(1);
    
   
    
   }
   Servo2.write(phi_degrees);
   delay(1);
  }
}


