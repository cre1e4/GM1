
// Code 1 : Sending Text (Transmitter)
// Library: TMRh20/RF24 (https://github.com/tmrh20/RF24/)

#include <SPI.h>
#include <RF24.h>
#include <nRF24L01.h>

RF24 radio(7, 8); // CE, CSN
const byte address[6] = "000001";

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openWritingPipe(address);
  radio.setChannel(0x76);
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();
  Serial.println("Connected");
};

void loop() {
  const char txt[] = "Bye bye world";
  radio.write(&txt, sizeof(txt));
  Serial.println("Transmitted");
  delay(1000);
};
