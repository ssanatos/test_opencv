import socket

receiver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
receiver.binder('192.168.16.26', 7778)

while True:
    bytepair = receiver.recvfrom(1024)

    message = bytepair[0]
    address = bytepair[1]

    print(message, ':현호PC ', address)
