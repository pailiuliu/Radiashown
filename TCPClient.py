from socket import *
serverName = 'localHost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.connect((serverName,serverPort))
sentence = raw_input('Input lowercase sentence:')
clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)
print(modifiedMessage.decode())
clientSocket.close()
