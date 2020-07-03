import socketserver

class tcpHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # request
        self.data = self.request.recv(1024).strip()

        print("{}:{} request:".format(self.client_address[0], self.client_address[1]))
        print("Request data: " + self.data.decode("utf-8"))
        self.data = "Şampiyon ".encode() +self.data + "!".encode()

        # response
        self.request.sendall(self.data)

if __name__ == "__main__":
    host, port = "localhost", 5000

    # create server
    with socketserver.TCPServer((host, port), tcpHandler) as server:
        server.serve_forever()