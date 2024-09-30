import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 8080)
client_socket.connect(server_address)
print("Connected to server...")

try:
    while True:
        # Input message to send to the server
        message = input("Client (type 'exit' to close connection): ")
        client_socket.sendall(message.encode())
        
        # Check if the client wants to close the connection
        if message.lower() == 'exit':
            print("Client has closed the connection.")
            break

        # Receive the response from the server
        data = client_socket.recv(1024).decode()
        if data.lower() == 'exit':
            print("Server has closed the connection.")
            break
        print(f"Server: {data}")

finally:
    # Clean up the connection
    client_socket.close()
    print("Connection closed.")


