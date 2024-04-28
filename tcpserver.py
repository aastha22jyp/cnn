import socket
def Server_Program():
    host=socket.gethostname()
    port=5000
    server_socket=socket.socket()
    server_socket.bind((host,port))

    server_socket.listen(2)

    conn,address=server_socket.accept()

    print("Connection "+str(address))

    while True:
        data=conn.recv(1024).decode()
        if not data:
            break
        print(data)

        data=input('->')
        conn.send(data.encode())
    conn.close()

Server_Program()
