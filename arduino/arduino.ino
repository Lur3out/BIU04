#define RLED_PIN 2 // R
#define GLED_PIN 6 // G
#define BLED_PIN 4 // B
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

void change(int color){  
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
  //(!Serial.available()){} //Если команды нет, вечный непрерывный цикл
  if (Serial.available()) {
    payload = Serial.readStringUntil('\n');
    StaticJsonDocument<512> doc;
    Serial.flush();
    DeserializationError error = deserializeJson(doc, payload);
    if (error) {
      Serial.println(error.c_str()); 
      return;
    }
    if (doc["type"] == "init") {
        Serial.println("{\"devices\": [{\"type\": \"rgb\", \"name\": \"rgb1\"}]}");
    } else if (doc["type"] == "set"){
      if (doc["device"] == "rgb1" && doc["option"] == "color"){
        if (doc["value"] == "r") change(0);
        if (doc["value"] == "g") change(1);
        if (doc["value"] == "b") change(2);
      }
    } else {
        Serial.println("{\"Success\":\"False\"}");
    }
  }
  delay(20);
}