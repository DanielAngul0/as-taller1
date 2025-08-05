# Librerias importadas
import socket
import threading

# Dirección y puerto donde escuchará el servidor
HOST = 'localhost'
PORT = 9000

# Mapea cada cliente a su nombre y sala actual
clientes = {}          # socket -> {'nombre': str, 'sala': str}
# Mapea cada sala a la lista de sockets que están dentro
salas = {'Lobby': []}

# Diccionario de comandos y sus descripciones
COMANDOS = {
    '/unirse nombre_sala': 'Cambiarte a la sala indicada (la crea si no existe).',
    '/usuarios':      'Lista los usuarios en tu sala actual.',
    '/salas':         'Lista todas las salas disponibles.',
    '/ayuda':         'Muestra esta lista de comandos.'
}

# Función para enviar un mensaje solo a los miembros de una sala
def difundir_sala(mensaje: str, sala: str, exclude_socket=None):
    dato = mensaje.encode()
    for sock in salas.get(sala, []):
        if sock is not exclude_socket:
            try:
                sock.sendall(dato)
            except:
                pass

# Función para enviar la lista de comandos a un cliente
def solicitar_ayuda(socket_cliente):
    lineas = ["» Comandos disponibles:"]
    for cmd, desc in COMANDOS.items():
        lineas.append(f"   {cmd:<15} — {desc}")
    socket_cliente.sendall(("\n".join(lineas)).encode())
    print(f"[SERVIDOR] Enviado /ayuda a {socket_cliente.getpeername()}")

# Función que gestiona a cada cliente en un hilo
def manejar_cliente(socket_cliente: socket.socket):
    # Recibir y registrar nombre de usuario
    nombre = socket_cliente.recv(1024).decode().strip()
    clientes[socket_cliente] = {'nombre': nombre, 'sala': 'Lobby'}
    salas['Lobby'].append(socket_cliente)
    print(f"[SERVIDOR] {nombre} conectado en Lobby")

    # Aviso de bienvenida
    difundir_sala(f"» {nombre} se ha unido a Lobby", 'Lobby', exclude_socket=socket_cliente)
    socket_cliente.sendall(
            "» Bienvenido a Lobby.\n"
            "  Usa /unirse nombre_sala para crear o para cambiarte a una sala.\n"
            "  Usa /usuarios  para ver participantes.\n"
            "  Usa /salas     para ver salas.\n"
            "  Usa /ayuda     para ver comandos.\n"
            .encode()
        )
        
        # Bucle de recepción de mensajes
    while True:
            try:
                dato = socket_cliente.recv(1024)
                if not dato:
                    break
                texto = dato.decode().strip()
                sala_actual = clientes[socket_cliente]['sala']
                
                # Comando: /ayuda
                if texto in ('/ayuda', '/comandos'):
                    print(f"[SERVIDOR] {nombre} solicitó /ayuda")
                    solicitar_ayuda(socket_cliente)
                    continue
                
                # Comando: /unirse <sala>
                if texto.startswith('/unirse '):
                    nueva_sala = texto.split(' ', 1)[1]
                    print(f"[SERVIDOR] {nombre} abandona {sala_actual}")
                    salas[sala_actual].remove(socket_cliente)
                    difundir_sala(f"« {nombre} ha dejado {sala_actual}", sala_actual)
    
                    salas.setdefault(nueva_sala, []).append(socket_cliente)
                    clientes[socket_cliente]['sala'] = nueva_sala
                    print(f"[SERVIDOR] {nombre} entra en {nueva_sala}")
                    socket_cliente.sendall(f"» Has entrado en {nueva_sala}".encode())
                    difundir_sala(f"» {nombre} se ha unido a {nueva_sala}", nueva_sala, exclude_socket=socket_cliente)
                    continue
                
                # Comando: /usuarios
                if texto == '/usuarios':
                    participantes = [clientes[s]['nombre'] for s in salas.get(sala_actual, [])]
                    print(f"[SERVIDOR] {nombre} solicitó /usuarios en {sala_actual}")
                    socket_cliente.sendall(f"» Usuarios en {sala_actual}: {', '.join(participantes)}".encode())
                    continue
                
                # Comando: /salas
                if texto == '/salas':
                    lista_salas = list(salas.keys())
                    print(f"[SERVIDOR] {nombre} solicitó /salas")
                    socket_cliente.sendall(f"» Salas disponibles: {', '.join(lista_salas)}".encode())
                    continue
                
                # Mensaje normal: reenviar solo dentro de la sala actual
                print(f"[SERVIDOR] {nombre} en {sala_actual}: {texto}")
                difundir_sala(f"[{nombre}] {texto}", sala_actual, exclude_socket=socket_cliente)
    
            except ConnectionResetError:
                break
            
    # Limpieza al desconectar
    sala_actual = clientes[socket_cliente]['sala']
    salas[sala_actual].remove(socket_cliente)
    difundir_sala(f"« {nombre} se ha desconectado", sala_actual)
    print(f"[SERVIDOR] {nombre} desconectado de {sala_actual}")
    del clientes[socket_cliente]
    socket_cliente.close()
    
    
# ** --- Punto de entrada del servidor --- **

def main():
    # Crear socket TCP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enlazar socket a HOST:PORT
    servidor.bind((HOST, PORT))

    # Poner socket en modo escucha
    servidor.listen()
    print(f"# Servidor escuchando en {HOST}:{PORT}")

    # Bucle principal: aceptar conexiones y lanzar hilos
    while True:
        socket_cliente, _ = servidor.accept()
        threading.Thread(target=manejar_cliente, args=(socket_cliente,), daemon=True).start()

if __name__ == '__main__':
    main()
