#include <Wire.h>
#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1305.h>

// Used for software SPI
#define OLED_CLK 13
#define OLED_MOSI 11

// Used for software or hardware SPI
#define OLED_CS 10
#define OLED_DC 8

// Used for I2C or SPI
#define OLED_RESET 9

// I2C
#define I2C_ADDRESS 0x04
#define I2C_ADDRESS 0x08
Adafruit_SSD1305 display(128, 64, &Wire, OLED_RESET);
char stateOfLights = 'a';

void setup() {

  Serial.begin(9600);
  while (! Serial) delay(100);
  Serial.println("SSD1305 OLED test");
  
  if ( ! display.begin(0x3C) ) {
     Serial.println("Unable to initialize OLED");
     while (1) yield();
  }

  Serial.begin(9600);
  Wire.begin(I2C_ADDRESS); // join i2c bus with address 0x04
  Wire.onReceive(receiveEvent);

  // init done
  display.display(); // show splashscreen
  delay(3000);
  display.clearDisplay();   // clears the screen and buffer

}


void loop() {
  // receive_bit = receiveEvent(1);
  Serial.print(stateOfLights);
  if(stateOfLights == 'R'){
  
    // stop text and symbol
    display.clearDisplay();

    display.setTextSize(2);
    display.setCursor(15,20);
   // display.println("Stopping");
    display.display();
  

    display.clearDisplay();
    display.fillTriangle(60, 30, 50, 5, 75, 5, WHITE); //top
    display.fillTriangle(60, 30, 75, 5, 90, 20, WHITE); //top right
    display.fillTriangle(60, 30, 90, 20, 90, 45, WHITE); //right
    display.fillTriangle(60, 30, 90, 45, 75, 60, WHITE); //bottom right
    display.fillTriangle(60, 30, 75, 60, 50, 60, WHITE); //bottom
    display.fillTriangle(60, 30, 50, 60, 35, 45, WHITE); //bottom left
    display.fillTriangle(60, 30, 35, 45, 35, 20, WHITE); //left
    display.fillTriangle(60, 30, 35, 20, 50, 5, WHITE); //top left

    display.setTextSize(2);
    display.setTextColor(BLACK);
    display.setCursor(40,25);
    display.println("STOP");
    display.display();
    delay(2000);
  }
  else if(stateOfLights == 'Y'){
    // right turn text and symbol
    display.clearDisplay();   // clears the screen and buffer

    // text display tests
    display.setTextSize(3);
    display.setTextColor(WHITE);
    display.setCursor(0,0);
    display.println("Turning");
    display.setCursor(20,25);
    display.print("Right");
    display.display();

    display.clearDisplay();
    delay(1500);

    display.fillRect(20,20,40,20,WHITE);
    display.fillTriangle(60,50,60,10,100,30,WHITE);
    display.display();
    

  }
  else if(stateOfLights == 'G'){
    // go text and symbol
    display.clearDisplay();
    delay(1000);

    display.setTextSize(4);
    display.setCursor(25,30);
    display.println("GO!");
    display.display();
    delay(1000);


    display.clearDisplay();
    delay(100);  
  }
}
  
  //delay(1000);
 

  // left turn text and symbol
  // display.clearDisplay();
  // delay(1000);

  // display.setCursor(0,0);
  // display.println("Turning");
  // display.setCursor(30,25);
  // display.print("Left");
  // display.display();
  // delay(3000);

  // display.clearDisplay();
  // delay(1000);

  // display.fillRect(60,20,40,20,WHITE);
  // display.fillTriangle(60,50,60,10,20,30,WHITE);
  // display.display();
  // delay(3000);


void receiveEvent(int bytesReceived) {
  while (Wire.available()) {
    char r = Wire.read();
    stateOfLights = r;
    //Serial.print(r);
    // return r;
  }
}