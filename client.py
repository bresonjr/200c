import socket
import threading

def receive(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == 'NICKNAME':
                client_socket.send(nickname.encode('utf-8'))
            else:
                print(message)
        except Exception as e:
            print("An error occurred:", str(e))
            client_socket.close()
            break

def write(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

nickname = input("Enter your nickname: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '127.0.0.1'  # Replace with the actual IP address of the server
server_port = 12345  # Replace with the actual port number on which the server is running

client_socket.connect((server_ip, server_port))

receive_thread = threading.Thread(target=receive, args=(client_socket,))
write_thread = threading.Thread(target=write, args=(client_socket,))

receive_thread.start()
write_thread.start()
