# ESP8266 OLED Display Data Viewer

This Python script is designed for an ESP8266 microcontroller equipped with an OLED display. The purpose of the script is to periodically request data from an HTTP server and display the processed value on the OLED screen.

## Prerequisites

Before running the script, make sure to:

1. **Adjust the URL:** Replace the placeholder URL (`http://192.168.0.100:8000`) with the actual URL of your HTTP server.

2. **Install MicroPython Libraries:** Ensure that your ESP8266 board has MicroPython installed, and the required libraries (`urequests` and `ujson`) are available.

## Hardware Setup

Connect an OLED display to the ESP8266 using the I2C protocol. In this example, the display is assumed to be a 128x32 SSD1306 type.

## Script Execution

The script follows these steps in an infinite loop:

1. **HTTP Request:** It sends a GET request to the specified URL.

2. **Data Parsing:** The response is parsed as JSON, extracting the "processed_value."

3. **Display Update:** The OLED display is cleared, and the processed value is shown.

4. **Delay:** The script pauses for one second before repeating the process.

## Usage

1. Upload the script to your ESP8266 board running MicroPython.
2. Ensure the OLED display is properly connected.
3. Power on the ESP8266.

The OLED display will continuously update with the processed value retrieved from the HTTP server.

## Note

- This script assumes a continuous operation. Modify the loop structure as needed for specific use cases.

Feel free to adapt the script according to your specific requirements and integrate it into your IoT projects.
