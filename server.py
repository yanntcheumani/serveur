# coding: utf-8

import socket
import threading
import datetime
import colorama as color
from Marta import Marta

color.init(True)
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("", 1706))


class ClientThread(threading.Thread):

    def __init__(self, ip, port, client_socket):
        color.init()
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.client_socket = client_socket
        self.dates = str(datetime.datetime.today()) + color.Style.RESET_ALL
        self.marta = Marta()
        print("%s [+] Nouveau thread pour %s\n" % (color.Fore.GREEN + self.dates, self.ip))

    def login
    def run(self):
        self.client_socket.send("bonjour quel est votre Prénom".encode())
        r = self.client_socket.recv(255)
        while r.decode().find("exit"):
            if r.decode() == "Morpion":
                print("%s [+] l'utilisateur %s c'est lancer une parti de morpion: %s" % (color.Fore.GREEN + self.dates, self.ip, r.decode()))
                self.client_socket.send("voulez vouez lancer une partie de morpion ?".encode())
            self.client_socket.send(self.marta.get_message(r))
            r = self.client_socket.recv(255)
        self.client_socket.close()
        print("%s [-] l'utilisateur %s c'est déconnecter" % (color.Fore.RED + self.dates, self.ip))

while True:
    tcpsock.listen(10)
    print("En écoute...")
    (client_socket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, client_socket)
    newthread.start()
