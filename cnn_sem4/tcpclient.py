import socket

def Client_server():
    host=socket.gethostname()
    # host='lab221-12'
    port= 5000
    
    client_socket=socket.socket()
    client_socket.connect((host,port))
    
    message= input("->")
    
    while message != 'Exit':
        client_socket.send(message.encode())
        data=client_socket.recv(1023).decode()
        
        print("received from server:"+ data)
        
        message=input('->')
    client_socket.close()

Client_server()



