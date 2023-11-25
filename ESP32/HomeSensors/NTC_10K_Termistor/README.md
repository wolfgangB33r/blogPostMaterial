# ESP32/ESP8266 + Viessmann NTC 10K Termistor Water Sensor

The Viessmann NTC 10k Termistor 7181301 represents a classic sensor for water temperature of all kinds, mostly used for solar water buffers.

![NTC 10k Viessmann termistor](ntc_10k_viessmann_termistor.jpeg)

The NTC 10k termistor is a 10K temperature dependent resistor with 2 wires that can be read from Arduino or ESP8266 by using a voltage divider circuit, 
using a resistor of the same resistance 10k as the termistor has.
The 10k resistor to use shows the colors brown/black/orange, as it is shown below:
![10k resistor color codes](10k_resistor_colors.png)

In order to get an analog readout on for the voltage of your voltage divider you need to choose an analog input pin on your ESP8266 as shown below:

![esp8266 analog pin](esp8266_analog_pin.png)

Now connect the NTC 10k Viessmann NTC termistor to one of the 3V and ground pins of your ESP8266 and connect the 10k resistor divided middle connection to your analog pin, as shown below:
![esp8266 NTC 10k termistor circuit](NTC_10k_esp_circuit.png)

The last part is to use the following Arduino code to read out the scaled voltage value from the analog pin and to calculate the temperature value from it.

```java
// Water temperatur Viessmann NTC 10K Termistor Sensor 
// Needs to connect to one of the ESP32 or ESP8866 analog input pins like A0
const int analogPin = A0; // Analog pin connected to the NTC thermistor
const int resistorValue = 10000; // Resistor value in ohms

void setup() {
  Serial.begin(115200);
}

void loop() {
  int sensorValue = analogRead(analogPin);

  // Convert analog reading to resistance
  float resistance = resistorValue / ((1023.0 / sensorValue) - 1.0);

  // Use the Steinhart-Hart equation to convert resistance to temperature in Celsius
  float temperature = log(resistance / 10000.0) / 3950.0 + 1.0 / (25 + 273.15);

  // Convert temperature to Fahrenheit if desired
  float temperatureF = (temperature * 9.0 / 5.0) + 32.0;

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print(" °C | ");
  Serial.print(temperatureF);
  Serial.println(" °F");

  delay(1000); // Delay for one second before reading again
}
```

Simpler termistor library variant is shown below: 

```java
A simpler implementation variant is to use the out of the box termistor.h library, as it is shown below:

#include <Thermistor.h>
#include <NTC_Thermistor.h>

#define Referenzwiderstand   10000 // Widerstandswert des Widerstandes der mit dem NTC in Reihe geschaltet wurde.
#define Nominalwiderstand     10000 // Widerstand des NTC bei Normaltemperatur
#define Nominaltemperatur    25 // Temperatur, bei der der NTC den angegebenen Widerstand hat
#define BWert                3750 // Beta Koeffizient(zu finden im Datenblatt des NTC)
Thermistor* thermistor;

// Water temperatur Viessmann NTC 10K Termistor Sensor 
// Needs to connect to one of the ESP32 or ESP8866 analog input pins like A0
int TERMISTORPIN = A0;

// init termistor
thermistor = new NTC_Thermistor(TERMISTORPIN, Referenzwiderstand, Nominalwiderstand, Nominaltemperatur, BWert);

// Read water temperature
const double celsius = thermistor->readCelsius();
```
