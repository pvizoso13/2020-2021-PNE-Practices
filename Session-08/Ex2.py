import socket

PORT = 8080
IP = "192.168.1.18"

while True:
    message = input("Message to send: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(message))
    s.close()
