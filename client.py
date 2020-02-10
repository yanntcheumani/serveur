# coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("", 1706))

r = s.recv(255)
print("Marta: %s" % (r.decode()))
message = input("user ")
s.send(message.encode())

while message != "exit":
    r = s.recv(255)
    print("Marta: %s" % (r.decode()))
    message = input("user: ")
    s.send(message.encode())
