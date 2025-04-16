# 📘 Making Requests with a REST API Using requests in Python

# Interacting with REST APIs is a common task in Python development, especially when working 
# with web services. The requests library provides a simple interface for sending HTTP 
# methods such as GET, POST, PUT, and DELETE. The website httpbin.org is a great tool to
#  test these HTTP methods. For instance, when making a GET request to
#  http://httpbin.org/get, the server returns a JSON response showing details about the
#  request, including headers and origin. A POST request allows us to send data to the
#  server, often simulating a form submission. In Python, this is done by passing a 
# dictionary as data or json along with optional custom headers. The response object 
# can then be used to inspect returned content, status codes, and both request and response
#  headers, which is crucial for debugging and verifying behavior when consuming APIs.

import requests
import json

# Data to send in the POST request
data_dictionary = {"id": "0123456789"}

# Custom headers for content type and accepted response format
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Sending the POST request
response = requests.post("http://httpbin.org/post", headers=headers, json=data_dictionary)

# Print status and inspect the response
print("HTTP Status Code:", response.status_code)

# If the request is successful
if response.status_code == 200:
    print("\n--- JSON Response ---")
    for key, value in response.json().items():
        print(f"{key}: {value}")

    print("\n--- Request Headers ---")
    for key, value in response.request.headers.items():
        print(f"{key} --> {value}")

    print("\n--- Server Info ---")
    print("Server:", response.headers.get('Server', 'N/A'))
else:
    print(f"Request failed with status code: {response.status_code}")
