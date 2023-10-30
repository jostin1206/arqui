import socket

#creamos un socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the sockets to the port
#unir los sockets al puerto
server_address = ('localhost',10000)
sock.bind(server_address)

#escucha por conexiones entrantes
sock.listen(1)

#acepta una conexión entrante
client_socket,client_address = sock.accept()

#RECIBE UN MENSAJE DEL CIENTE
while True:

    message = client_socket.recv(1024)
    print(f'Mensaje del cliente: {message}')


    #ENVIA UN MENSAJE AL CLIENTE
    message = input('Escribe un mensaje para el cliente: ')
    client_socket.sendall(message.encode('utf-8'))

#cierra el socket
client_socket.close()
sock.close()