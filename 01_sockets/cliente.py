# Importando la libreria Socket
import socket

# Definiendo la maquina HOST
HOST = 'localhost' # IP
# Elegimos un puerto superior a 1024 pues hasta este puerto todos estan reservados
PORT = 9000 # Puerto

# Abre el Socket para conectarse con uno que ya este abierto
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectamos nuestro cliente a la IP: 'localhost' y al puerto: '9000'
cliente.connect((HOST, PORT)) # Despues de esto, tanto el servidor como el cliente se cambiaran de puerto(ej: 65000), para que el puerto 9000 del servidor quede abierto para otra conexion

# Enviando datos al servidor
cliente.sendall(b"Mundo!") # Los datos que se mandan atrevés de un Socket deben ser binario, no String

# Recibiendo la respuesta del servidor
# El Buffer es una memoria temporal en donde almacena los datos antes de leerlos o enviarlos
respuesta = cliente.recv(1024) # Esto leera hasta 1024 bytes / 1 kilobyte, los textos simples en inglés (ASCII) ocupan 1 byte por carácter

# Mostramos la respuesta del servidor
print(f"Respuesta: {respuesta}")

# Cierra la conexion con el servidor
cliente.close()