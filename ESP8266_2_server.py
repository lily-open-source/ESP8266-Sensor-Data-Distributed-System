import urequests
import ujson

# Initialize the HTTP server
import usocket

def handle_request(client, path):
  # Read the request data
  data = client.recv(1024)
  print(data)
  
  # Parse the request data
  request = ujson.loads(data)
  
  # Process the request
  value = request["value"]
  processed_value = value * 2
  
  # Send the processed value to the client
  client.send(ujson.dumps({"processed_value": processed_value}))

s = usocket.socket()
s.bind(("", 8000))
s.listen(1)

while True:
  client, addr = s.accept()
  print("Connected from", addr)
  handle_request(client, "")
  client.close()
