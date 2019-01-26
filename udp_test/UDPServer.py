from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', serverPort))
print("The server is ready to receive")
while True:
	messgae, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage =messgae.decode().upper()
	serverSocket.sendto(modifiedMessage.encode(), clientAddress)