#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

// Global Declarations
const int switchPin = 6;
int switchState = 0;
int prevSwitchState = 0;
int reply;

void setup() {
  // put your setup code here, to run once:
  lcd.begin(16,2);
  pinMode(switchPin, INPUT);

  // Introductory Welcome Screen! 
  lcd.print("Ask the    :)");
  lcd.setCursor(0, 1); // Move down to bottom row on LCD
  lcd.print("Crystal Ball!");

}

void loop() {
  // put your main code here, to run repeatedly:
  switchState = digitalRead(switchPin);
  if(switchState != prevSwitchState) {
    if(switchState == LOW) {
      reply = random(8);

      // Clear Screen and Reset for Answer
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("The ball says...");

      // Add a loading visual
      delay(1000);
      lcd.clear();
      lcd.print("       .");
      delay(1000);
      lcd.clear();
      lcd.print("       ..");
      delay(1000);
      lcd.clear();
      lcd.print("       ...");
      delay(1000);
      lcd.clear();
      lcd.setCursor(0, 0);

      // Randomly generate Reply
      switch(reply) {
        case 0:
        lcd.print("Yesssir");
        break;
        case 1:
        lcd.print("Prolly");
        break;
        case 2:
        lcd.print("Oh Yeah that");
        lcd.setCursor(0, 1);
        lcd.print("gonna happen lol");
        lcd.setCursor(0, 0);
        break;
        case 3:
        lcd.print("Lookin good");
        break;
        case 4:
        lcd.print("Bruh idk");
        break;
        case 5:
        lcd.print("Ask me again yo");
        break;
        case 6:
        lcd.print("I don't think");
        lcd.setCursor(0, 1);
        lcd.print("you him");
        lcd.setCursor(0, 0);
        break;
         case 7:
        lcd.print("Hell nah");
        break;
      }
    }
  }

  prevSwitchState = switchState;

}
