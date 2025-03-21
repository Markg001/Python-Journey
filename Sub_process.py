import subprocess
import sys
import os

# subprocess: Allows execution of system commands within Python.
# sys: Provides system-related functions (e.g., detecting OS).
# os: Helps identify the operating system type.

print("Operating system:", sys.platform)

if sys.platform.startswith("linux"):
    command_ping = '/bin/ping'
    ping_parameter = '-c 1'
elif sys.platform == "darwin":
    command_ping = '/sbin/ping'
    ping_parameter = '-c 1'
elif os.name == "nt":
    command_ping = 'ping'
    ping_parameter = '-n 1'

domain = "www.google.com"

p = subprocess.Popen([command_ping, ping_parameter, domain], shell=False,
                      stderr=subprocess.PIPE)

out = p.stderr.read(1)
sys.stdout.write(str(out.decode('utf-8')))
sys.stdout.flush()
