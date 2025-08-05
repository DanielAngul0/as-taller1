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

# Diccionario de comandos y sus descripciones
COMMANDS = {
    '/join <sala>': 'Cambiarte a la sala indicada (la crea si no existe).',
    '/users':       'Lista los usuarios en tu sala actual.',
    '/rooms':       'Lista todas las salas disponibles.',
    '/help':        'Muestra esta lista de comandos.'
}

# Función para enviar un mensaje solo a los miembros de una sala
def broadcast_room(message: str, room: str, exclude_sock=None):
    data = message.encode()
    for sock in rooms.get(room, []):
        if sock is not exclude_sock:
            try:
                sock.sendall(data)
            except:
                pass

# Función para enviar la lista de comandos a un cliente
def send_help(sock):
    lines = ["» Comandos disponibles:"]
    for cmd, desc in COMMANDS.items():
        lines.append(f"   {cmd:<15} — {desc}")
    sock.sendall(("\n".join(lines)).encode())
    print(f"[SERVER] Enviado /help a {sock.getpeername()}")

# Función que gestiona a cada cliente en un hilo
def handle_client(client_sock: socket.socket):
    # Recibir y registrar nombre de usuario
    name = client_sock.recv(1024).decode().strip()
    clients[client_sock] = {'name': name, 'room': 'Lobby'}
    rooms['Lobby'].append(client_sock)
    print(f"[SERVER] {name} conectado en Lobby")

    # Aviso de bienvenida
    broadcast_room(f"» {name} se ha unido a Lobby", 'Lobby', exclude_sock=client_sock)
    client_sock.sendall(
        "» Bienvenido a Lobby.\n"
        "  Usa /join <sala> para cambiar.\n"
        "  Usa /users  para ver participantes.\n"
        "  Usa /rooms  para ver salas.\n"
        "  Usa /help   para ver comandos.\n"
        .encode()
    )
    
    # Bucle de recepción de mensajes
    while True:
        try:
            data = client_sock.recv(1024)
            if not data:
                break
            text = data.decode().strip()
            room = clients[client_sock]['room']
            
            # Comando: /help
            if text in ('/help', '/commands'):
                print(f"[SERVER] {name} solicitó /help")
                send_help(client_sock)
                continue

            # Comando: /join <sala>
            if text.startswith('/join '):
                new_room = text.split(' ', 1)[1]
                print(f"[SERVER] {name} abandona {room}")
                rooms[room].remove(client_sock)
                broadcast_room(f"« {name} ha dejado {room}", room)

                rooms.setdefault(new_room, []).append(client_sock)
                clients[client_sock]['room'] = new_room
                print(f"[SERVER] {name} entra en {new_room}")
                client_sock.sendall(f"» Has entrado en {new_room}".encode())
                broadcast_room(f"» {name} se ha unido a {new_room}", new_room, exclude_sock=client_sock)
                continue
            
            # Comando: /users
            if text == '/users':
                participants = [clients[s]['name'] for s in rooms.get(room, [])]
                print(f"[SERVER] {name} solicitó /users en {room}")
                client_sock.sendall(f"» Usuarios en {room}: {', '.join(participants)}".encode())
                continue

            #Comando: /rooms
            if text == '/rooms':
                salas = list(rooms.keys())
                print(f"[SERVER] {name} solicitó /rooms")
                client_sock.sendall(f"» Salas disponibles: {', '.join(salas)}".encode())
                continue

            # Mensaje normal: reenviar solo dentro de la sala actual
            print(f"[SERVER] {name} en {room}: {text}")
            broadcast_room(f"[{name}] {text}", room, exclude_sock=client_sock)

        except ConnectionResetError:
            break

    # Limpieza al desconectar
    room = clients[client_sock]['room']
    rooms[room].remove(client_sock)
    broadcast_room(f"« {name} se ha desconectado", room)
    print(f"[SERVER] {name} desconectado de {room}")
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