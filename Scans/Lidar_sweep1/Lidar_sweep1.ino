

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
  
for(phi_degrees = 0; phi_degrees< 900 ; phi_degrees++){
  for (float angle = 0; angle < 1810; angle++){ 
     dist = lidarLite.distance();      // With bias correction


    theta = (angle/10)*((3.14159265)/180);
    phi_radians = (phi_degrees/10) * ((3.14159265)/180);
    x =dist*sin(phi_radians)*cos(theta);
    y =dist*sin(phi_radians)*sin(theta);
    z =dist*cos(phi_radians);
  

   
    
    Serial.print(x);
    
    Serial.print(y);
    
    Serial.println(z);
    
    if (angle<1800&&angle!=0){
     Servo1.write(angle);
     delay(50);
    }else{ 
     Servo1.write(0);
     delay(1000);
     Servo2.write(phi_degrees++);
     delay(50); 
    
    }
  }
}
}

