#include <Wire.h> // Enable this line if using Arduino Uno, Mega, etc.
#include <Adafruit_GFX.h>
#include "Adafruit_LEDBackpack.h"

Adafruit_7segment matrix = Adafruit_7segment();


// I2C connection using 2 different i2c addresses
#define I2C_ADDRESS 0x08
#define I2C_ADDRESS 0x04
char stateOfLights = 'a';

void setup() {
#ifndef __AVR_ATtiny85__
  Serial.begin(9600);
  Serial.println("7 Segment Backpack Test");
#endif
  matrix.begin(0x70);

Serial.begin(9600);
Wire.begin(I2C_ADDRESS); // join i2c bus with address 0x70
Wire.onReceive(receiveEvent);

}

void loop() {
  // receive_bit = receiveEvent(1);
  Serial.print(stateOfLights);
  if(stateOfLights == 'R'){
      matrix.writeDigitNum(0,0);
      matrix.writeDigitNum(1,0);
      matrix.writeDigitNum(2,0);
      matrix.writeDigitNum(3,0);
      matrix.writeDigitNum(4,0);
      matrix.writeDisplay();
      delay(500);
      matrix.clear();
      matrix.writeDisplay();
      delay(500);
}
  else if(stateOfLights == 'Y'){

    // right blinker
      matrix.writeDigitNum(4,0);
      matrix.writeDisplay();
      delay(500);
      matrix.clear();
      matrix.writeDisplay();
      delay(500);

  // left blinker
      matrix.writeDigitNum(0,0);
      matrix.writeDisplay();
      delay(500);
      matrix.clear();
      matrix.writeDisplay();
      delay(500);
  }
  else if(stateOfLights == 'G'){

    delay(1000);
    matrix.clear();
    matrix.writeDisplay();
    delay(500);

  }
}


void receiveEvent(int bytesReceived) {
  while (Wire.available()) {
    char r = Wire.read();
    stateOfLights = r;

}
}

void receiveEvent(int bytesReceived) {
while (Wire.available()) {
char r = Wire.read();
stateOfLights = r;

}
}
