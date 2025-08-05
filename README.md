## Autor
### Estudiante: Daniel Andres Angulo Perez

## [@DanielAngul0](https://github.com/DanielAngul0)

# taller #1 de Arquitectura de Software: Cliente-Servidor

## Descripción

Este proyecto proporciona una plantilla para la implementación de los ejemplos del modelo Cliente/Servidor, según se explican en el vídeo [Programando Cliente/Servidor con Python](https://www.youtube.com/watch?v=kPXa73a0kCA)

## Estructura del Proyecto

```
as-taller1/
├── README.md
├── requirements.txt
├── .gitignore
├── 01_sockets/
│   ├── cliente.py
│   └── servidor.py
├── 02_echo/
│   ├── cliente.py
│   └── servidor.py
├── 03_chat/
│   ├── cliente.py
│   └── servidor.py
├── 04_http/
│   ├── cliente.py
│   └── servidor.py
└── 05_proyecto/
    ├── cliente.py
    └── servidor.py
```

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/UR-CC/as-taller1.git
cd as-taller1

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual en Windows:
venv\Scripts\activate
# Activar entorno virtual en Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## Ejercicios

### 1. Sockets Básicos (Paso de Mensajes)

- **Ubicación**: `01_sockets/`
- **Descripción**: Implementación básica de comunicación cliente-servidor con sockets
- **Características**:
  - _elabora la documentación_
  - ...
  - ...

**Uso**:

```bash
# Terminal 1 - Servidor
python servidor.py

# Terminal 2 - Cliente
python cliente.py
```

### 2. Servidor Echo

- **Ubicación**: `02_echo/`
- **Descripción**: Servidor que devuelve exactamente lo que recibe del cliente
- **Características**:
  - _elabora la documentación_
  - ...
  - ...

**Uso**:

```bash
# Terminal 1 - Servidor
python servidor.py

# Terminal 2 - Cliente
python cliente.py
```

### 3. Chat Multiusuario

- **Ubicación**: `03_chat/`
- **Descripción**: Sistema de chat que permite múltiples usuarios conectados simultáneamente
- **Características**:
  - _elabora la documentación_
  - ...
  - ...

**Uso**:

```bash
# Terminal 1 - Servidor
python servidor.py

# Terminales adicionales - Clientes
python cliente.py
```

### 4. Servidor HTTP Básico

- **Ubicación**: `04_http/`
- **Descripción**: Implementación de un servidor HTTP básico desde cero
- **Características**:
  - _elabora la documentación_
  - ...
  - ...

**Uso**:

```bash
# Servidor HTTP
python server.py

# Acceder desde navegador:
# http://localhost:8080
```

### 5. Proyecto de Chat por Salas (Cliente/Servidor)

## 🗂️ Estructura

- **Ubicación**: `05_proyecto/`
- **Archivos principales**:
  - `servidor.py`: Código del servidor que administra las salas, usuarios y mensajes.
  - `cliente.py`: Código del cliente que permite interactuar con el sistema.

## 🧠 Descripción
Sistema de chat por consola con soporte para múltiples salas, utilizando sockets en Python.

## ⚙️ Características
  - Comunicación en tiempo real entre múltiples clientes.  
- Múltiples salas de chat (se pueden crear y unir con `/unirse nombre_sala`).  
- Listado de usuarios conectados en la sala actual (`/usuarios`).  
- Listado de salas disponibles (`/salas`).  
- Ayuda y comandos disponibles (`/ayuda`).  
- Cada acción relevante (salida, mensajes, etc.) se registra en el servidor.  
- Estructura con hilos para manejo concurrente de clientes.  

**Ejemplo de flujo**:

1) Un usuario ejecuta servidor.py.

2) Otros usuarios ejecutan cliente.py e ingresan su nombre.

3)  Se conectaran a la sala por defecto **Lobby**.

4) Pueden chatear o moverse a otras salas usando comandos.


## 📝 Comandos Disponibles en el Cliente

| Comando              | Descripción                                                        |
|----------------------|---------------------------------------------------------------------|
| `/unirse nombre_sala`     | Cambiarte a la sala indicada (la crea si no existe)                |
| `/usuarios`          | Ver los usuarios en la sala actual                                  |
| `/salas`             | Ver las salas disponibles                                           |
| `/ayuda`             | Ver esta lista de comandos                                          |


###  🛠️ Requisitos

- Python 3.7 o superior (recomendado Python 3.10+)

## 🖥️ Uso

1. Abre una terminal para iniciar el **servidor**:

```bash
# Terminal del servidor
python3 servidor.py
```

2. Abre dos o más terminales adicionales, una por cada **cliente** que desees conectar:

```bash
# Terminal del cliente
python3 cliente.py
```


## Conceptos

#### Modelo Cliente/Servidor

Esta arquitectura es un patrón de diseño de software en el que las tareas se dividen entre los **proveedores de un recurso o servicio** (servidores) y los **solicitantes** de dicho servicio (clientes).

* **El Servidor:** Es un programa que se ejecuta de forma continua, esperando y escuchando solicitudes de los clientes. Puede manejar una o múltiples conexiones, como en el caso del chat multiusuario. Sus responsabilidades incluyen:
   * Gestionar el acceso a recursos compartidos (como la base de datos de un sitio web o los mensajes de un chat).
   * Responder a las solicitudes de los clientes.
   * Autenticar usuarios.

* **El Cliente:** Es un programa que inicia la comunicación y envía solicitudes al servidor. Sus responsabilidades son:
   * Interactuar con el usuario.
   * Enviar solicitudes bien formadas al servidor.
   * Procesar y mostrar la respuesta del servidor.

**Patrones de Interacción:**

* **Modelo de Petición/Respuesta (Request/Response):** Es el patrón más simple. El cliente envía una solicitud al servidor y espera una respuesta antes de hacer otra cosa. El servidor procesa la solicitud y envía la respuesta. El ejemplo del **Servidor Echo** y el **Servidor HTTP Básico** se basan directamente en este patrón.

* **Modelo de Publicador/Suscriptor (Publisher/Subscriber):** En este patrón, el servidor actúa como un "publicador" que envía mensajes a los clientes que se han "suscrito" a un tema de interés. El **Chat Multiusuario** es un ejemplo de este patrón, donde los mensajes de un usuario se "publican" a todos los demás clientes "suscritos" al chat.

#### Red de Computadores

Es un conjunto de equipos y dispositivos interconectados que comparten recursos e información. La conexión puede ser física (como un cable Ethernet) o inalámbrica (Wi-Fi). Los conceptos de **cliente** y **servidor** son fundamentales en este contexto:

  * **Cliente:** Una aplicación que inicia una solicitud a otra computadora (el servidor).
  * **Servidor:** Una aplicación que escucha las solicitudes entrantes y responde a ellas.

#### Protocolos de Red

Es un conjunto de reglas que definen cómo los datos deben ser formateados, transmitidos y recibidos. Para que el cliente y el servidor se entiendan, necesitan hablar el mismo "idioma". Ese idioma es un protocolo. En este proyecto, los protocolos más relevantes son **TCP** y **HTTP**.

   * **TCP (Transmission Control Protocol):** Es un protocolo de transporte que garantiza una comunicación fiable, ordenada y orientada a la conexión. Esto significa que antes de enviar datos, el cliente y el servidor establecen una conexión y, una vez que los datos se envían, TCP verifica que llegaron correctamente y en el orden adecuado. Es ideal para aplicaciones donde no se pueden perder datos, como un chat o la transferencia de archivos.

   * **HTTP (Hypertext Transfer Protocol):** Es un protocolo de aplicación diseñado para la comunicación entre navegadores web (clientes) y servidores web. Se basa en TCP y define cómo los navegadores solicitan páginas web y cómo los servidores responden. En el proyecto, el **Servidor HTTP Básico** implementa una versión simple de este protocolo.

#### Sockets

Es un **punto final** de comunicación en una red. Piensa en un socket como un extremo de una tubería. Cuando un cliente y un servidor se conectan, crean una "tubería" (la conexión) entre sus respectivos sockets para intercambiar datos. En Python, la librería `socket` proporciona las funciones para crear y manipular estos puntos de conexión.

**Proceso Básico del Servidor**:

* `socket()`: Crea un nuevo socket.
* `bind()`: Asocia el socket a una dirección IP y un número de puerto específicos. Esto le dice al sistema operativo que este servidor "escucha" en esa dirección.
* `listen()`: Pone el socket en modo de escucha para aceptar conexiones entrantes.
* `accept()`: Bloquea la ejecución y espera una conexión de un cliente. Cuando llega una conexión, devuelve un nuevo socket para esa conexión específica y la dirección del cliente.

**Proceso Básico del Cliente**:

* `socket()`: Crea un nuevo socket.
* `connect()`: Se conecta al socket del servidor especificado por su dirección IP y puerto.

Los sockers pueden ser creados sobre protocolo TCP o UDP, su elección depende de la necesidad de fiabilidad versus velocidad.

**Sockets TCP (Orientados a la Conexión)**:

* **Características**:

    * **Fiabilidad:** Garantiza que los paquetes de datos lleguen en el orden correcto y sin errores. Si se pierde un paquete, TCP lo reenvía.
    * **Orientación a la conexión:** Establece una conexión persistente (el "handshake" de tres vías) antes de enviar datos y la cierra al finalizar.
    * **Control de flujo:** Evita que un emisor rápido sature a un receptor lento.

* **Casos de uso:** Aplicaciones donde la integridad de los datos es crítica:

    * Navegación web (HTTP).
    * Transferencia de archivos (FTP).
    * Correo electrónico.
    * Chat multiusuario, como el del proyecto, para asegurar que todos los mensajes se entregan.

**Sockets UDP (Sin Conexión)**

* **Características:**

    * **No fiable:** Los paquetes (llamados datagramas) se envían sin establecer una conexión previa. No hay garantía de que lleguen, ni de que lo hagan en el orden correcto.
    * **Sin conexión:** No hay "handshake". El emisor simplemente envía los datos.
    * **Velocidad:** Al no tener la sobrecarga de la fiabilidad, UDP es mucho más rápido.

* **Casos de uso:** Aplicaciones donde la velocidad es más importante que la fiabilidad: 

    * Streaming de video y audio en tiempo real.
    * Videojuegos en línea.
    * Consultas DNS (Domain Name System).

#### Programación Concurrente

Es la capacidad de un sistema para manejar múltiples tareas aparentemente al mismo tiempo. En lugar de procesar a un cliente por completo antes de atender al siguiente, la programación concurrente permite que el servidor alterne entre las conexiones de forma eficiente.

* **Threading (Hilos):** Los hilos son una de las formas más comunes de lograr la concurrencia en Python. Un **hilo** es una unidad de ejecución ligera dentro de un proceso. Para el chat multiusuario, el servidor puede crear un nuevo hilo por cada cliente que se conecta. Cada hilo se encarga de manejar la comunicación con su cliente específico, permitiendo que el hilo principal del servidor siga escuchando nuevas conexiones.

#### Puertos

Son un número de 16 bits que identifica una aplicación o servicio específico en una computadora. Cuando un cliente se conecta a una dirección IP, también debe especificar un puerto para que el sistema operativo sepa a qué programa entregar los datos. Por ejemplo, el puerto 80 es el puerto estándar para el tráfico HTTP. El proyecto **Servidor HTTP Básico** usará el puerto 80 (o un puerto similar) para recibir las solicitudes web.

## Sugerencias para aprender más ...

- Logging configurable por módulo
- Pruebas unitarias para cada ejemplo
- Documentación detallada por componente
- Manejo robusto de errores y excepciones
- Código limpio y bien documentado
- Patrones de diseño aplicados

## Recursos Adicionales

- [Documentación oficial de sockets en Python](https://docs.python.org/3/library/socket.html)
- [Python Socket Programming: Server and Client Example Guide](https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client)
- [Socket Programming in Python (Guide)](https://realpython.com/python-sockets/)
- [Python Socket Programming: Server-Client Connection](https://www.pubnub.com/blog/python-socket-programming-client-server/)
- [Guía completa de programación de sockets en Python](https://www.datacamp.com/es/tutorial/a-complete-guide-to-socket-programming-in-python)


