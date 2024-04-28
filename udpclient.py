import socket

 
while(True):

   msgfromClient=input("enter")
   if msgfromClient == 'exit':break
   byteToSend=str.encode(msgfromClient)
   serverA=("127.0.0.1",20001)
   buffersize=1024
   udpc=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
   udpc.sendto(byteToSend, serverA)
   msgfs=udpc.recvfrom(buffersize)
   msg=f"meesage client {msgfs[0][1:]}"

   print(msg)





