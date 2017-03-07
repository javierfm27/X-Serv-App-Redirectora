#!/usr/bin/python3
"""
    Servidor que redirecciona permanentemente
    Javier Fernández Morata
    Aplicacion, que informa en el cuerpo a que URL va a ser redireccionado
"""
import socket
import random

# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
port = 1231
mySocket.bind((socket.gethostname(), port))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)

try:
    while True:
        print ('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print ('Request received:')
        print (recvSocket.recv(2048).decode('utf-8'))
        print ('Answering back...')
        httpCode = "HTTP/1.1 302 Found "
        aleatURL = str(random.randint(0,1000000))
        recvSocket.send(bytes(httpCode +
                        "\r\n" +
                        "Location: " +
                        aleatURL +
                        "\r\n\r\n" +
                        "<html> +
                        "<body><h1>Va a ser redirigido a </h1>" +
                        "<p>http://" +
                         socket.gethostname() +
                         ":" +
                         str(port) +
                         "/" +
                         str(aleatURL) +
                        "</p>" +
                        "</body></html>" +
                        "\r\n",
                        'utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print ("Closing binded socket")
    mySocket.close()
