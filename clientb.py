import socket

#creamos un socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#conecta al servidor
server_address = ('localhost',10000)
sock.connect(server_address)

while True:
    #envia un mensaje al  servidor
    message = input('Escribe un mensaje para el servidor: ')
    sock.sendall(message.encode('utf-8'))

    #recibe un mensaje del servidor
    message = sock.recv(1024)
    print(f'Mensaje del servidor: {message}')

#cierra el socket
sock.close()

