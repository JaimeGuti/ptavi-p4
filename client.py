#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar
SERVER = sys.argv[1]
PORT = int(sys.argv[2])
LINE = " ".join(sys.argv[4:])
REGISTRO = sys.argv[3].upper()

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando:", REGISTRO, 'sip:', LINE, 'SIP/2.0\r\n\r\n')
    Rg = bytes(REGISTRO, 'utf-8')
    Ln = bytes(LINE, 'utf-8')
    my_socket.send(Rg + b' sip ' + Ln + b' SIP/2.0\r\n\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
