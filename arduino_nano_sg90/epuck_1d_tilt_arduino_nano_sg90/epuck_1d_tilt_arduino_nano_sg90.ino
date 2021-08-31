// Board: "Arduino Nano"
// Processor: "ATmega328P(Old Bootloader)"

#include <Servo.h>

int servoPin = 7;

Servo servo1;

void setup()
{
  // Put your setup code here, to run once:
  servo1.attach(servoPin);
  servo1.write(90);
  delay(500);
}

void loop()
{
  moveServo(90);
  moveServo(80);
  moveServo(70);
  moveServo(60);
  moveServo(70);
  moveServo(80);
  moveServo(90);
  moveServo(100);
  moveServo(110);
  moveServo(120);
  moveServo(110);
  moveServo(100);
}

void moveServo(int angle)
{
  servo1.write(angle);
  delay(1000);
}
