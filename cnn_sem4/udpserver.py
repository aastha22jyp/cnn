import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address and port
server_address = ('localhost', 9999)
server_socket.bind(server_address)

print('UDP server is running...')

while True:
    print('Waiting for message...')
    data, address = server_socket.recvfrom(4096)
    
    print(f"Received message from client: {data.decode('utf-8')}")

    # Echo back the received data to the client
    message = input("Enter your response: ")
    server_socket.sendto(message.encode('utf-8'), address)
