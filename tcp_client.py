"""
Autor1: Yulong Chunyu  4068559
Autor2: Lizhong Tang   4068443
Datum: 16.03.2021
"""
from socket import *   #Module socket und time
from time import *
import sys

serverName=sys.argv[1]
serverPort=int(sys.argv[2])

ADDR = (serverName,serverPort)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(ADDR)   #verbinden mit dem Server
print("Verbindung mit der IP: %s" %serverName, "port: %s" %serverPort)
while True:
    try:
        msg = input("Geben Sie Ihre Nachricht ein:")
        
        #clientSocket.send(msg.encode())
        clientSocket.send(bytes(msg,"utf8"))
        if (msg == "ende"):
            break
        
        msg_r = clientSocket.recv(1024)
        sleep(1)
        print (strftime("%d.%m.%Y %H:%M:%S", localtime()))
        print("Server hat die Nachriceht: ",str(msg_r,"utf8")," erhalten")
    except:
        print("Server ist geschlossen")
        break
        
   
    
clientSocket.close()
print("Client ist geschlossen")
