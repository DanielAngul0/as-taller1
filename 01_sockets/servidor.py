# Importando Sockets
import socket

HOST = 'localhost'
PORT = 9000

# Creando el servidor/canal de comunicacion
servidor = socket.socket(socket.AF_INET, socket.SOCK:STERAM)
servidor.bind((HOST, PORT))

# El servidor esta en modo escucha
servidor.listen
print("El servidor esta a la espera de conexiones...")

cliente, direccion = servidor.accept()
print(f"Un cliente se conecto desde la {direccion}")

# Recibiendo los datos
datos = cliente.recv(1024)