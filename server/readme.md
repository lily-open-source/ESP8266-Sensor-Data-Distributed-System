# ESP8266 Simple HTTP Server

This Python script transforms your ESP8266 into a basic HTTP server capable of receiving requests, processing them, and sending back a response. The server doubles the received value and returns the processed result.

## Prerequisites

Ensure that your ESP8266 board has MicroPython installed. No additional libraries are required for this script.

## Script Details

The script follows these steps:

1. **Socket Initialization:** It creates a socket, binds it to an empty address on port 8000, and starts listening for incoming connections.

2. **Request Handling:** When a connection is established, the `handle_request` function is called. It reads the request data, parses it as JSON, processes the request, and sends back the processed value.

3. **Processing Logic:** The server multiplies the received "value" by 2 to get the "processed_value."

4. **Client Connection:** After processing, the client connection is closed.

## Usage

1. Upload the script to your ESP8266 board running MicroPython.
2. Power on the ESP8266.

The ESP8266 will now act as an HTTP server, listening on port 8000. When a client connects and sends a JSON request with a "value" field, the server responds with the processed result.

## Example Client Script

To interact with the server, you can use the previous script that periodically requests data from the HTTP server and displays the processed value on an OLED display.

Feel free to modify the server script to suit your specific application or integrate it into more complex IoT projects.
