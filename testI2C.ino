#include <Wire.h> // Enable this line if using Arduino Uno, Mega, etc.
#include <Adafruit_GFX.h>
#include "Adafruit_LEDBackpack.h"

Adafruit_7segment matrix = Adafruit_7segment();

// I2C connection using 2 different i2c addresses
#define I2C_ADDRESS 0x70
#define I2C_ADDRESS 0x08
char stateOfLights = 'a';

void setup() {
#ifndef __AVR_ATtiny85__
  Serial.begin(9600);
  Serial.println("7 Segment Backpack Test");
#endif
  matrix.begin(0x70);

Serial.begin(9600);
Wire.begin(); // join i2c bus

}

void loop() {
  // receive_bit = receiveEvent(1);
  Wire.beginTransmission(8);
  Wire.write('Right');
  Wire.endTransmission();

}
