#!/bin/python3

import sys
import socket
from datetime import datetime

# Define our target
if len(sys.argv) == 2: # argv take an argument/s 
	target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
	
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

# Add a pretty banner
print("-" * 50)
print(f"Scanning target: {target}")
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(50, 80): # range from 50......80
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		if result == 0:
			print(f"Port {port} is open")
		s.close()

except KeyboardInterrupt:	
	print("\nExiting program.")
	sys.exit() # allow to exit
	
except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()
	
except socket.error:
	print("Could not connect to the server")
	sys.exit()
