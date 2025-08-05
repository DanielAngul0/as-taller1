# Importamos socket
import socket
# Con threading haremos multiples tareas al tiempo en las cuales normalmente el programa se quedaria bloqueado
# Importamos 'threading' para manejar hilos para las conexiones individuales de los clientes
import threading

# Asignamos el IP de la maquina HOST y asignamos un puerto ≥ 1024
HOST = 'localhost'
PORT = 9000

# Creamos una lista en la que se almacenaran todos los clientes
clientes = []
  
# Creamos una funcion para manejar cada cliente por separado
# Solicitamos saber el socket del cliente y el nombre del cliente
def atender_cliente(cliente, nombre):
    # Bucle que mantiene viva la escucha de mensajes de este cliente
    while True:
        # 'try' manejara los errores para que si ocurre un imprevisto en la conexion active 'except ConnectionResetError' y cierre la conexion del cliente
        try:
            # Recibiendo los datos del cliente
            mensaje = cliente.recv(1024)
            #  Detecta el fin de la conexión
            if not mensaje:
                break
            # Mostrara el nombre del cliente, junto a su mensaje ya decodificado
            print(f"{nombre}: {mensaje.decode()} ")
            # Enviara el mensaje a cualquiera que este en el chat
            broadcast(mensaje.decode(), cliente)
        # Si existe un error en la conexion o el cliente se desconecta de forma brusca, elimina el socket de la lista y cierra su conexión.
        except ConnectionResetError: 
            clientes.remove(cliente) # Elimina este cliente de la lista de cliente
            cliente.close() # Termina la conexion con el cliente
            break

# Creamos el metodo 'broadcast'
# Leera el mensaje asi como tambien vera quien fue el que lo envio
def broadcast(mensaje, emisor):
    # Recorrera todos los clientes de la lista
    for cliente in clientes:
        # Cualquier cliente que sea diferente al emisor, recibira el mensaje del emisor decodificado
        if cliente != emisor:
            cliente.send(mensaje.encode())

# Creando el canal de comunicacion
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Asociamos nuestro servidor a la IP: 'localhost' y al puerto: '9000'
servidor.bind((HOST, PORT))
# El servidor esta a la escucha
servidor.listen()
print("El servidor 'Chat' esta esperando conexiones...")

while True:
    # Si un cliente se conecta, poder saber quien es el cliente y cual es su direccion
    cliente, direccion = servidor.accept()
    print(f"Se conecto un cliente desde la IP {direccion}")
    # Le preguntaremos el nombre al cliente
    nombre = cliente.recv(1024).decode()
    # Añadimos este cliente nuevo a la lista de clientes
    clientes.append(cliente)
    # Llamaremos a la funcion 'broadcast' y avisaremos a todos los del chat que un nuevo usuario se ha unido
    broadcast(f"{nombre} se ha unido al 'Chat'", cliente)
    
    
    # *--- Creando Hilo para atender ---*
    
    # Este hilo atendera a un cliente en especifico, uno por uno
    hilo_cliente = threading.Thread(target=atender_cliente, args=(cliente, nombre))
    # El hilo comenzara a actuar
    hilo_cliente.start()