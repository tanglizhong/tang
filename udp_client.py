"""
Autor1: Yulong Chunyu  4068559
Autor2: Lizhong Tang   4068443
Datum: 16.03.2021
"""
from socket import *
from time import *    #Module socket time
import sys
ip = sys.argv[1]
port = int(sys.argv[2])
udp_client = socket(AF_INET, SOCK_DGRAM) 
while True:
    try:
        msg_send = input("Geben Sie Ihre Nachricht ein:")  
        udp_client.sendto(msg_send.encode(),(ip, port)) #Nachricht codieren und an diese Addresse senden 
        if(msg_send== "ende"):
            break
        msg_recive, addr = udp_client.recvfrom(1472)  #Nachricht bekommen
        print (strftime("%d.%m.%Y %H:%M:%S", localtime()))
        print ("Server hat die Nachricht:",msg_recive.decode(),"erhalten")
    except:
        print("Server ist geschlossen")
        break
    
udp_client.close()

