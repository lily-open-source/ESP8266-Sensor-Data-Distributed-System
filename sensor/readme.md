# ESP8266 Sensor Data Sender

This Python script is designed for an ESP8266 microcontroller with an analog sensor connected. It continuously reads the sensor value, sends it to an HTTP server, and repeats the process at regular intervals.

## Prerequisites

Before running the script, make sure to:

1. **Adjust the URL:** Replace the placeholder URL (`http://192.168.0.100:8000`) with the actual URL of your HTTP server.

2. **Install MicroPython Libraries:** Ensure that your ESP8266 board has MicroPython installed, and the required libraries (`urequests`) are available.

3. **Sensor Connection:** Connect the analog sensor to the ADC pin (Pin 0 in this example) on the ESP8266.

## Script Execution

The script follows these steps in an infinite loop:

1. **Read Sensor:** It uses the analog-to-digital converter (ADC) to read the sensor value.

2. **HTTP Post Request:** The sensor value is sent as a POST request to the specified URL.

3. **Delay:** The script pauses for one second before reading the sensor again.

## Usage

1. Upload the script to your ESP8266 board running MicroPython.
2. Connect an analog sensor to Pin 0 (ADC pin) on the ESP8266.
3. Power on the ESP8266.

The ESP8266 will continuously read the sensor value and send it to the specified HTTP server URL.

## Note

- Ensure the server is ready to receive POST requests and handle the incoming sensor data.

Feel free to adapt the script according to your specific sensor requirements and integrate it into your IoT projects.
