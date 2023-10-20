void setup() {
  Serial.begin(9600);
}

void loop() {
  // Measure the signal
  unsigned long startTime = micros(); // Record the start time
  while (digitalRead(A0) == HIGH) {
    // Wait for the signal to go LOW
  }
  unsigned long endTime = micros(); // Record the end time

  // Calculate and display pulse width and frequency
  unsigned long pulseWidth = endTime - startTime;
  float frequency = 1000000.0 / pulseWidth; // Frequency in Hertz
  int rawVoltage = analogRead(A0);
  float voltage = rawVoltage * (5.0 / 1023.0); // Convert analog value to voltage

  // Output results to the Serial Monitor
  Serial.print("Voltage (V): ");
  Serial.println(voltage, 3); // Display voltage with 3 decimal places
  Serial.print("Frequency (Hz): ");
  Serial.println(frequency, 2); // Display frequency with 2 decimal places
  Serial.print("Pulse Width (microseconds): ");
  Serial.println(pulseWidth);

  // Send data to the computer via the serial port
  Serial.print("DATA:");
  Serial.print(pulseWidth);
  Serial.print(",");
  Serial.print(frequency);
  Serial.print(",");
  Serial.println(voltage);

  // Delay for a moment (adjust as needed)
  delay(1000);
}
