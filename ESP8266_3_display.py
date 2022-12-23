import urequests
import ujson

# Replace this with the URL of the HTTP server
URL = "http://192.168.0.100:8000"

# Initialize the OLED display
import ssd1306

i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4))
display = ssd1306.SSD1306_I2C(128, 32, i2c)

while True:
  # Send a request to the HTTP server
  response = urequests.get(URL).text
  
  # Parse the response
  data = ujson.loads(response)
  processed_value = data["processed_value"]
  
  # Clear the display
  display.fill(0)
  
  # Display the processed value on the OLED display
  display.text("Processed value:", 0, 0)
  display.text(str(processed_value), 0, 10)
  display.show()
  
  # Wait a second before updating the display again
  time.sleep(1)
