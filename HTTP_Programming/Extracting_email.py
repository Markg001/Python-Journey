#This script extracts email addresses from any webpage by making a request to the 
# given URL and searching the page's content for email-like patterns using 
# regular expressions. It starts by simulating a browser visit using a fake 
# "User-Agent" to avoid being blocked by some websites. The urllib.request 
# module is used to fetch the webpage, and the HTML content is read. 
# Then, the re module applies a regular expression that matches email formats 
# (like name@example.com). All found email addresses are collected and printed 
# out. This script is useful for gathering contact information from public web pages.
import urllib.request
import re

USER_AGENT = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36'

url = input("Enter URL: ")

# Create a custom opener with a user-agent (pretending to be Chrome on Android)
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', USER_AGENT)]
urllib.request.install_opener(opener)

# Open the URL and read the HTML content
response = urllib.request.urlopen(url)
html_content = response.read()

# Define the email pattern
pattern = re.compile(r"[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+\.[a-zA-Z0-9_.]+")

# Find all emails in the HTML content
mails = re.findall(pattern, str(html_content))

# Print the extracted email addresses
print(mails)
