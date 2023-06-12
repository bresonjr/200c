import socket
import threading

def handle_client(client_socket, client_address):
    while True:
        try:
            data = client_socket.recv(2048)
            if data:
                message = data.decode('utf-8')
                print(f"Received message from {client_address}: {message}")
                # Handle the received message or perform server logic here
            else:
                print(f"Connection closed by {client_address}")
                break
        except Exception as e:
            print(f"An error occurred with {client_address}: {str(e)}")
            break

    client_socket.close()

def start_server(ip_address, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip_address, port))
    server_socket.listen(5)
    print(f"Server started on {ip_address}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# Replace with your desired IP address and port number
ip_address = '127.0.0.1'
port = 8000

start_server(ip_address, port)
