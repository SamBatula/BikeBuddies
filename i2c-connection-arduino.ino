#include <Wire.h>
#define I2C_ADDRESS 0x08

void setup() {
  Serial.begin(9600);
  Wire.begin(I2C_ADDRESS); // join i2c bus with address 0x04
  Wire.onReceive(receiveEvent);
}

void loop() {
  delay(100);
}

void receiveEvent(int bytesReceived) {
  while (Wire.available()) {
    char c = Wire.read();
    Serial.print(c);
  }
}