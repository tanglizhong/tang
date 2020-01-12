import tkinter as tk
import tkinter.messagebox
import time as t
fenster = tk.Tk()
fenster.configure(background='lightpink') 
fenster.title("Geldautomat")
fenster.geometry("500x500")


pin="1234"
kontostand = 500
def button1():
    global bt11
    global bt12
    global bt1
    global bt2
    global bt3
    global bt4
    bt1.place_forget()
    bt2.place_forget()
    bt3.place_forget()
    bt4.place_forget()
    bt11=tk.Button(fenster ,text="Noten",bg="lightblue",command=button11)       
    bt11.place(x=200,y=200)
    bt12=tk.Button(fenster ,text="Münzen",bg="lightblue",command=button11)       
    bt12.place(x=200,y=250)
    
    
def button_geld():
    global geld1
    global geld2
    global geld3
    tkinter.messagebox.showinfo(title="Hinweis",message="Bitte haben Sie kurz Geduld,Ihr Geld kommt bald")
    t.sleep(1)
    tkinter.messagebox.showinfo(title="Hinweis",message="Bitte nehmen Sie Ihr Geld ")


    geld1.place_forget()
    geld2.place_forget()
    geld3.place_forget()
    button()
def button_geld1():
    button_geld()
    global kontostand
    if kontostand < 50:
        tkinter.messagebox.showinfo(title="Hinweis",message="Ihr Konto hat weniger als 50 Euro")
        geld1.place_forget()
        geld2.place_forget()
        geld3.place_forget()
        button()
        
    else:
        button_geld()

        
        
        kontostand = kontostand - 50
    
def button_geld2():
    global kontostand
    if kontostand <100:
        tkinter.messagebox.showinfo(title="Hinweis",message="Ihr Konto hat weniger als 100 Euro")
        geld1.place_forget()
        geld2.place_forget()
        geld3.place_forget()
        button()

        
    else:
        button_geld()
        
        kontostand = kontostand - 100
    
def button_geld3():
    
    global kontostand
    if kontostand <200:
        tkinter.messagebox.showinfo(title="Hinweis",message="Ihr Konto hat weniger als 200 Euro")
        geld1.place_forget()
        geld2.place_forget()
        geld3.place_forget()
        button()
        
    else:
        button_geld()
    
        kontostand = kontostand - 200
def buffer1():
    global frage
    frage.place_forget()
    button()
def buffer2():
    fenster.destroy()
def button11():
    global kontostand
    global frage
    einzahlung=int(input("Wie viel Gled möchten Sie einzahlen?"))
    kontostand=kontostand+einzahlung
    tkinter.messagebox.showinfo(title="Hinweis",message="Legen Sie Ihr Geld bitte ein")
    t.sleep(1)
    print ("Sie haben ",einzahlung,"Euro eingezahlt")
    bt11.place_forget()
    bt12.place_forget()
    frage=tk.Label(fenster,text="Möchten Sie weiter machen ?")
    frage.place(x=150,y=100)
    bf1=tk.Button(fenster ,text="ja",bg="lightblue",command=buffer1)       
    bf1.place(x=200,y=200)
    bf2=tk.Button(fenster ,text="nein",bg="lightblue",command=buffer2)       
    bf2.place(x=200,y=250)
    
        
        
    
    
def button2():
    global bt1
    global bt2
    global bt3
    global bt4
    tkinter.messagebox.showinfo(title="Hinweis",message="Geben Sie Ihre Geheimzahl ein:")
    bt1.place_forget()
    bt2.place_forget()
    bt3.place_forget()
    bt4.place_forget()
    
    while True:
        p=str(input("Geben Sie Ihre Geheimzahl ein:"))
        
            
        if p == pin:
            break
        else:
            print ("Sie haben falsche Geheimzahl eingegeben,bitte versuchen Sie noch einmal ")
       
    geld()
    
            
        
def geld():
    global geld1
    global geld2
    global geld3
    geld1=tk.Button(fenster ,text=" 5 0",bg="lightblue",command=button_geld1)       
    geld1.place(x=200,y=200)
    geld2=tk.Button(fenster ,text="1 0 0",bg="lightblue",command=button_geld2)       
    geld2.place(x=200,y=250)
    geld3=tk.Button(fenster ,text="2 0 0",bg="lightblue",command=button_geld3)       
    geld3.place(x=200,y=300)



def button3():
    
    
    print ("Sie haben",kontostand,"Euro")
    
    
def button4():
    tkinter.messagebox.showinfo(title="Hinweis",message="Bitte nehmen Sie Ihre Karte zurück:")
    fenster.destroy()




def button():
    global bt1
    global bt2
    global bt3
    global bt4
    
    bt1=tk.Button(fenster ,text="Einzahlung",bg="lightblue",command=button1)       
    bt1.place(x=200,y=200)
    bt2=tk.Button(fenster ,text="Auszahlung",bg="lightblue",command=button2)       
    bt2.place(x=200,y=250)
    bt3=tk.Button(fenster ,text="Kontostand",bg="lightblue",command=button3)       
    bt3.place(x=200,y=300)
    bt4=tk.Button(fenster ,text="Karte zurueck",bg="lightblue",command=button4)       
    bt4.place(x=200,y=350)

   
bt1=tk.Button(fenster ,text="Einzahlung",bg="lightblue",command=button1)       
bt1.place(x=200,y=200)
bt2=tk.Button(fenster ,text="Auszahlung",bg="lightblue",command=button2)       
bt2.place(x=200,y=250)
bt3=tk.Button(fenster ,text="Kontostand",bg="lightblue",command=button3)       
bt3.place(x=200,y=300)
bt4=tk.Button(fenster ,text="Karte zurueck",bg="lightblue",command=button4)       
bt4.place(x=200,y=350)




fenster.mainloop()
