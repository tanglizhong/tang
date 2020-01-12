import tkinter as tk
import tkinter.messagebox
import time as t
fenster = tk.Tk()
fenster.configure(background='red') 
fenster.title("Geldautomat")
fenster.geometry("500x500")


pin="13579"


def button1():
    bt1.place_forget()
    bt2.place_forget()
    bt3.place_forget()
    bt4.place_forget()
    bt11=tk.Button(fenster ,text="Noten",bg="red",command=button11)       
    bt11.place(x=200,y=200)
    bt12=tk.Button(fenster ,text="Münzen",bg="green",command=button11)       
    bt12.place(x=200,y=250)
    
    
def button_geld():
    tkinter.messagebox.showinfo(title="Hinweis",message="Bitte haben Sie kurz Geduld,Ihr Geld kommt gleich")

    t.sleep(5)
    tkinter.messagebox.showinfo(title="Hinweis",message="Bitte nehmen Sie Ihr Geld")
    
    button()

    
    
    

def button11():
    tkinter.messagebox.showinfo(title="Hinweis",message="Legen Sie Geld bitte ein")
    t.sleep(10)
    tkinter.messagebox.showinfo(title="Hinweis",message="Sie haben schon eingezahlt")
    button()
def button2():
    tkinter.messagebox.showinfo(title="Hinweis",message="Geben Sie Ihre Geheimzahl ein:")
    bt1.place_forget()
    bt2.place_forget()
    bt3.place_forget()
    bt4.place_forget()
    #text1 = tk.Text(fenster, width=6, height=1, bg='orange', font=('Arial', 12))
    #text1.place(x=200,y=250)
    while True:
        p=str(input("Geben Sie Ihre Geheimzahl ein:"))
        if p == pin:
            break
    geld()
            
        
def geld():         
    geld1=tk.Button(fenster ,text="50",bg="green",command=button_geld)       
    geld1.place(x=200,y=200)
    geld2=tk.Button(fenster ,text="100",bg="green",command=button_geld)       
    geld2.place(x=200,y=250)
    geld3=tk.Button(fenster ,text="200",bg="green",command=button_geld)       
    geld3.place(x=200,y=300)



def button3():
    print ("Sie haben kein Geld")
    




def button():
    bt1=tk.Button(fenster ,text="Einzahlung",bg="green",command=button1)       
    bt1.place(x=200,y=200)
    bt2=tk.Button(fenster ,text="Auszahlung",bg="green",command=button2)       
    bt2.place(x=200,y=250)
    bt3=tk.Button(fenster ,text="Kontostand",bg="green",command=button3)       
    bt3.place(x=200,y=300)
    bt4=tk.Button(fenster ,text="Karte zurueck",bg="green",command=button3)       
    bt4.place(x=200,y=350)

    
bt1=tk.Button(fenster ,text="Einzahlung",bg="green",command=button1)       
bt1.place(x=200,y=200)
bt2=tk.Button(fenster ,text="Auszahlung",bg="green",command=button2)       
bt2.place(x=200,y=250)
bt3=tk.Button(fenster ,text="Kontostand",bg="green",command=button3)       
bt3.place(x=200,y=300)
bt4=tk.Button(fenster ,text="Karte zurueck",bg="green",command=button3)       
bt4.place(x=200,y=350)




fenster.mainloop()
