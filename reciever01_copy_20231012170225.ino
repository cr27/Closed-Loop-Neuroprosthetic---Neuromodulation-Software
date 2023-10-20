bool flagC = false; // No LED
bool flagB = false; // Steady LED on infinitely
bool flagA = false; // Slow blinking
bool flag0 = false; // Very fast blinking

// Declare randomNumber as a float and initialize it with a random value
float randomNumber;

unsigned long previousMillis = 0;
const long interval = 1000;  // Interval in milliseconds for blinking

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT); // Set the LED pin as an output
  
  // Enable the DAC0 channel
  analogWriteResolution(12);  // Set the DAC resolution to 12 bits (0-4095)
  analogWrite(DAC0, 2048);   // Set the initial voltage to half of the maximum (2.5V)


}

void loop() {
  unsigned long currentMillis = millis();
  // Generate a random float between 0 and 3.3 for "Neural Population Voltage"
  randomNumber = random(0, 3301) / 1000.0;

  if (Serial.available()) {
  String receivedData = Serial.readStringUntil('\n');
  Serial.println("Assess encoded String alpha or 0 numeral before trial-and-error based serial monitor voltage input methodology to determine if inhibition or excitation is the desired outcome");
  receivedData.trim(); // Remove leading/trailing spaces

  // Check if the received data is a valid float
  float voltage = receivedData.toFloat();

  if (voltage >= 0.0 && voltage <= 3.3) {
    int value = (int)(voltage * 4095 / 3.3); // Convert voltage to DAC value
    analogWrite(DAC0, value);

    Serial.print("Neural Population Voltage: ");
    Serial.println(randomNumber, 2); // Display the random float value with 2 decimal places

    Serial.print("DAC0 Output Voltage (0-3.3V): ");
    Serial.print(voltage, 2); // Display the converted voltage with two decimal places
    Serial.println(" V");

    Serial.print("Your value is: ");
    Serial.println(voltage, 2); // Display the user's entered value with 2 decimal places

    if (randomNumber > voltage) {
      Serial.println("Excitation Opportunity");
    } else if (randomNumber < voltage) {
      Serial.println("Inhibition Opportunity");
    } else {
      Serial.println("Inhib or Excite Opportunity");
    }
  } else {
    Serial.println("Invalid input. Please enter a value between 0 and 3.3.");
  }



    if (receivedData.equals("C")) {
      flagC = true;
      flagB = false;
      flagA = false;
      flag0 = false;
    }
    else if (receivedData.equals("B")) {
      flagC = false;
      flagB = true;
      flagA = false;
      flag0 = false;
    }
    else if (receivedData.equals("A")) {
      flagC = false;
      flagB = false;
      flagA = true;
      flag0 = false;
    }
    else if (receivedData.equals("0")) {
      flagC = false;
      flagB = false;
      flagA = false;
      flag0 = true;
    }
  } //

  if (flagC) {
    digitalWrite(LED_BUILTIN, LOW); // Turn off the LED
  }
  else if (flagB) {
    digitalWrite(LED_BUILTIN, HIGH); // Turn on the LED
  }
  else if (flagA) {
    if (currentMillis - previousMillis >= interval) {
      previousMillis = currentMillis;
      digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN)); // Toggle the LED state
    }
  }
  else if (flag0) {
    if (currentMillis - previousMillis >= interval / 10) {
      previousMillis = currentMillis;
      digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN)); // Toggle the LED state at a faster rate
    }
  }
  // Implement other loop logic as needed
}
