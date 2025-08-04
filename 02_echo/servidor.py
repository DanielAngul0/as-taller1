# El protocolo Echo recibe un mensaje, y eso mismo que recibio lo envia

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

# El servidor nunca se cerrara, siempre estara recibiendo y respondiendo a las peticiones
while True:
    
    # El servidor esta a la escucha
    print("El servidor 'Echo' esta esperando conexiones...")

    # Si un cliente se conecta, el servidor sabra cual es su IP y su Puerto designado
    cliente, direccion = servidor.accept() 
    print(f"Un cliente se conecto desde la direccion {direccion}")

    # Recibiendo los datos del cliente
    datos = cliente.recv(1024)

    # Si no hay datos recibidos de parte del cliente, volvera a estar a la escucha esperando conexiones
    if not datos:
        break
    
    # Mostrara los datos recibidos
    print("Datos recibidos: ", datos)
    
    # Respondiendo al cliente con los mismos datos recibidos por el cliente
    cliente.sendall(datos)

    # Cierra la conexion con el cliente
    cliente.close()
