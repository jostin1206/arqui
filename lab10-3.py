import socket
host = '127.0.0.1'
port = 12345

def cliente():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectate al servidor
    client_socket.connect((host, port))

    client_socket.send(n.encode())

    rs = client_socket.recv(1024) ##recibe datos del servidor

    if n == 'a':
        with open('informacion.csv','w') as f:
            f.write(f"Promedio de las edades de los pacientes: {rs}")
    
    elif n == 'b':
        with open('informacion.csv','w') as f:
            f.write(f"numero de pacientes enfermos: {rs}")
    
    if n == 'c':
        with open('informacion.csv','w') as f:
            f.write(f"Numero de pacientes sanos: {rs}")


if __name__ == "__main__":

    n = input("Ingrese una opcion(a,b,c): ")
    cliente()
   