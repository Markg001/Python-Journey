#!usr/env/bin python3
import re
from collections import defaultdict

log_data = """
Jan 23 12:34:56 server sshd[12345]: Failed password for invalid user admin from 192.168.1.100 port 45678 ssh2
Jan 23 12:35:01 server sshd[12346]: Failed password for root from 192.168.1.101 port 56789 ssh2
Jan 23 12:35:05 server sshd[12347]: Failed password for user test from 192.168.1.100 port 45678 ssh2
"""

failed_attempts = defaultdict(int)

for line in log_data.split("\n"):
    match = re.search(r'Failed password .* from (\d+\.\d+\.\d+\.\d+)', line)
    if match:
        ip = match.group(1)
        failed_attempts[ip] += 1

print(failed_attempts)