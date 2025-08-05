# Librerias importadas
import socket
import threading

# Dirección y puerto del servidor al que conectarse
HOST = 'localhost'
PORT = 9000

# Función que corre en un hilo: recibe y muestra mensajes del servidor
def bucle_recepcion(socket_cliente):
    while True:
        try:
            datos = socket_cliente.recv(1024)
            if not datos:
                print("# Desconectado del servidor")
                break
            print(datos.decode())
        except:
            break

# Punto de entrada del cliente
def main():
    # Pedir nombre de usuario
    nombre = input("Tu nombre: ").strip()
    # Crear socket TCP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conectar al servidor
    cliente_socket.connect((HOST, PORT))
    print(f"# Conectado a {HOST}:{PORT}")

    # Enviar nombre al servidor
    cliente_socket.sendall(nombre.encode())
    
    # Iniciar hilo de recepción de mensajes
    hilo_recepcion = threading.Thread(target=bucle_recepcion, args=(cliente_socket,), daemon=True)
    hilo_recepcion.start()

    # Bucle principal: enviar lo que el usuario teclee
    while True:
        texto = input().strip()
        if not texto:
            continue
        cliente_socket.sendall(texto.encode())

if __name__ == '__main__':
    main()
