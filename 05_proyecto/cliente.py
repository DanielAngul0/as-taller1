# Librerias importadas
import socket
import threading

# Dirección y puerto del servidor al que conectarse
HOST = 'localhost'
PORT = 9000

# Función que corre en un hilo: recibe y muestra mensajes del servidor
def receive_loop(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("# Desconectado del servidor")
                break
            print(data.decode())
        except:
            break

# Punto de entrada del cliente
def main():
    
    # Pedir nombre de usuario
    nombre = input("Tu nombre: ").strip()
    # Crear socket TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conectar al servidor
    client.connect((HOST, PORT))
    print(f"# Conectado a {HOST}:{PORT}")

    # Enviar nombre al servidor
    client.sendall(nombre.encode())
    
    # Iniciar hilo de recepción de mensajes
    hilo_recv = threading.Thread(target=receive_loop, args=(client,), daemon=True)
    hilo_recv.start()

    # Bucle principal: enviar lo que el usuario teclee
    while True:
        texto = input().strip()
        if not texto:
            continue
        client.sendall(texto.encode())

if __name__ == '__main__':
    main()
