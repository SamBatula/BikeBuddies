#include <Wire.h>
#include <Adafruit_GFX.h>


#define SLAVE_ADDRESS 0x04       // I2C address for Arduino
int i2cData = 1; 
char incoming = 'a';             // the I2C data received

void setup(){
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);

  Serial.begin(9600);
  
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


