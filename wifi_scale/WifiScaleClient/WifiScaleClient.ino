/*
    This sketch sends a string to a TCP server, and prints a one-line response.
    You must run a TCP server in your local network.
    For example, on Linux you can use this command: nc -v -l 3000
*/

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>

#include "HX711.h" //Load Cell Amplifier
HX711 cell(D2, D3); //Amplifier is connected to these pins on the NodeMCU ESP8266 Board

#ifndef STASSID
#define STASSID "SPWifi"
#define STAPSK  "crazily backwash detonator dentist"
#endif

const char* ssid     = STASSID;
const char* password = STAPSK;

const char* host = "192.168.0.110";
const uint16_t port = 3000;

ESP8266WiFiMulti WiFiMulti;

void setup() 
{
  Serial.begin(115200);

  // We start by connecting to a WiFi network
  WiFi.mode(WIFI_STA);
  WiFiMulti.addAP(ssid, password);

  Serial.println();
  Serial.println();
  Serial.print("Wait for WiFi... ");

  while (WiFiMulti.run() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  delay(500);
}

int counter = 0;

void loop() {
  Serial.print("connecting to ");
  Serial.print(host);
  Serial.print(':');
  Serial.println(port);

  // Use WiFiClient class to create TCP connections
  WiFiClient client;

  if (!client.connect(host, port)) {
    Serial.println("connection failed");
    Serial.println("wait 5 sec...");
    delay(5000);
    return;
  }

  //----------Get data from load cell and amplifier
 
  long valCalibrated = 0;
  long val = 0;
  float count = 0;


  count = count + 1;
  val = 0.5 * val + 0.5 * cell.read();
  valCalibrated = (val - 4137240) / 234.20;
  
  //----------Send data to IBM Waton IoT Service
  String payload = "weight\:";
  payload += valCalibrated;
//  payload += "";
 
  Serial.print("Sending payload: ");
  Serial.println(payload);

  client.println(payload);
  // This will send the request to the server
//  client.println("hello from ESP8266");

  //read back one line from server
  Serial.println("receiving from remote server");
  String line = client.readStringUntil('\r');
  Serial.println(line);

  Serial.println("closing connection");
  client.stop();

  Serial.println("wait 5 sec...");
  delay(5000);
}
