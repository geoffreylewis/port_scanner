#!/bin/python3

################
# Port Scanner #
################

# Note: You can run this with something like "python3 port_scanner_linux.py <ip>".

# Importing modules.
from datetime import datetime
import socket
import sys

# Define the target machine (preferably with IP address).
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("You didn't put in the right number of arguments.")
    print("The syntax should be something like: python3 port_scanner_linux.py <IP address>.")
    sys.exit()

# Banner
print("=" * 25 + "PORT SCANNER" + "=" * 25)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("=" * 62)

# Try attempting the port scan.
try:
    for port in range(20, 444):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port)) #s.connect_ex is an error indicator.
        # If a port is open, a "0" will be returned; if a port is closed, a "1" will be returned.
        if result == 0:
            print(f"Port {port} is open!")
            s.close()

# Exception if you decide to Ctrl + C the process.
except KeyboardInterrupt:
    print("\nExiting program...")
    sys.exit()

# Exception if you provided hostname instead of an IP address and it doesn't resolve.
except socket.gaierror:
    print("Hostname could not be resolved.  Maybe try an IP address this time.")
    sys.exit()

# Exception if there is some sort of socket error.
except socket.error:
    print("There seems to be some sort of socket error.  Could not connect to the server.")
    sys.exit()