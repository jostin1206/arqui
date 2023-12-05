import socket 

from threading import Thread

stock = {"lavadora": 5, "refrigerador": 3, "aspiradora": 2, "licuadora": 4}
def conexion_cliente(c_socket):
    while True:
        ##recibimos la info del cliente - c_socket
        info = c_socket.recv(1024).decode()
        if stock[info] > 0: ##si el producto esta en stock
            c_socket.sendall('1'.encode())
            stock[info] -= 1
            ##print(stock)
        else:
            c_socket.sendall('0'.encode())

def server():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar (unir) el socket al host y puerto
    s.bind(('localhost', 12345))

    s.listen(1)

    while True:

        ##aceptamos la conexion entrante
        c_socket , c_add = s.accept()

        ##creamos hilos 
        thread = Thread(target=conexion_cliente, args=(c_socket,))
        thread.start()

if __name__ == "__main__":
    server()



