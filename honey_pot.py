#!user/bin/env python3
import socket
import paramiko
import threading

class SSHServer(paramiko.ServerInterface):
    
    def check_auth_password(self, username: str, password: str) -> int:
        print(f"{username}:{password}")
        return paramiko.AUTH_FAILED
    
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind({"", 2222}) # Listening on port 2222
    server_socket.listen(223)

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"Connection from {client_addr[0]}':{client_addr[1]}")
        client_socket.send(b"Hello!\n") # Sends over this message when connected
        print(client_socket.recv(256).decode())
        t = threading.Thread(target=handle_connection, args=(client_socket,))
        t.start()

def handle_connection(client_socket, ssh):
    transport = paramiko.Transport(client_socket)
    #server_key = paramiko.RSAKey.generate(2048)
    server_key = paramiko.RSAKey.from_private_key_file("key")
    transport.add_server_key(server_key)
    ssh = SSHServer()
    transport.start_server(server=ssh)

if __name__ == "__main__":
        main()

