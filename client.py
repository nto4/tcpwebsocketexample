import socket

HOST, PORT = "localhost", 5000
while True:
    # creta tcp socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        data = input("Hangi takımı tutuyorsun ?  \n")

        # connect server
        sock.connect((HOST, PORT))
        
        # send request
        sock.sendall(bytes(data + "\n", "utf-8"))

        # receive response
        received = str(sock.recv(1024), "utf-8")

    print("Received: " + received)