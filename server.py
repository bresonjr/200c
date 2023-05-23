import socket
import threading

def clientthread(client_socket, client_address):
    nickname = client_socket.recv(1024).decode('utf-8')
    nicknames.append(nickname)

    while True:
        # Your server logic here

    client_socket.close()
    nicknames.remove(nickname)

nicknames = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '127.0.0.1'  # Replace with the actual IP address of the server
server_port = 12345  # Replace with the actual port number on which the server will listen

server_socket.bind((server_ip, server_port))
server_socket.listen(5)

print("Server started on {}:{}".format(server_ip, server_port))

while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=clientthread, args=(client_socket, client_address))
    client_thread.start()
