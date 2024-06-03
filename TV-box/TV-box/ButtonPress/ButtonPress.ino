#define BUTTON_BACK 2
#define BUTTON_SHORTCUT1 3
#define BUTTON_SHORTCUT2 4
#define BUTTON_UP A1
#define BUTTON_LEFT 6
#define BUTTON_SEL 5
#define BUTTON_DOWN 10
#define BUTTON_RIGHT A6
#define BUTTON_POWER A7

void setup() {
  // put your setup code here, to run once:
  pinMode(BUTTON_BACK, INPUT);
  pinMode(BUTTON_SHORTCUT1, INPUT);
  pinMode(BUTTON_SHORTCUT2, INPUT);
  pinMode(BUTTON_UP, INPUT);
  pinMode(BUTTON_LEFT, INPUT);
  pinMode(BUTTON_SEL, INPUT);
  pinMode(BUTTON_DOWN, INPUT);
  pinMode(BUTTON_RIGHT, INPUT);
  pinMode(BUTTON_POWER, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  // Serial.println(digitalRead(BUTTON_BACK));  //HIGH / LOW
  // delay(100);
  if (digitalRead(BUTTON_BACK) == LOW){
    Serial.println("Back button pressed");
  }
  if (digitalRead(BUTTON_SHORTCUT1) == LOW){
    Serial.println("Shortcut button 1 pressed");
  }
  if (digitalRead(BUTTON_SHORTCUT2) == LOW){
    Serial.println("Shortcut button 2 pressed");
  }
  if (digitalRead(BUTTON_UP) == LOW){
    Serial.println("Up button pressed");
  }
  if (digitalRead(BUTTON_LEFT) == LOW){
    Serial.println("Left button pressed");
  }
  if (digitalRead(BUTTON_SEL) == LOW){
    Serial.println("Select button pressed");
  }
  if (analogRead(BUTTON_DOWN) == 0){
    // Serial.println("Down button pressed");
  }
  if (analogRead(BUTTON_RIGHT) == 0){
    Serial.println("Right button pressed");
  }
  if (analogRead(BUTTON_POWER) == 0){
    Serial.println("Power button pressed");
  }
}
