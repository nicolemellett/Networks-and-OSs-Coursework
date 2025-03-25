# client side exercise 1

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 65433)

print("Connected to UDP Chat Server")

while True:
    message = input("You (Client): ")
    client_socket.sendto(message.encode(), server_address)
    
    response, _ = client_socket.recvfrom(2048)
    print(f"Server: {response.decode()}")

client_socket.close()
