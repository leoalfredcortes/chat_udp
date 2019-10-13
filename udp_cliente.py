######################################################################################
# Instituto Tecnológico de Colima - División de Estudios de Posgrado e Investigación #
# Maestría en Sistemas Computacionales - Materia: Tecnologías de Internet            #
#                                                                                    #
# Código Fuente para Cliente UDP                                                     #
# Realizado por:                                                                     #
# Osvaldo Vladimir Rodríguez Leal                                                    #
# José Alfredo Cortés Quiroz                                                         #
# Villa de Álvarez, Col 12/10/19                                                     #
######################################################################################

import socket 
import time

#serverAddressPort = (((socket.gethostbyname("leoalfred.ddns.net")), 20001)) #Dirección del servidor REMOTO y el puerto
serverAddressPort = ("127.0.0.1", 20001) #Dirección del servidor local y el puerto
bufferSize = 1024 # tamaño del bufer

# La siguiente instrucción crea el Datagrama para UDP
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# El código siguiente inicia el chat con el servidor y permite enviarle cadenas de texto por udp
print("..::Chat UDP Online::.")
while(True):
    msgFromClient = raw_input("--> You Say: ") # asignamos el texto a enviar a una variable
    bytesToSend = str.encode(msgFromClient) # codificamos la cadena a bytes
    UDPClientSocket.sendto(bytesToSend, serverAddressPort) # enviamos el texto al servidor    
    time.sleep(1) # damos una ligera pausa y quedamos a la espera
    msgFromServer = UDPClientSocket.recvfrom(bufferSize) # asignamos el texto recibido  a una variable
    msg = "--> Server Say: {}".format(msgFromServer[0]) #añadimos texto y decodificamos el mensaje
    time.sleep(1) # damos una ligera pausa y quedamos a la espera
    print(msg) # imprimimos el mensaje en pantalla
