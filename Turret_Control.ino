#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_LEDBackpack.h>
#include <Servo.h>

#define ENABLE 5

char move[2];

Servo myservo; 

// Create an instance of the matrix
Adafruit_8x8matrix myMatrix = Adafruit_8x8matrix();

uint8_t LedArray1[4][8] = {{0x00, 0x24, 0x24, 0x0, 0x42, 0x3C, 0x00, 0x00}, {0x00, 0x24, 0x24, 0x0, 0x3C, 0x42, 0x00, 0x00}, 
{0x00, 0x24, 0x24, 0x0, 0x7E, 0x42, 0x3C, 0x00}, {0x42, 0x24, 0x24, 0x0, 0x3C, 0x42, 0x42, 0x00}};

void setup() {
    // Initialize the matrix with I2C address 0x70
    myMatrix.begin(0x70);
    pinMode(ENABLE,OUTPUT);
    Serial.begin(9600);
    myservo.attach(9);
    myservo.write(0); 
}

void loop() {
    

    while(Serial.available() > 0)
    {

        int size = Serial.readBytes(move, 1);
        move[1] = '\0';

        if(move[0] == 'S') {

            myMatrix.clear();    // Clear the display buffer
            for (int i = 0; i < 8; i++) {
                uint8_t row = LedArray1[3][i];
                for (int j = 0; j < 8; j++) {
                    if (row & 0x01) {
                        myMatrix.drawPixel(j+1, i, LED_ON);    // Draw pixel at (j, i) if the bit is set
                    }
                    row >>= 1;    // Shift to the next bit
                }
            }
            myMatrix.writeDisplay();    // Update the display with the buffer content
            delay(500);    // Add a delay for visibility if needed

            digitalWrite(ENABLE,255); 
            delay(1500);
            myservo.write(70);                         
            delay(2000); 
            myservo.write(0);    
            digitalWrite(ENABLE,0); 
            delay(3000); 

            

            continue; 
        }
    }

    myMatrix.clear();    // Clear the display buffer
    for (int i = 0; i < 8; i++) {
        uint8_t row = LedArray1[0][i];
        for (int j = 0; j < 8; j++) {
            if (row & 0x01) {
                myMatrix.drawPixel(j+1, i, LED_ON);    // Draw pixel at (j, i) if the bit is set
            }
            row >>= 1;    // Shift to the next bit
        }
    }
    myMatrix.writeDisplay();    // Update the display with the buffer content
    delay(500);    // Add a delay for visibility if needed
}
