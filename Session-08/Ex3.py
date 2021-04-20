import socket

PORT = 8081
IP = "192.168.1.18"

while True:
    message = input("Message to send: ")
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((IP, PORT))
    socket.send(str.encode(message))
    socket.close()
