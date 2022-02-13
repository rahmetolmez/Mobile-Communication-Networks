from socket import *
import ssl # Added
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('smtp.gmail.com', 465) #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start  
with ssl.wrap_socket(socket(AF_INET, SOCK_STREAM)) as clientSocket:
	clientSocket.connect(mailserver)
#Fill in end
	recv = clientSocket.recv(1024)
	print(recv) # Added parentheses
	if recv[:3] != '220':
		print('220 reply not received from server.') # Added indentation and parens
	
	# Send HELO command and print server response.
	heloCommand = 'HELO Alice\r\n'
	clientSocket.send(str.encode(heloCommand)) # Added str.encode()
	recv1 = clientSocket.recv(1024)
	print(recv1)
	if recv1[:3] != '250':
		print('250 reply not received from server.')
	
	# Send MAIL FROM command and print server response.
	# Fill in start
	# To generate login input: echo -ne "\0username\0password"|base64
	# The input is edited just for safety
	login_input = 'a098dsufa9G0weDasCjdfX80asdfA'.encode()
	auth_plain_command = 'AUTH PLAIN '.encode()+login_input+'\r\n'.encode()
	clientSocket.send(auth_plain_command)
	response = clientSocket.recv(1024)
	print('AUTH RESPONSE: ', response)
	
	mail_from_command = 'MAIL FROM: <rahmetolmez@gmail.com>\r\n'
	clientSocket.send(mail_from_command.encode())
	response = clientSocket.recv(1024)
	print('MAIL FROM RESPONSE: ', response)
	# Fill in end
	
	# Send RCPT TO command and print server response. 
	# Fill in start
	send_rcpt_command = 'RCPT TO: <r.olmez2018@gtu.edu.tr>\r\n'
	clientSocket.send(str.encode(send_rcpt_command))
	response = clientSocket.recv(1024)
	print('RCPT TO RESPONSE: ', response)
	# Fill in end
	
	# Send DATA command and print server response. 
	# Fill in start
	data_command = 'DATA\r\n'
	clientSocket.send(str.encode(data_command))
	response = clientSocket.recv(1024)
	print('DATA RESPONSE: ', response)
	# Fill in end
	
	# Send message data.
	# Fill in start
	mail_subject = 'Subject: SMTP Mail Client Test\r\n\r\n'
	clientSocket.send(str.encode(mail_subject))
	#mail_content = 'Hello, Rahmet. This mail is sent using smtp_mail_client.py!\r\n'
	clientSocket.send(str.encode(msg))
	# Fill in end

	# Message ends with a single period.
	# Fill in start
	clientSocket.send(str.encode(endmsg))
	response = clientSocket.recv(1024)
	print('PERIOD RESPONSE: ', response)
	# Fill in end
	
	# Send QUIT command and get server response.
	# Fill in start
	period = 'QUIT\r\n'
	clientSocket.send(str.encode(period))
	response = clientSocket.recv(1024)
	print('QUIT RESPONSE: ', response)
	# Fill in end
	