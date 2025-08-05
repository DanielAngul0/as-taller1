# Importamos socket
import socket
# http.server es el módulo estándar de Python para crear servidores HTTP básicos
import http.client

# Asignamos el IP de la maquina HOST y asignamos un puerto ≥ 1024
HOST = 'localhost'
PORT = 9000

# Crea un objeto cliente HTTP, el cual sabe como interactuar con el protocolo HTTP con el servidor vinculado al HOST y al PORT
cliente = http.client.HTTPConnection(HOST, PORT)
# Envia Envía una petición HTTP GET para la ruta raiz '/'
cliente.request('GET', '/')

# Espera la respuesta del servidor y la envuelve en un objeto HTTPResponse
respuesta = cliente.getresponse()
# Lee todos los bytes del cuerpo de la respuesta (respuesta.read()) y los decodifica de bytes a texto
datos = respuesta.read().decode()

# Muestra por pantalla el contenido como HTML o el listado de ficheros que el servidor devuelve
print(datos)

# Cierra el socket 
cliente.close()