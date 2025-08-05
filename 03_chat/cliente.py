# Importando la libreria Socket
import socket
# Importamos 'threading' para manejar hilos para las conexiones de los clientes
# Usamos un hilo para no bloquear la consola mientras escuchamos mensajes entrantes
import threading 

# Asignamos el IP de la maquina HOST y asignamos un puerto ≥ 1024
HOST = 'localhost'
PORT = 9000 

# Creamos la funcion para recibir mensajes
def recibir_mensajes():
    # Siempre estara activo para recibir cualquier mensaje
    while True:
        # Recibira un mensaje decodificado por parte del servidor
        mensaje = cliente.recv(1024).decode()
        print(mensaje)

# Solicitamos el nombre al cliente
nombre = input("Cual es tu nombre: ")

# Abre el Socket para conectarse con uno que ya este abierto
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectamos nuestro cliente a la IP: 'localhost' y al puerto: '9000'
cliente.connect((HOST, PORT))

# Enviando el nombre del cliente al servidor antes de entrar al chat
cliente.send(nombre.encode())


# *--- Creando Hilo para recibir mensajes ---*

# Este hilo esperara para recibir mensajes
hilo_recibir = threading.Thread(target=recibir_mensajes)
# El hilo comenzara a actuar
hilo_recibir.start()

# Mientras siempre estara activo para enviar mensajes codificados al servidor
while True:
    mensaje = input("Mensaje: ")
    cliente.send(mensaje.encode())