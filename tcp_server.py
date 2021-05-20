"""
Autor1: Yulong Chunyu  4068559
Autor2: Lizhong Tang   4068443
Datum: 16.03.2021
"""
from socket import *        #Module socket threading time
from threading import *  
from time import *
import fileinput
import sys
ip = "192.168.1.47"
port=int(sys.argv[1])
print(port)
addr = (ip, port)
tcpSocket = socket(AF_INET, SOCK_STREAM)   #neues socket erstellen
tcpSocket.bind(addr)        #tcpSocket verbindet mit addr
tcpSocket.listen(5)         #maximale Client gleichzeitig

def tcp(Socket, clientAddr):  #Unterprogramm zum Empfangen und Senden
    
    while True:
       
        try:
            msg = Socket.recv(1024)     #maximal 1024 Byte für ein Mal
            
            if (str(msg,"utf8") == "ende"):
                print ("Server hat schon mit der IP: %s" %clientAddr[0]," port: %s" %clientAddr[1],"getrennt")
                Socket.close()
                
                
                """
                antwort = input("Schalten Sie Server aus? \nwenn ja, bitte geben Sie j ein\nwenn nein, dann geben Sie bitte egal ein\nGeben Sie bitte Ihre Antwort ein:")
                if (antwort == "j"):
                    m=0
                    break
                                
                                
                else:
                    print("Wartet auf die Verbindung...")
                    m=1
                    break
                """
            else:    
                nachricht=str(msg,"utf8")  
                #print(msg.decode())
                print (strftime("%d.%m.%Y %H:%M:%S", localtime()))   #aktuelle Zeit
                print("Nachricht aus client IP:",clientAddr[0]," port:",clientAddr[1],":",nachricht)
                Socket.send(bytes(nachricht,"utf8"))
          
            
        except:         
            print("client IP:",clientAddr[0]," port:",clientAddr[1], "ist geschlossen\nwartet auf andere Verbindung...")
            break
    
print("Wartet auf die Verbindung...")


while True:
       
    
    Socket, clientAddr = tcpSocket.accept()      #Verbindung akzeptieren
    sleep(1)
    print('Verbindung mit der IP: %s' %clientAddr[0],' port: %s' %clientAddr[1])

    t = Thread(target=tcp,args=(Socket, clientAddr))  #Unterfunktion aufrufen
    t.start() #neue Linie beginnt
  
  
            


 
        
        
   


       
    




