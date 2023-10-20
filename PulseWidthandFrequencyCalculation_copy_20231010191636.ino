const int signalPin = 2; // Digital pin connected to your signal source
volatile unsigned long startTime;
volatile unsigned long endTime;
volatile bool signalState = LOW;

void setup() {
  pinMode(signalPin, INPUT);
  Serial.begin(9600);
  attachInterrupt(digitalPinToInterrupt(signalPin), handleInterrupt, CHANGE);
}

void loop() {
  // Measure pulse width
  if (signalState == HIGH) {
    endTime = micros();
    unsigned long pulseWidth = endTime - startTime;
    Serial.print("Pulse Width (microseconds): ");
    Serial.println(pulseWidth);
  }

  // Calculate and display frequency
  float frequency = 1000000.0 / (endTime - startTime); // Frequency in Hertz
  Serial.print("Frequency (Hz): ");
  Serial.println(frequency);

  delay(1000); // Wait for 1 second before taking another measurement
}

void handleInterrupt() {
  if (signalState == LOW) {
    startTime = micros();
  }
  else {
    endTime = micros();
  }
  signalState = !signalState;
}

