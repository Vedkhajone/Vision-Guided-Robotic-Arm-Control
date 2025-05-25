#include <ESP32Servo.h>

Servo servo1;  // Base servo
Servo servo2;  // Elbow servo

void setup() {
  Serial.begin(115200);
  servo1.attach(13);  // Adjust pins
  servo2.attach(12);
  servo1.write(0);  // Start at middle position
  servo2.write(0);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    int commaIndex = data.indexOf(',');
    if (commaIndex > 0) {
      int angle1 = data.substring(0, commaIndex).toInt();
      int angle2 = data.substring(commaIndex + 1).toInt();

      // Optional: Clamp angles to safe ranges
      angle1 = constrain(angle1, 0, 180);
      angle2 = constrain(angle2, 0, 180);

      servo1.write(angle1);
      servo2.write(angle2);
      Serial.print("Moving to: ");
      Serial.print(angle1);
      Serial.print(", ");
      Serial.println(angle2);
    }
  }
}

