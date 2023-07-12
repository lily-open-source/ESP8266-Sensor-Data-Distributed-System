import machine
import time

# Replace this with the URL of the HTTP server
URL = "http://192.168.0.100:8000"

# Initialize the ADC (analog-to-digital converter)
adc = machine.ADC(0)

while True:
  # Read the sensor value
  sensor_value = adc.read()
  
  # Send the sensor value to the HTTP server
  urequests.post(URL, data={"value": sensor_value})
  
  # Wait a second before reading the sensor again
  time.sleep(1)
