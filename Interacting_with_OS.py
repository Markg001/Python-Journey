import sys
import os

if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print('[-] ' + filename + 'does not exist.')
        exit(0)
    if not os.access(filename,os.R_OK):
         print('[-] ' + filename + 'Access denied.')
         exit(0)
    # to check current working directory

import os 
pwd= os.getcwd()
list_directory = os.listdir(pwd)
for directory in list_directory:
    print('[+] ', directory)

# os.system() allows us to execute a shell command.
# • os.listdir(path) returns a list with the contents of the directory passed as an argument.
# • os.walk(path) navigates all the directories in the provided path directory, and returns
# three values: the path directory, the names of the subdirectories, and a list of filenames
# in the current directory path.

import os 
pwd= os.getcwd()
list_directory = os.walk(pwd)
for directory in list_directory:
    print('[+] ', directory)

import os
from collections import Counter

# 1. Using os.listdir() to list files and directories in the current folder
print("\n[INFO] Listing files and directories using os.listdir():")
current_directory = os.getcwd()
entries = os.listdir(current_directory)
for entry in entries:
    print(f"  [-] {entry}")

# 2. Using os.walk() to list all files and directories recursively
print("\n[INFO] Listing all files and subdirectories using os.walk():")
for root, directories, files in os.walk(".", topdown=False):
    for file_entry in files:
        print(f"  [+] File: {os.path.join(root, file_entry)}")
    for directory in directories:
        print(f"  [++] Directory: {directory}")

# 3. Counting the total number of files in the current directory
file_count = 0
for _, _, filenames in os.walk('.'):
    file_count += len(filenames)
print(f"\n[INFO] Total number of files in the current directory: {file_count}")

# 4. Counting the number of files by extension
print("\n[INFO] Counting files by extension:")
counts = Counter()
for _, _, filenames in os.walk('.'):
    for filename in filenames:
        _, extension = os.path.splitext(filename)
        counts[extension] += 1
for extension, count in counts.items():
    print(f"  {extension:8} {count}")

# 5. Getting system information and environment variables
print("\n[INFO] System Information and Environment Variables:")
print(f"  Current Directory: {os.getcwd()}")
if hasattr(os, "getuid"):  # getuid() is only available on Unix-based systems
    print(f"  User ID: {os.getuid()}")
print(f"  PATH Environment Variable: {os.getenv('PATH')}\n")

print("[INFO] Listing all environment variables:")
for key, value in os.environ.items():
    print(f"  {key}: {value}")
#SEARCHING FOR FILE AND DIRECTORIES

import os
os.path.isfile("/directory")