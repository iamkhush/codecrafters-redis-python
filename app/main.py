import socket
from contextlib import closing
from io import BytesIO


def main():
    print("Logs from your program will appear here!")
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    connection, address = server_socket.accept() # wait for client
    with connection:
        connection.send(b'+PONG\r\n')

if __name__ == "__main__":
    main()
