/*
 * See documentation at https://nRF24.github.io/RF24
 * See License information at root directory of this library
 * Author: Brendan Doherty (2bndy5)
 */

/**
 * A simple example of sending data from 1 nRF24L01 transceiver to another.
 *
 * This example was written to be used on 2 devices acting as "nodes".
 * Use the Serial Monitor to change each node's behavior.
 */
#include <SPI.h>
#include "printf.h"
#include "RF24.h"

#define CE_PIN 7
#define CSN_PIN 8

RF24 radio(CE_PIN, CSN_PIN);


uint8_t address[][6] = { "1Node", "2Node" };

bool radioNumber = 1; 

bool role = false;  // true = TX role, false = RX role

float payload = 0.0;

char c = ('R');

unsigned long lastReceiveTime = 0;
const unsigned long receiveTimeout = 100; // 1 second timeout




void setup() {

  Serial.begin(115200);
  while (!Serial) {
  // some boards need to wait to ensure access to serial over USB
  }

  // initialize the transceiver on the SPI bus
  if (!radio.begin()) {
    Serial.println(F("radio hardware is not responding!!"));
    while (1) {}  // hold in infinite loop
  }

  
  Serial.println(F("11111"));

  radioNumber = 0;



  radio.setPALevel(RF24_PA_LOW);  // RF24_PA_MAX is default.


  radio.setPayloadSize(sizeof(payload)); 
  // set the TX address of the RX node into the TX pipe
  radio.openWritingPipe(address[radioNumber]);  // always uses pipe 0

  // set the RX address of the TX node into a RX pipe
  radio.openReadingPipe(1, address[!radioNumber]);  // using pipe 1

  // additional setup specific to the node's role
  if (role) {
    radio.stopListening();  // put radio in TX mode
  } else {
    radio.startListening();  // put radio in RX mode
  }

  // For debugging info
  // printf_begin();             // needed only once for printing details
  // radio.printDetails();       // (smaller) function that prints raw register values
  // radio.printPrettyDetails(); // (larger) function that prints human readable data

}  // setup

void loop() {

  if (role) {
    // This device is a TX node
    unsigned long start_timer = micros();
    bool report = radio.write(&payload, sizeof(float));
    unsigned long end_timer = micros();


    if (report) {
      Serial.println(payload);  // print payload sent
      payload += 0.01;          // increment float payload
    } else {
      Serial.println(F("Transmission failed or timed out"));  // payload was not delivered
    }

    // to make this example readable in the serial monitor
    delay(100);  // slow transmissions down by 1 second

  } else {
    // This device is a RX node

    

    uint8_t pipe;
    if (radio.available(&pipe)) {              // is there a payload? get the pipe number that recieved it
      uint8_t bytes = radio.getPayloadSize();  // get the size of the payload
      radio.read(&payload, bytes);             // fetch payload from FIFO
      if (payload != 0.00) {
      Serial.println(payload);  // print the payload's value
      }
    }

    if (millis() - lastReceiveTime > receiveTimeout) {
      // Serial.println(0000);
      lastReceiveTime = millis(); // Reset the receive time
    }
  }  // role

  if (Serial.available()) {
    // change the role via the serial monitor

    char c = toupper(Serial.read());
    if (c == 'T' && !role) {
      // Become the TX node

      role = true;
      Serial.println(F("*** CHANGING TO TRANSMIT ROLE -- PRESS 'R' TO SWITCH BACK"));
      radio.stopListening();

    } else if (c == 'R' && role) {
      // Become the RX node

      role = false;
      Serial.println(F("*** CHANGING TO RECEIVE ROLE -- PRESS 'T' TO SWITCH BACK"));
      radio.startListening();
      lastReceiveTime = millis(); // Initialize the receive time
    }
  }

}  // loop
