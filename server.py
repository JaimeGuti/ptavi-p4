#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


PORT = int(sys.argv[1])


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    clients = {}

    def handle(self):

        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        line = self.rfile.read()
        if line.decode('utf-8').split(' ')[0] == 'REGISTER':
            name_client = line.decode('utf-8').split(' ')[1][4:]
            self.clients[name_client] = self.client_address[0]
        print(line.decode('utf-8'))
        print(self.clients)

if __name__ == "__main__":
    # Listens at localhost ('') port 6001
    # and calls the SIPRegisterHandler class to manage the request
    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
