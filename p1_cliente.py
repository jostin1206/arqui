import socket

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost",12345))

    while True:

        message = input("Ingrese el nombre del electrodoméstico: ")

        ##enviamos el mensaje al servidor
        s.sendall(message.encode())
        data = s.recv(1024)

        ## respuesta del servidor data.decodeR()
        if data.decode() == '1':
            print('Producto en stock. Pedido procesado.')
        else:
            print('Producto agotado. Pedido no procesado.')

if __name__ == "__main__":
    client()    