import socket

def client():

    ##leer el archivo CSV y extraer las notas como una cadena de texto
    with open('notas.csv','r') as f:
        notas = f.read()

    ##dividir la cadena de ttexto en una lista de notas
    notas_lista = notas.split(',')

    ##crear un socket y conectarse al servidor
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost",12345))
    ##s.bind(("localhost",12345))  # SOLO SE USA EN EL SERVIDOR

    ##enviar las notas al servidor como una cadena de texto
    s.sendall(','.join(notas_lista).encode())

    ##recibir el promedio final del servidor
    promedio_final = s.recv(1024).decode()

    print("Promedio final: ",promedio_final)

    s.close()
if __name__ == "__main__":
    client()
