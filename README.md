# ESP8266 Sensor Data Distributed System

This project demonstrates the implementation of a distributed system using three ESP8266 microcontrollers. The setup involves one microcontroller collecting sensor data, another processing the data, and a third displaying the processed results on an OLED display.

## System Components

To replicate this distributed system, you will need the following components:

- Three ESP8266 microcontrollers
- USB-to-serial adapter (e.g., FTDI adapter)
- Sensor (e.g., temperature sensor)
- OLED display

## Hardware Connections

1. **Sensor Connection:**
   - Connect the sensor to the ADC (analog-to-digital converter) of one ESP8266 microcontroller.

2. **OLED Display Connection:**
   - Connect the OLED display to the I2C bus of another ESP8266 microcontroller.

3. **USB-to-Serial Connection:**
   - Connect all three ESP8266 microcontrollers to your computer using the USB-to-serial adapter.

## Usage

Follow these detailed steps to use the distributed system effectively:

1. **Burn MicroPython Firmware:**
   - Utilize the esptool utility to burn the MicroPython firmware to each ESP8266 microcontroller.
   - Refer to the [MicroPython documentation](https://micropython.org/download#esp8266) for firmware burning instructions.

2. **Upload Code:**
   - Use a tool like ampy to upload the code for each microcontroller.
   - Check the [ampy documentation](https://github.com/pycampers/ampy) for code uploading guidance.

3. **Configure Display Microcontroller:**
   - Ensure that the IP address and port of the HTTP server in the code for the display microcontroller match the server microcontroller's IP address and port.

4. **Power On:**
   - Power on all three ESP8266 microcontrollers and the OLED display.
   - The OLED display should start showing the processed value of the sensor data.

## Customization Opportunities

Feel free to customize the code to meet specific needs:

- Modify communication protocols.
- Add extra processing steps.
- Adjust display output according to requirements.

## Note

This distributed system serves as a foundation for more complex IoT projects. Explore and adapt the codebase to suit your unique applications and extend the functionalities of the system.
