#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar
try:
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    LINE = " ".join(sys.argv[4:-1])
    REGISTRO = sys.argv[3].upper()
    EXPIRES = sys.argv[5]

    # Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        my_socket.connect((SERVER, PORT))
        print("Enviando:", REGISTRO, 'sip:', LINE, 'SIP/2.0\r\n\r\n')
        Rg = bytes(REGISTRO, 'utf-8')
        Ln = bytes(LINE, 'utf-8')
        Ex = bytes(EXPIRES, 'utf-8')
        Send_1 = Rg + b' sip:' + Ln + b' SIP/2.0\r\n\r\n'
        my_socket.send(Send_1 + b'Expires: ' + Ex + b'\r\n\r\n')
        #my_socket.send()
        data = my_socket.recv(1024)
        print('Recibido -- ', data.decode('utf-8'))
        print("Socket terminado.")
except:
    sys.exit("Usage: client.py ip puerto register sip_address expires_value")
