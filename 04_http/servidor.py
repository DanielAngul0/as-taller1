# Importamos socket
import socket
# http.server es el módulo estándar de Python para crear servidores HTTP básicos
import http.server

# Asignamos el IP de la maquina HOST y asignamos un puerto ≥ 1024
# Define que el servidor escuchará sólo en la interfaz local (127.0.0.1) y en el puerto 9000
HOST = 'localhost'
PORT = 9000

# Heredamos de SimpleHTTPRequestHandler
class Servidor(http.server.SimpleHTTPRequestHandler):
    pass

# Se crea el socket, se liga a localhost:9000 y arranca el manejador de peticiones definido en Servidor
servidor = http.server.HTTPServer((HOST, PORT), Servidor)
# Entra en un bucle infinito, aceptando conexiones HTTP.
servidor.serve_forever()