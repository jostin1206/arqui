#servidor
import socket
import math
host = '127.0.0.1'
port = 12345

def server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ##enlazar(unir) el socket al host y puerto
    server_socket.bind((host, port))

    server_socket.listen(1)

    while True:
        client_socket, client_address = server_socket.accept()
    
        data = client_socket.recv(1024).decode() ###recibe datos del cliente y decodifica

        if not data:
            break

        datos = obtener_datos(data)
            
        client_socket.send(f'{datos}'.encode())

        client_socket.close()


    server_socket.close()

def obtener_datos(n):
    edades = []
    diagnosticos =[]
    with open("pacientes.csv",'r', encoding = 'utf-8') as f:
       
        #saltamos la primera linea que contiene los encabezados
        next(f)

        #leemos cada linea del archivo
        for linea in f:
            #separamos los valores por la coma
            paciente,edad,diagnostico = linea.strip().split(',')

            #agregamos la edad a la lista de edades
            edades.append(int(edad))

            #agregamos el diagnostico a la lista de diagnosticos
            diagnosticos.append(diagnostico)

    sanos = 0
    enfermos = 0
    #for i in range(1,11):
     #   d = diagnosticos[i]
      #  if d == '0':
       #     sanos += 1
       # elif d == '1':
        #    enfermos += 1
    
    for diagnostico in diagnosticos:
        if diagnostico == '0':
            sanos += 1
        elif diagnostico == '1':
            enfermos +=1

    if n == 'a' :
        dato = sum(edades) / len(edades)
        return dato
    
    elif n =='b':
        dato = enfermos
        return dato
    
    elif n =='c':
        dato = sanos
        return dato

    
if __name__ == '__main__':
    server()

