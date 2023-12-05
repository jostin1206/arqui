import socket

host = '127.0.0.1'
port = 12345


def resultado_factorial(n):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectate al servidor
    client_socket.connect((host, port))

    client_socket.send(f'{n}'.encode())

    rs = client_socket.recv(1024) ##recibe datos del servidor

    print(f"El factorial de {n} es {rs.decode()}")


if __name__ == "__main__":

    n = int(input("Numero: "))
    resultado_factorial(n)

