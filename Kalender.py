"""
Programmieren_I
Autor1:Tang,Lizhong(4068443) 
Autor2:Chen,Cheng(4068922) 
Autor3:Song,Zhaorui(4068539)
Fachbereich:EIT 1
Gruppe:3
Datum:21.02.2019
Version 5
"""
#Module time
import time as t
#Ausgabe des Kalenders
def p(jahr,monat):
#Name des Monates
    print "  ----------",monat_dict[int(monat)],jahr,"----------"
    print "  Sun  Mon  Tue  Wed  Thu  Fri  Sat"
    return main(jahr,monat)
    
    
#Urteilung des Schaltjahres    
def schalt(jahr):
    jahr=int(jahr)
    if jahr % 4 == 0 and jahr %100 !=0 or jahr % 400==0:
        return True
    else:
        return False
#Analyse der Anzahl der Tage in jedem Monat
def m(monat):
    monat=int(monat)
    if monat in (1,3,5,7,8,10,12):
        return 31
    elif monat in(4,6,9,11):
        return 30
    elif schalt(jahr):
        return 29
    else:
       return 28
#gesamte Tage von 01,01,1899 bis bestimmtes Jahr,bestimmtes Monat.01,01,1899 ist Sonntag
def gesamttage(jahr,monat):
    jahr=int(jahr)
    monat=int(monat)
    tag=0
    for i in range (1899,jahr):
        if schalt(i):
            tag=tag+366
        else:
            tag=tag+365
    for j in range (1,monat):
        tag=tag+m(j)  
    return tag
def main(jahr,monat): 
    x=gesamttage(jahr,monat)
    b=x%7
#b=Woche (z.B.b=1,d.h.dieser Tag ist Montag)
    if b!=0:
#  sun  mon  tue
#12301234012340
        print "    "*b+" "*(b-1),
    for v in range(1,m(monat)+1):
#ab 4-te Stelle,Bereite sind 4 zwischen den Zahlen
        print "%4d"%v,
        b=b+1
#Zeilen wechseln
        if b %7==0:  
            print " "
    print " "
#Monat in Woerterbuch
monat_dict={1:"Januar",2:"Februar",3:"Maerz",4:"April",5:"Mai",6:"Juni",7:"Juli",8:"August",9:"September",10:"Oktober",11:"November",12:"Dezember"}
#Analyse der Fehler 
while True:
    print"a-----bestimmten Monat aus dem aktuellen Jahr anzeigen\nb-----alle Kalender fuer ausgewaehltes Jahr anzeigen\nc-----bestimmten Monat aus bestimmten Jahr anzeigen\nd-----beenden"        
    option=raw_input("Geben Sie Option:")
    if option=="a":
        jahr=t.strftime("%Y")
        while True:
            monat=raw_input("cal -m")
#bei normalem Fall:
            try :
                if int(monat) in (1,2,3,4,5,6,7,8,9,10,11,12):
                    break
                else:
                    print "Monat muss von 1 bis 12 sein"
#bei dem Fall des existierenden Fehlers
            except:
                print "Monat muss zahl sein"
        p(jahr,monat)
        
    elif option=="b":
        while True:
            jahr=raw_input("cal -y")
            
            try:
                if int(jahr)>1899:
                    break
                else:
                    print "Jahr muss groesser als 1899 sein"
            except:
                print "Jahr muss ein Zahl sein"
        for i in range (1,13):
            monat=i
            p(jahr,monat)
            t.sleep(1)
    elif option == "c":
#Eingabe der zwei Argumente in einer Zelle
        while True:
            try:
                monat,jahr=raw_input("cal -my").split()
                if int(monat) in (1,2,3,4,5,6,7,8,9,10,11,12) and int(jahr)>1899:
                    break
                else:
                    print "ungueltig,bitte nochmal.Monat muss von 1 bis 12.Jahr muss groesser als 1899 sein."
            except:
                print "ungueltig,bitte nochmal.Geben Sie bitte 2 Argumente ein ,erste ist Monat ,dann Leerzeichen , zweite ist Jahr und zwar sie muessen Zahlen sein"
            
        p(jahr,monat)
    elif option=="d":
        break
    else:
        print "ungueltig,nochmal bitte ,Geben Sie bitte nur a,b,c oder d ein."
    


