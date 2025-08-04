# Importando la libreria Socket
import socket

# Definiendo la maquina HOST
HOST = 'localhost' # IP
# Elegimos un puerto superior a 1024 pues hasta este puerto todos estan reservados
PORT = 9000 # Puerto

# Recibira el mensaje digitado por el cliente
mensaje = input("Digite su mensaje: ")

# Abre el Socket para conectarse con uno que ya este abierto
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectamos nuestro cliente a la IP: 'localhost' y al puerto: '9000'
cliente.connect((HOST, PORT))

# Enviando datos al servidor
cliente.sendall(mensaje.encode()) # Dado que el Socket solo recibe binario, '.encode()' codifica el mensaje/dato de String a binario para que este sea recibido
print(f"Mensaje enviado: '{mensaje}'")

# Recibiendo los datos del cliente
respuesta = cliente.recv(1024)
print(f"Respuesta del 'Echo': '{respuesta.decode()}'") # Cuando se le vaya a responder al cliente, '.decode()' decodifica el mensaje para que este pase de binaio a String

# Cierra la conexion con el cliente
cliente.close()
