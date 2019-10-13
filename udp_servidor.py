######################################################################################
# Instituto Tecnológico de Colima - División de Estudios de Posgrado e Investigación #
# Maestría en Sistemas Computacionales - Materia: Tecnologías de Internet            #
#                                                                                    #
# Código Fuente para Servidor UDP                                                    #
# Realizado por:                                                                     #
# Osvaldo Vladimir Rodríguez Leal                                                    #
# José Alfredo Cortés Quiroz                                                         #
# Villa de Álvarez, Col 12/10/19                                                     #
######################################################################################
import socket
import time

localIP = "0.0.0.0" # dirección ip local
localPort = 20001 # puerto de escucha
bufferSize = 1024 # tamaño del bufer

# La siguiente instrucción crea el Datagrama para UDP
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# La siguiente instrucción crea el servidor UDPP
UDPServerSocket.bind((localIP, localPort))
print("..::Chat UDP Online::..") # el código siguiente inicia el chat y enviar cadenas de texto por udp al cliente
while(True):
    
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize) # Devuelve un objeto de bytes leído por UDP y la dirección del socket del cliente
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "--> Client Say: {}".format(message)
    clientIP  = "MSG FROM IP: {}".format(address)    
    print(clientMsg) #imprimimos en pantalla el mensaje
    print(clientIP) # imprimimos en pantalla la dirección IP de donde se envia el mensaje
    msgFromServer = raw_input("--> You Say: ") # asignamos el texto a enviar en una variable  
    bytesToSend = str.encode(msgFromServer) # Convertimos  a bytes para el envío
    UDPServerSocket.sendto(bytesToSend, address) # Enviamos mensaje a cliente