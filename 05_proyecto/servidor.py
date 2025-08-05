# Librerias importadas
import socket
import threading

# Dirección y puerto donde escuchará el servidor
HOST = 'localhost'
PORT = 9000

# Mapea cada cliente a su nombre y sala actual
clients = {}          # socket -> {'name': str, 'room': str}
# Mapea cada sala a la lista de sockets que están dentro
rooms = {'Lobby': []}

# Función para enviar un mensaje solo a los miembros de una sala
def broadcast_room(message: str, room: str, exclude_sock=None):
    data = message.encode()
    for sock in rooms.get(room, []):
        if sock is not exclude_sock:
            try:
                sock.sendall(data)
            except:
                pass

# Función que maneja a cada cliente en un hilo separado
def handle_client(client_sock: socket.socket):
    # Recibir y registrar nombre de usuario
    name = client_sock.recv(1024).decode().strip()
    clients[client_sock] = {'name': name, 'room': 'Lobby'}
    rooms['Lobby'].append(client_sock)

    # Notificar en Lobby
    broadcast_room(f"» {name} se ha unido a Lobby", 'Lobby', exclude_sock=client_sock)
    client_sock.sendall("» Bienvenido a Lobby. Usa /join <sala> para cambiar de sala.".encode())
    
    # Bucle de recepción de mensajes
    while True:
        try:
            data = client_sock.recv(1024)
            if not data:
                break
            text = data.decode().strip()
            current_room = clients[client_sock]['room']

            # Comando: /join <sala>
            if text.startswith('/join '):
                new_room = text.split(' ', 1)[1]
                old_room = current_room

                # Salir de la sala actual
                rooms[old_room].remove(client_sock)
                broadcast_room(f"« {name} ha dejado {old_room}", old_room)

                # Entrar o crear la nueva sala
                rooms.setdefault(new_room, []).append(client_sock)
                clients[client_sock]['room'] = new_room
                client_sock.sendall(f"» Has entrado en {new_room}".encode())
                broadcast_room(f"» {name} se ha unido a {new_room}", new_room, exclude_sock=client_sock)
                continue

            # Mensaje normal: reenviar solo dentro de la sala actual
            broadcast_room(f"[{name}] {text}", current_room, exclude_sock=client_sock)

        except ConnectionResetError:
            break

    # Limpieza al desconectar
    room = clients[client_sock]['room']
    rooms[room].remove(client_sock)
    broadcast_room(f"« {name} se ha desconectado", room)
    del clients[client_sock]
    client_sock.close()



# ** --- Punto de entrada del servidor --- **

def main():
    
    # Crear socket TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enlazar socket a HOST:PORT
    server.bind((HOST, PORT))

    # Poner socket en modo escucha
    server.listen()
    print(f"# Servidor escuchando en {HOST}:{PORT}")

    # Bucle principal: aceptar conexiones y lanzar hilos
    while True:
        client_sock, _ = server.accept()
        threading.Thread(target=handle_client, args=(client_sock,), daemon=True).start()
        

if __name__ == '__main__':
    main()