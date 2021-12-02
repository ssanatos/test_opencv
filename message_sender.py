import socket

sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
while True:
    msg = input()
    sender.sendto(str.encode(msg),('192.168.16.26', 7778))

