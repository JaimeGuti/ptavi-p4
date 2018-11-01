#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import json
import time


PORT = int(sys.argv[1])


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    clients = {}

    def handle(self):

        self.json2registered()
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        line = self.rfile.read()
        exp = float(line.decode('utf-8').split()[-1])
        tm = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + exp))
        info = {"address": self.client_address[0], "expires": tm}
        if line.decode('utf-8').split(' ')[0] == 'REGISTER':
            name_client = line.decode('utf-8').split(' ')[1][4:]
            self.clients[name_client] = info
            self.register2json()
            if line.decode('utf-8').split(' ')[3][-1] == 'Expires':
                expires = int(line.decode('utf-8').split(' ')[-1])
                if str(expires) == '0':
                    del self.clients[name_client]
                    print(b"SIP/2.0 200 OK\r\n\r\n")
        print(line.decode('utf-8'))
        print(self.clients)

    def register2json(self):
        # Creación del fichero .json
        json_file = open('registered.json', 'w')
        json.dump(self.clients, json_file)

    def json2registered(self):
        # Comprobación del fichero .json
        try:
            json_file = open('registered.json')
            self.clients = json.load(json_file)
        except:
            self.register2json()


if __name__ == "__main__":
    # Listens at localhost ('') port 6001
    # and calls the SIPRegisterHandler class to manage the request
    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
