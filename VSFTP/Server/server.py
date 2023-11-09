import socket

PORT = 1999  # Ports > 1023 are non-privileged


class Server:
    def __init__(self, port):
        self.port = port

    def socket(self):
        self.socket_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return self

    def bind(self):
        self.socket_s.bind((socket.gethostbyname("localhost"), self.port))

    def listen(self):
        self.socket_s.listen()

    def accept(self):
        self.connection, self.address = self.socket_s.accept()

    def recv(self):
        if self.is_connected:
            bytes_recv = 0
            with open("file.txt", "wb") as file:
                while True:
                    data = self.connection.recv(1024)
                    file.write(data)
                    bytes_recv += len(data)
                    if bytes_recv == 4:
                        break

    def send(self):
        if self.is_connected:
            self.connection.send(b"File received")

    def close(self):
        self.connection.close()
        self.socket_s.close()

    def is_connected(self):
        return bool(self.connection)


def main():
    server_socket = Server(PORT).socket()
    server_socket.bind()
    server_socket.listen()
    server_socket.accept()
    server_socket.recv()
    server_socket.send()
    server_socket.close()


if __name__ == "__main__":
    main()

