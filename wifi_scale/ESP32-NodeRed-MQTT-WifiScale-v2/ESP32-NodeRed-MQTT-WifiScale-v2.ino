/*  Node-RED and ESP32 Make a Terrarium Controller
 * 
 * This code is part of a course from Tech Explorations.
 * For information about this course, please see
 * 
 * https://techexplorations.com/so/nodered/
 * 
 * For information on hardware components and the wiring needed to 
 * run this sketch, please see the relevant lecture in the course.
 * 
 *  
 *  Created by Peter Dalmaris
 * https://github.com/plapointe6/EspMQTTClient
 */

#include "EspMQTTClient.h"
#include "esp32_secrets.h"
#include "HX711.h" //Load Cell Amplifier
HX711 cell(D2, D3); //Amplifier is connected to these pins on the NodeMCU ESP8266 Board


EspMQTTClient client(
  SECRET_SSID,
  SECRET_PASS,
  BROKER_IP,         // MQTT Broker server ip
  BROKER_USERNAME,   // Can be omitted if not needed
  BROKER_PASSWORD,   // Can be omitted if not needed
  CLIENT_NAME,       // Client name that uniquely identify your device
  BROKER_PORT        // The MQTT port, default to 1883. this line can be omitted
);

String dummy_topic = "wifiscale/test";
long dummy_data;     

void setup()
{
  Serial.begin(115200);

  // Optionnal functionnalities of EspMQTTClient :
  client.enableDebuggingMessages(); // Enable debugging messages sent to serial output
  client.enableHTTPWebUpdater();    // Enable the web updater. 
                                    // User and password default to values of MQTTUsername 
                                    // and MQTTPassword. These can be overrited with 
                                    // enableHTTPWebUpdater("user", "password").

}

void onConnectionEstablished()
{
  // Subscribe to "mytopic/test" and display received message to Serial
//  client.subscribe("mytopic/test", [](const String & payload) {
//    Serial.println(payload);
//  });
    client.publish(dummy_topic, "This is a message.");
    Serial.print("Connected");
    Serial.println();
}

void loop()
{
  client.loop(); // must be called once per loop.
  dummy_data = calculateWeight();
  Serial.print("Current: ");
  Serial.print(dummy_data);

  client.publish(dummy_topic, String(dummy_data, DEC));
  
  Serial.println();
  delay(1000);
}

long calculateWeight()
{
  //----------Get data from load cell and amplifier
 
  long valCalibrated = 0;
  long val = 0;
  float count = 0;


  count = count + 1;
  val = 0.5 * val + 0.5 * cell.read();
  valCalibrated = (val - 4137240) / 234.20;
  valCalibrated = valCalibrated - 370;
  
  //----------Send data to IBM Waton IoT Service
  String payload = "weight\:";
  payload += valCalibrated;
  return valCalibrated;

}
