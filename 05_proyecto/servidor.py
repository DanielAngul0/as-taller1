# Librerias importadas
import socket
import threading

# Dirección y puerto donde escuchará el servidor
HOST = 'localhost'
PORT = 9000

# Lista clientes conectados
clients = []

# Función para reenviar un mensaje a todos menos al emisor
def broadcast(message: bytes, sender: socket.socket):
    for client in clients:
        if client is not sender:
            try:
                client.sendall(message)
            except:
                pass

# Función que maneja a cada cliente en un hilo separado
def handle_client(client_sock: socket.socket, addr):
    # Bucle de recepción
    while True:
        try:
            data = client_sock.recv(1024)
            if not data:
                break
            # Reenvía el dato a todos
            broadcast(data, client_sock)
        except:
            break

    # Limpieza al desconectar
    clients.remove(client_sock)
    client_sock.close()



# ** --- Configuracion del servidor --- **

# Crear socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar socket a HOST:PORT
server.bind((HOST, PORT))

# Poner socket en modo escucha
server.listen()
print(f"# Servidor escuchando en {HOST}:{PORT}")



# Bucle principal: aceptar conexiones y lanzar hilos
while True:
    
    # Esperar a que un cliente se conecte
    client_sock, addr = server.accept()
    # Añadimos este cliente nuevo a la lista de clientes
    clients.append(client_sock)
    # Mostrar en consola la IP del cliente
    print(f"# Cliente conectado desde {addr}")



    # ** --- Creando hilo para atender a los clientes  --- **
    
    hilo = threading.Thread(target=handle_client, args=(client_sock, addr), daemon=True)
    # El hilo comenzara a actuar
    hilo.start()