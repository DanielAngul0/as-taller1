# Importar librería de sockets
import socket

# Dirección y puerto del servidor al que conectarse
HOST = 'localhost'
PORT = 9000

# Crear socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
client.connect((HOST, PORT))
print(f"# Conectado a {HOST}:{PORT}")

# Cerrar la conexión inmediatamente
client.close()
print("# Conexión cerrada")
