# Interacting with RESTful APIs based on HTTP is a common task 
# in modern software projects across programming languages. In Python,
#  the requests module provides a simple and effective way to handle 
# HTTP-based API communication.

#Making HTTP Requests

# The module offers convenient functions like:
#     requests.get()
#     requests.post()
#     requests.put()
#     requests.delete()
#     requests.head()
#     requests.options()

# 🔹 requests.get()

#     Purpose: Retrieve data from a server (read operation).
#     Example use: Fetching a webpage or data from an API.
#     Analogy: Like reading a page from a book.
# 🔹 requests.post()

#     Purpose: Send data to the server to create a new resource.
#     Example use: Submitting a form, registering a user.
#     Analogy: Like writing a new page into a notebook.
# 🔹 requests.put()

#     Purpose: Update an existing resource with new data.
#     Example use: Editing a user profile.
#     Analogy: Like replacing an old page in a book with a new version.
# 🔹 requests.delete()

#     Purpose: Delete a resource from the server.
#     Example use: Removing a user account.
#     Analogy: Like tearing a page out of a book.
# 🔹 requests.head()

#     Purpose: Similar to GET, but only retrieves headers (no body/content).
#     Example use: Check if a resource exists or get metadata.
#     Analogy: Like reading just the title of a page.
# 🔹 requests.options()

#     Purpose: Get information about what methods are allowed for a resource.
#     Example use: See if POST, PUT, etc., are supported on a URL.
#     Analogy: Like checking the table of contents for available chapters

# Response Object Properties

# The response object returned by these methods includes:

#     response.status_code: The HTTP status code (e.g., 200, 404).

#     response.content: The raw content of the server’s response.

#     response.json(): Parses the response body as JSON and returns a Python dictionary 
#       (raises an exception if the response isn’t valid JSON).

# requests simplifies working with RESTful APIs by wrapping around lower-level libraries 
# like urllib.request and offering a more Pythonic interface.

import requests

response = requests.get('http://www.python.org')

# In the following script, we can also view the properties through the response object in the python.
# org domain. The response.headers statement provides the headers of the web server response.
# Basically, the response is an object dictionary we can iterate with the key-value format using
# the items() method.

import requests, json
domain = input("Enter the hostname http://")
response = requests.get('http://'+domain)
print(response.json)
print("Status code: "+str(response.status_code))
print("Headers response: ")
for header, value in response.headers.items():
    print(header, '--->', value)
print("Headers request: ")
for header, value in response.headers.items():
    print(header, '--->', value)

print("-------------------------TO OBTAIN ONLY KEYS-----------------------")

import requests

if __name__ == "__main__":
    domain = input("Enter the hostname (without 'http://'): ")
    response = requests.get("http://" + domain)

    for header in response.headers.keys():
        print(header + ": " + response.headers[header])


# Getting Images and Links from a URL in Python
# 🔹 Downloading an Image using requests and shutil

import shutil
import requests

url = 'https://www.python.org/static/img/python-logo@2x.png'
response = requests.get(url, stream=True)

with open('python.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)

#     🔹 Accessing API Data (e.g., GitHub)
# To access data from a REST API such as GitHub:
import requests

response = requests.get('https://api.github.com/users/packt')
print(response.url)      # Prints the actual URL requested
print(response.text)     # Prints the raw response content (usually JSON)
