"""
Autor1: Yulong Chunyu  4068559
Autor2: Lizhong Tang   4068443
Datum: 16.03.2021
"""
from socket import *
from time import *    # Module socket time
import sys
ip = "127.0.0.1"
port=int(sys.argv[1])
udp_server = socket(AF_INET, SOCK_DGRAM) 
udp_server.bind((ip, port))  #Server verbindet eigene ip

while True:
    print ("wartet auf die Nachrichten...")
    while True:
        msg, addr = udp_server.recvfrom(1024)
        msg = msg.decode()  #Nachricht decodieren
        if (msg == "ende"):
            print("Client ip",addr[0],"port:",addr[1],"ist geschlossen")
            break
        print (strftime("%d.%m.%Y %H:%M:%S", localtime()))
        print("Nachricht aus client ip",addr[0],"port:",addr[1],msg)
        udp_server.sendto(msg.encode() ,addr)   #Nachricht codieren und  Nachricht an Client senden
       
       
    
    antwort = input("Schalten Sie Server aus? \nwenn ja, bitte geben Sie j ein\nwenn nein, dann geben Sie bitte egal ein\nGeben Sie bitte Ihre Antwort ein:")
    if antwort == ("j"):
        break
    else:
        continue
        

udp_server.close()
print("Server ist geschlossen")

