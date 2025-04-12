#urllib.request?
# What is urllib.request?
# urllib.request is a built-in Python module that lets your code:
#     Send requests to websites.
#     Download web pages, data, or files.
#     Get responses from servers.

print("========================================================================")
print("==================       EXAMPLE         ==============================")
print("======================================================================")

import urllib.request

url = ("https://www.google.com")
response = urllib.request.urlopen(url)
html = response.read().decode() # the content is in html thats why we used this variable
print(html)

# with urllib.request.urlopen(url) as response:
#     html = response.read().decode("utf-8")  # convert bytes to string
#     with open("mark.html", "w", encoding="utf-8") as file:
#         file.write(html)  # write string, with encoding