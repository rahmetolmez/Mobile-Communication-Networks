### UDP Pinger Client
### Sends message to server and calculates
### the round trip time of returning message
### Author: Rahmet Ali Olmez
### December 2021

import random
from socket import *
import time
from datetime import datetime

# Set the timeout
timeout = 1
setdefaulttimeout(timeout)

serverSocket = socket(AF_INET, SOCK_DGRAM)

address = ('192.168.137.77', 12000)

for sequence_number in range(1, 11):
	start_time = time.time_ns()
	message = 'Ping ' + str(sequence_number) + ' ' + str(datetime.now().strftime("%H:%M:%S"))
	message = str.encode(message)
	serverSocket.sendto(message, address)
	# Get message from server
	try:
		message, address = serverSocket.recvfrom(1024)
		end_time = time.time_ns()
		print(message.decode('utf-8'))
		print('PACKET', sequence_number, 'RTT:', (end_time - start_time) / 1000000000, 'SECONDS')
	except:
		print('REQUEST TIMED OUT. PACKET ', sequence_number, 'LOST')
