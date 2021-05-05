#define RLED_PIN 2 // B
#define GLED_PIN 6 // R
#define BLED_PIN 4 // G
#include <Arduino.h>
#include <ArduinoJson.h>

byte ch;
int color = 0;

void disable(){
  digitalWrite(BLED_PIN, HIGH);
  digitalWrite(RLED_PIN, HIGH);
  digitalWrite(GLED_PIN, HIGH);
}

void setup() {
  Serial.begin(9600);
  while(!Serial)continue;
  pinMode(RLED_PIN, OUTPUT);
  pinMode(GLED_PIN, OUTPUT);
  pinMode(BLED_PIN, OUTPUT);

  disable();
}

void change(int current){
  if (current > 2) current = 0;
  if (current < 0) current = 2;
  color = current;
  
  switch(color) {
    case 0: //R
      digitalWrite(BLED_PIN, HIGH);
      digitalWrite(RLED_PIN, LOW);
      digitalWrite(GLED_PIN, HIGH);
      break;
    case 1: //G
      digitalWrite(BLED_PIN, HIGH);
      digitalWrite(RLED_PIN, HIGH);
      digitalWrite(GLED_PIN, LOW);
      break;
    case 2: //B
      digitalWrite(BLED_PIN, LOW);
      digitalWrite(RLED_PIN, HIGH);
      digitalWrite(GLED_PIN, HIGH);
      break;
  }
}

void loop() {
  int     size_ = 0;
  String  payload;
  while (!Serial.available()){}
  if (Serial.available())
    payload = Serial.readStringUntil('\n');
  StaticJsonDocument<512> doc;
  Serial.flush();
//  Serial.println("{\"Success\":\"True\"}");
  DeserializationError   error = deserializeJson(doc, payload);
  if (error) {
    Serial.println(error.c_str()); 
    return;
  }
  if (doc["operation"] == "sequence") {
      Serial.println("{\"Success\":\"True\"}");
  }
  else {
      Serial.println("{\"Success\":\"False\"}");
  }
  delay(20);
//  Serial.println("{\"Success\":\"False\"}");
}
