#include <Wire.h>
#include "rgb_lcd.h"
#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX

rgb_lcd lcd;
int opcion;
void setup() 
{
    // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  mySerial.begin(9600);
  lcd.clear();
  lcd.print("Pulse boton");
  lcd.setRGB(255, 0, 0);
}

void loop() 
{
  opcion = -1;
  if(mySerial.available()>0){
    opcion = mySerial.read();
    switch(opcion){
    case 0:
      lcd.clear();
      lcd.print("Espere verde");
      lcd.setRGB(0, 0, 255);
      break;
    case 2:
      lcd.clear();
      lcd.print("Pase");
      lcd.setRGB(0, 255, 0);
      break;
    default:
      lcd.clear();
      lcd.print("Pulse boton");
      lcd.setRGB(255, 0, 0);
    break;
    }
  }
}
