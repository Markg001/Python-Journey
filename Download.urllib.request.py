#The given scripts demonstrate different ways to download files using Python’s 
# urllib.request module. The first example uses both urlretrieve() and urlopen() 
# to download an image from a URL and save it as python.png. The second script retrieves
#  a .gz file from a Debian repository, reads its entire binary content with
#  urlopen().read(), and saves it using the open() function in write-binary mode. 
# The third example downloads the same file in chunks of 10,000 bytes using a loop 
# to handle large files more efficiently while tracking and printing the total bytes 
# downloaded. These scripts highlight common techniques for downloading files from the
#  internet using Python

# urllib_request/download_file.py

print("--------------------------------------------------------------------------")
print("-----       DOWNLOAD AN IMAGE USING urlretrieve()   AND urlopen()    -----")
print("--------------------------------------------------------------------------")
import urllib.request

print("Starting download...")

url = "https://www.python.org/static/img/python-logo.png"

# Method 1: Using urlretrieve()
urllib.request.urlretrieve(url, "python.png")
print("Downloaded using urlretrieve()")

# Method 2: Using urlopen()
with urllib.request.urlopen(url) as response:
    print("Status:", response.status)
    print("Downloading python.png using urlopen()")
    with open("python.png", "wb") as image:
        image.write(response.read())

print("Download complete.")
print("--------------------------------------------------------------------------")
print("--------------       DOWNLOAD A .GZ FILE AND SAVE AS BINARY      ----------")
print("--------------------------------------------------------------------------")
# urllib_request/urllib_request_download_file.py
import urllib.request

url = 'http://ftp.debian.org/debian/dists/stable/contrib/Contents-all.gz'

print("Downloading Contents-all.gz...")

file_gz = urllib.request.urlopen(url).read()

with open('Contents-all.gz', 'wb') as file:
    file.write(file_gz)

print("Download and save complete.")


print("--------------------------------------------------------------------------")
print("--------       DOWNLOAD FILE IN CHUNKS (BLOCKS OF 100000BYTES)      -----")
print("--------------------------------------------------------------------------")
# urllib_request/urllib_request_download_file_bytes.py
import urllib.request

url = 'http://ftp.debian.org/debian/dists/stable/contrib/Contents-all.gz'

print("Starting chunked download...")

file_gz = urllib.request.urlopen(url)
file_size = 0

with open('Contents-all.gz', 'wb') as file:
    while True:
        chunk = file_gz.read(10000)
        if len(chunk) < 1:
            break
        file.write(chunk)
        file_size += len(chunk)

print(file_size, 'bytes copied')
