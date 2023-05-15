#include <Wire.h>
#include <Adafruit_GFX.h>
#include "Adafruit_LEDBackpack.h"

Adafruit_7segment matrix = Adafruit_7segment();

#define SLAVE_ADDRESS 0x04       // I2C address for Arduino
int i2cData = 1; 
char incoming = 'a';             // the I2C data received

void setup(){
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);

#ifndef __AVR_ATtiny85__
  Serial.begin(9600);
  Serial.println("7 Segment Backpack Test");
#endif
  matrix.begin(0x08);

  //sevenSeg();
}

void loop() {
  // Everything happens in the interrupts

}

// Handle reception of incoming I2C data
void receiveData(int byteCount) {
  while (Wire.available()) {
    i2cData = Wire.read();
    incoming = Serial.read();

    if (incoming == 'R') {
      i2cData = 2;
    }
    else if(incoming == 'L'){
      i2cData = 3;
    }
    else if(incoming == 'S'){
      i2cData = 4;
    }
    else{
      i2cData = 5;   
    }
  }
}
// Handle request to send I2C data
void sendData() { 
  Wire.write(i2cData);
}

void sevenSeg(char incoming){
  Serial.print(incoming);
    if (incoming == 'R') {
      matrix.writeDigitNum(4,0);
      matrix.writeDisplay();
      delay(200);
    }
    else if(incoming == 'L'){
      matrix.writeDigitNum(0,0);
      matrix.writeDisplay();
      delay(200);
    }
    else if(incoming == 'S'){
      matrix.writeDigitNum(0,0);
      matrix.writeDigitNum(1,0);
      matrix.writeDigitNum(2,0);
      matrix.writeDigitNum(3,0);
      matrix.writeDigitNum(4,0);
      matrix.writeDisplay();
      delay(200);
    }
    else{
      matrix.clear();
      matrix.writeDisplay();    
    }
  }
