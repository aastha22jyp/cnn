import socket
localIP ="127.0.0.1"
localPort=20001
bufferSize=1024
UDPServerSocket=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP,localPort))

print("udp serevr up and listening")

while(True):
    msgFromClient = input("enter message")
    if msgFromClient == "exit":break
    bytestTosend = str.encode(msgFromClient)
    bytesAddressPair=UDPServerSocket.recvfrom(bufferSize)
    
    message = bytesAddressPair[0]
    
    address=bytesAddressPair[1]
    
    ClientMsg ="message from Client:{}".format(message)
    ClientIP =" Client IP Address:{}".format(address)
    
    print(ClientMsg)
    print(ClientIP)
