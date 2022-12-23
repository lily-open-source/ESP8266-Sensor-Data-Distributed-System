<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <h1>Distributed System with Three ESP8266 Microcontrollers</h1>
  <p>This project demonstrates how to set up a distributed system with three ESP8266 microcontrollers, where one microcontroller collects sensor data, another processes the data, and a third displays the results.</p>
  <h2>Setup</h2>
  <p>To set up the distributed system, you will need:</p>
  <ul>
    <li>Three ESP8266 microcontrollers</li>
    <li>A USB-to-serial adapter, such as an FTDI adapter</li>
    <li>A sensor, such as a temperature sensor</li>
    <li>An OLED display</li>
  </ul>
  <p>Connect the sensor to the ADC (analog-to-digital converter) of one of the ESP8266 microcontrollers. Connect the OLED display to the I2C bus of another ESP8266 microcontroller. Connect the three ESP8266 microcontrollers to your computer using the USB-to-serial adapter.</p>
  <h2>Usage</h2>
  <p>To use the distributed system, follow these steps:</p>
  <ol>
    <li>Burn the MicroPython firmware to the three ESP8266 microcontrollers using the esptool utility. You can find instructions on how to do this in the <a href="https://micropython.org/download#esp8266">MicroPython documentation</a>.</li>
    <li>Upload the code for each microcontroller to the corresponding ESP8266 using a tool such as ampy. You can find instructions on how to do this in the <a href="https://github.com/pycampers/ampy">ampy documentation</a>.</li>
    <li>Make sure that the IP address and port of the HTTP server in the code for the display microcontroller match the IP address and port of the server microcontroller.</li>
    <li>Power on the three ESP8266 microcontrollers and the OLED display. The OLED display should show the processed value of the sensor data.</li>
  </ol>
  <p>You can customize the code to fit your specific needs and requirements, such as by using different communication protocols, adding additional processing steps, or modifying the display output.</p>
</body>
</html>

