import socket
from contextlib import closing
from io import BytesIO


def main():
    print("Logs from your program will appear here!")
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    server_socket.accept() # wait for client
    with closing(BytesIO()) as query_buffer:
        query_buffer.write("+PONG\r\n")
        server_socket.send(query_buffer.getvalue())


if __name__ == "__main__":
    main()
