/*
 * Script to decode IR signals from a remote
 */

#include <IRremote.h>

int IRPIN = 7;

void setup()

{

Serial.begin(9600);

Serial.println("Enabling IRin");

IrReceiver.begin(IRPIN, ENABLE_LED_FEEDBACK);

Serial.println("Enabled IRin");

}

void loop()

{

if (IrReceiver.decode())

{
// Print Decoded Hex code

Serial.println(IrReceiver.decodedIRData.decodedRawData, HEX);

IrReceiver.resume();

}

delay(500);

}
