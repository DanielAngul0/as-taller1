# Importar librería de sockets
import socket

# Dirección y puerto donde escuchará el servidor
HOST = 'localhost'
PORT = 9000

# Crear socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar socket a HOST:PORT
server.bind((HOST, PORT))

# Poner socket en modo escucha
server.listen()
print("# Escuchando conexiones en", HOST, PORT)

# Bucle principal: aceptar y cerrar conexión
while True:
    # Esperar a que un cliente se conecte
    client_sock, addr = server.accept()
    # Mostrar en consola la IP del cliente
    print(f"# Conexión recibida de {addr}")
    
    # Recibir hasta 1024 bytes (se espera “ping”)
    data = client_sock.recv(1024)
    mensaje = data.decode().strip()
    print(f"# Mensaje recibido: {mensaje}")
    
    # Si el mensaje es “ping”, responder “pong”
    if mensaje.lower() == "ping":
        client_sock.sendall(b"pong")
        print("# Enviado: pong")
    
    # Cerrar la conexión
    client_sock.close()
    print("# Conexión cerrada con", addr)
