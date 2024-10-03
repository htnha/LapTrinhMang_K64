import socket
def start_server():
    host = '127.0.0.1'  # Localhost
    port = 65432  # Port to listen on

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server is listening on {host}:{port}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024).decode()  # Receive data from the client
            if data:
                name = data.split("is")[-1].strip()  # Extract name from the message
                response = f"Hello {name}"
                conn.sendall(response.encode())  # Send response back to client

if __name__ == "__main__":
    start_server()
