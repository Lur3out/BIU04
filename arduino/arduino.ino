#define RLED_PIN 2 // R
#define GLED_PIN 6 // G
#define BLED_PIN 4 // B
#include <Arduino.h>

byte ch;

void setup() {
  Serial.begin(115200);
  Serial.println("Initializing...");
  pinMode(RLED_PIN, OUTPUT);
  pinMode(GLED_PIN, OUTPUT);
  pinMode(BLED_PIN, OUTPUT);

  digitalWrite(BLED_PIN, HIGH);
  digitalWrite(RLED_PIN, HIGH);
  digitalWrite(GLED_PIN, HIGH);
}

void loop() {
  if (Serial.available() > 0) {  //если есть доступные данные
      ch = Serial.read();
      if (ch=='\x01') {
          digitalWrite(BLED_PIN, LOW);
          digitalWrite(RLED_PIN, HIGH);
          digitalWrite(GLED_PIN, HIGH);
      } else if (ch=='\x02') {
          digitalWrite(BLED_PIN, HIGH);
          digitalWrite(RLED_PIN, HIGH);
          digitalWrite(GLED_PIN, LOW);
      }
  } else {
    digitalWrite(BLED_PIN, HIGH);
    digitalWrite(RLED_PIN, HIGH);
    digitalWrite(GLED_PIN, HIGH);
  }
  Serial.flush();
  delay(2000);
}
