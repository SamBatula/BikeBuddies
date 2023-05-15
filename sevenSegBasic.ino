#include <Wire.h> // Enable this line if using Arduino Uno, Mega, etc.
#include <Adafruit_GFX.h>
#include "Adafruit_LEDBackpack.h"

Adafruit_7segment matrix = Adafruit_7segment();

void setup() {
#ifndef __AVR_ATtiny85__
  Serial.begin(9600);
  Serial.println("7 Segment Backpack Test");
#endif
  matrix.begin(0x70);
}

void loop() {

  // right blinker
  int x=0;
  while(x<5){
    matrix.writeDigitNum(4,0);
    matrix.writeDisplay();
    delay(500);
    matrix.clear();
    matrix.writeDisplay();
    delay(500);
    x++;
  }

// left blinker
  int y=0;
  while(y<5){
    matrix.writeDigitNum(0,0);
    matrix.writeDisplay();
    delay(500);
    matrix.clear();
    matrix.writeDisplay();
    delay(500);
    y++;
  }

  int z=0;
  while(z<5){
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
    z++;
  }

}
