import socket
import numpy 
def calcular_promedio(notas):

   # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   # s.bind(('localhost',12345))
   # s.listen(1)

    practicas = []
    for i in range (4):
        practicas.append(int(notas[i]))

    laboratorios = []
    for i in range (4,14):
        laboratorios.append(int(notas[i]))
    
    ta = int(notas[14])

    practicas.remove(min(practicas))
    laboratorios.remove(min(laboratorios))
    laboratorios.remove(min(laboratorios))

    #calculamos promedio de acuerdo a la siguientes formulas
    suma = 0
    for nota in practicas:
        suma += nota
    
    Pa = suma / len(practicas)

    suma2 = 0
    for nota in laboratorios:
        suma2 += nota
    
    Pb = suma2 / len(laboratorios)

    nota = (3*Pa + 3*Pb + 4*ta)/10

    return nota

def server():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost',12345))
    s.listen(1)

    while True:

        client_conn, client_addr = s.accept()
        dato = client_conn.recv(1024)
        mt = dato.decode()

        notas = mt.split(",")

        promedio_final = calcular_promedio(notas)

        client_conn.sendall(str(promedio_final).encode())

        client_conn.close()
if __name__ == "__main__":
    
    server()