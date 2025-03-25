# Client code Example


import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 65433)
message = b"Hello, udp server!"

client_socket.sendto(message, server_address)

client_socket.close()