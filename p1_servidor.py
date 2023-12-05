
import socket

import math

host = '127.0.0.1'
port = 12345


def factorial(x):

    return math.factorial(x)

def inicio_servidor():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ##enlazar(unir) el socket al host y puerto
    server_socket.bind((host, port))

    server_socket.listen(1)

    print(f"Servidor iniciando en {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexion entrante desde {client_address}")
        data = client_socket.recv(1024) ###recibe datos del cliente

        if not data:
            break
        
        n = int(data.decode())
        rs = factorial(n)
        

        client_socket.send(f'{rs}'.encode())

        client_socket.close()


    server_socket.close()

if __name__ == "__main__":
    inicio_servidor()

