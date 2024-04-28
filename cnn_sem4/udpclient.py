import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 9999)

while True:
    message = input("Enter message to send: ")

    # Send data
    client_socket.sendto(message.encode('utf-8'), server_address)

    # Receive response
    data, address = client_socket.recvfrom(4096)
    print(f"Received response from server: {data.decode('utf-8')}")
