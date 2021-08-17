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
  servo1.write(0);
  delay(1000);
  servo1.write(90);
  delay(1000);
  servo1.write(180);
  delay(1000);
  servo1.write(90);
  delay(1000);
}
