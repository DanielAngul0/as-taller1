# Importando la libreria Socket
import socket

# Definiendo la maquina HOST
HOST = 'localhost' # IP
# Elegimos un puerto superior a 1024 pues hasta este puerto todos estan reservados
PORT = 9000 # Puerto

# Creando el servidor/canal de comunicacion
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Con esto asociamos nuestro servidor a la IP: 'localhost' y al puerto: '9000'
servidor.bind((HOST, PORT))

# El servidor esta a la escucha
servidor.listen()
print("El servidor esta a la espera de conexiones...")

# Si un cliente se conecta, poder saber quien es el cliente y cual es su direccion
cliente, direccion = servidor.accept() # Con 'servidor.accept()' espera las conexiones 
print(f"El cliente {cliente} se conecto desde la direccion {direccion}")

# Recibiendo los datos del cliente
# El Buffer es una memoria temporal en donde almacena los datos antes de leerlos o enviarlos
datos = cliente.recv(1024) # Esto leera hasta 1024 bytes / 1 kilobyte, los textos simples en inglés (ASCII) ocupan 1 byte por carácter

# Respondiendo al cliente
# Los sockets trabajan con binarios, así que todo lo que se envía o recibe debe ser codificado/decodificadoe
cliente.sendall(b"Hola! " + datos) # Los datos que se mandan atrevés de un Socket deben ser binario, no String

# Cierra la conexion con el cliente
cliente.close()