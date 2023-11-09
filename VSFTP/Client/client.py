import socket

PORT = 1999  # Ports > 1023 are non-privileged


class Client:
    def __init__(self, port):
        self.port = port

    def socket(self):
        self.socket_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return self

    def connect(self):
        self.socket_c.connect((socket.gethostbyname("localhost"), self.port))

    def send(self):
        with open("file.txt", "rb") as file:
            while True:
                data = file.read(1024)
                self.socket_c.send(data)
                if not data:
                    break

    def recv(self):
        data = self.socket_c.recv(1024)
        print(data.decode("ascii"))

    def close(self):
        self.socket_c.close()

    def is_connected(self):
        return bool(self.connection)


def main():
    server_socket = Client(PORT).socket()
    server_socket.connect()
    server_socket.send()
    server_socket.recv()
    server_socket.close()


if __name__ == "__main__":
    main()

