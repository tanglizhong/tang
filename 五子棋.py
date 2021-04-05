import tkinter as tk
from tkinter import messagebox
s=0
xy_x =[]
xy_y =[]
    
def schwarz(event):
    global s,xy_x,xy_Y
  
    a = event.x                      
    b = event.y
    c = 30
    d = 80
    j=0
    while (j<19):
        for i in range(30,1000,50):
            if (c<a<d and i<b<i+50 and s%2==0 and [c,i,d,i+50] not in xy_x and [c,i,d,i+50] not in xy_y):
                xy=cv.create_oval(c,i,d,i+50,fill="black")
                xy_x.append(cv.coords(xy))
                print(cv.coords(xy))
                s += 1

                if([c, i, d, i+50] in xy_x and [c+50, i, d+50, i+50] in xy_x and [c+100, i, d+100, i+50] in xy_x and [c+150, i, d+150,i+50]in xy_x and [c+200, i, d+200, i+50] in xy_x ):
                    messagebox.showinfo(title="Ergebnis",message="Schwarz ist Gewinner \nSpiel verlassen  bitte ok drueken")
                    fenster.destroy()  
                elif([c, i, d, i+50] in xy_x and [c-50, i, d-50, i+50] in xy_x and [c-100, i, d-100, i+50] in xy_x and [c-150, i, d-150,i+50]in xy_x and [c-200, i, d-200, i+50] in xy_x ):
                    messagebox.showinfo(title="Ergebnis",message="Schwarz ist Gewinner \nSpiel verlassen  bitte ok drueken")
                    fenster.destroy()
                elif([c, i, d, i+50] in xy_x and [c, i+50, d, i+100] in xy_x and [c, i+100, d, i+150] in xy_x and [c, i+150, d,i+200]in xy_x and [c, i+200, d,i+250] in xy_x ):
                    messagebox.showinfo(title="Ergebnis",message="Schwarz ist Gewinner \nSpiel verlassen  bitte ok drueken")
                    fenster.destroy()
                elif([c, i, d, i+50] in xy_x and [c, i-50, d, i] in xy_x and [c, i-100, d, i-50] in xy_x and [c, i-150, d,i-100]in xy_x and [c, i-200, d,i-150] in xy_x ):
                    messagebox.showinfo(title="Ergebnis",message="Schwarz ist Gewinner \nSpiel verlassen  bitte ok drueken")
                    fenster.destroy()
                elif([c, i, d, i+50] in xy_x and [c+50, i+50, d+50, i+100] in xy_x and [c+100, i+100, d+100, i+150] in xy_x and [c+150, i+150, d+150,i+200]in xy_x and [c+200, i+200, d+200,i+250] in xy_x ):
                    messagebox.showinfo(title="Ergebnis",message="Schwarz ist Gewinner \nSpiel verlassen  bitte ok drueken")
                    fenster.destroy()
                elif([c, i, d, i+50] in xy_x and [c-50, i-50, d-50, i] in xy_x and [c-100, i-100, d-100, i-50] in xy_x and [c-150, i-150, d-150,i-100]in xy_x and [c-200, i-200, d-200,i-150] in xy_x ):
                    messagebox.showinfo(title="Ergebnis",message="Schwarz ist Gewinner \nSpiel verlassen  bitte ok drueken")
                    fenster.destroy()
                elif([c, i, d, i+50] in xy_x and [c-50, i+50, d-50, i+100] in xy_x and [c-100, i+100, d-100, i+150] in xy_x and [c-150, i+150, d-150,i+200]in xy_x and [c-200, i+200, d-200, i+250] in xy_x ):
                    messagebox.showinfo(title="Ergebnis",message="Schwarz ist Gewinner \nSpiel verlassen  bitte ok drueken")
                    fenster.destroy()
                elif([c, i, d, i+50] in xy_x and [c+50, i-50, d+50, i] in xy_x and [c+100, i-100, d+100, i-50] in xy_x and [c+150, i-150, d+150,i-100]in xy_x and [c+200, i-200, d+200, i-150] in xy_x ):
                    messagebox.showinfo(title="Ergebnis",message="Schwarz ist Gewinner \nSpiel verlassen  bitte ok drueken")
                    fenster.destroy()
                else:
                    continue

            else:
                continue
        c += 50
        d += 50
        j +=1
          
        
def weiss(event):
    global s,xy_x,xy_Y
    a = event.x                      
    b = event.y
    c = 30
    d = 80
    j=0
    while (j<19):
        for i in range(30,1000,50):
            if (c<a<d and i<b<i+50 and s%2==1 and [c,i,d,i+50] not in xy_x and [c,i,d,i+50] not in xy_y ):
                xy=cv.create_oval(c,i,d,i+50,fill="white")
                xy_y.append(cv.coords(xy))
                s += 1
                if([c, i, d, i+50] in xy_y and [c+50, i, d+50, i+50] in xy_y and [c+100, i, d+100, i+50] in xy_y and [c+150, i, d+150,i+50]in xy_y and [c+200, i, d+200, i+50] in xy_y ):
                    messagebox.showinfo(title="Ergebnis",message="weiss ist Gewinner \nSpiel verlassen  bitte ok drueken")
                    fenster.destroy()  
                elif([c, i, d, i+50] in xy_y and [c-50, i, d-50, i+50] in xy_y and [c-100, i, d-100, i+50] in xy_y and [c-150, i, d-150,i+50]in xy_y and [c-200, i, d-200, i+50] in xy_y ):
                    messagebox.showinfo(title="Ergebnis",message="weiss ist Gewinner \nSpiel verlassen  bitte ok drueken")
                    fenster.destroy()
                elif([c, i, d, i+50] in xy_y and [c, i+50, d, i+100] in xy_y and [c, i+100, d, i+150] in xy_y and [c, i+150, d,i+200]in xy_y and [c, i+200, d,i+250] in xy_y ):
                    messagebox.showinfo(title="Ergebnis",message="weiss ist Gewinner \nSpiel verlassen  bitte ok drueken")
                    fenster.destroy()
                elif([c, i, d, i+50] in xy_y and [c, i-50, d, i] in xy_y and [c, i-100, d, i-50] in xy_y and [c, i-150, d,i-100]in xy_y and [c, i-200, d,i-150] in xy_y ):
                    messagebox.showinfo(title="Ergebnis",message="weiss ist Gewinner \nSpiel verlassen  bitte ok drueken")
                    fenster.destroy()
                elif([c, i, d, i+50] in xy_y and [c+50, i+50, d+50, i+100] in xy_y and [c+100, i+100, d+100, i+150] in xy_y and [c+150, i+150, d+150,i+200]in xy_y and [c+200, i+200, d+200,i+250] in xy_y ):
                    messagebox.showinfo(title="Ergebnis",message="weiss ist Gewinner \nSpiel verlassen  bitte ok drueken")
                    fenster.destroy()
                elif([c, i, d, i+50] in xy_y and [c-50, i-50, d-50, i] in xy_y and [c-100, i-100, d-100, i-50] in xy_y and [c-150, i-150, d-150,i-100]in xy_y and [c-200, i-200, d-200,i-150] in xy_y ):
                    messagebox.showinfo(title="Ergebnis",message="weiss ist Gewinner \nSpiel verlassen  bitte ok drueken")
                    fenster.destroy()
                elif([c, i, d, i+50] in xy_y and [c-50, i+50, d-50, i+100] in xy_y and [c-100, i+100, d-100, i+150] in xy_y and [c-150, i+150, d-150,i+200]in xy_y and [c-200, i+200, d-200,i+250] in xy_y ):
                    messagebox.showinfo(title="Ergebnis",message="weiss ist Gewinner \nSpiel verlassen  bitte ok drueken")
                    fenster.destroy()
                elif([c, i, d, i+50] in xy_y and [c+50, i-50, d+50, i] in xy_y and [c+100, i-100, d+100, i-50] in xy_y and [c+150, i-150, d+150,i-100]in xy_y and [c+200, i-200, d+200,i-150] in xy_y ):
                    messagebox.showinfo(title="Ergebnis",message="weiss ist Gewinner \nSpiel verlassen  bitte ok drueken")
                    fenster.destroy()
                else:
                    continue

            else:
                continue
                
        c += 50
        d += 50
        j +=1

        
def maus_links():
    cv.bind("<Button-1>",schwarz)
def maus_rechts():
    cv.bind("<Button-3>",weiss)
def spielen1():
    print("人机模式")
def spielen2():
    print("玩家对抗")
    maus_links()
    maus_rechts()
    
  
def button2():
    fenster.destroy()
def menue():
    global item
    topmenu = tk.Menu(fenster)
    file1=tk.Menu(fenster)
    for item in ["新建","打开","保存","另存为"] :
        file1.add_command(label=item)
    file2=tk.Menu(fenster)
    file2.add_command(label="人机模式",command=spielen1)
    file2.add_command(label="玩家对抗",command=spielen2)
    
    topmenu.add_cascade(label="文件",menu=file1)
    topmenu.add_command(label="编辑")
    topmenu.add_cascade(label="模式",menu=file2)
    topmenu.add_command(label="离开",command=button2)
    fenster.config(menu=topmenu)

def button1():
    bt1.place_forget()
    bt2.place_forget()
    lb.place_forget()
    a=cv.create_rectangle(0,0,1010,1010,fill="green")
    x=50
    for i in range(21):
        cv.create_line(x-45,5,x-45,1005)
        x += 50
    y=50
    for i in range(21):
        cv.create_line(0,y-45,1005,y-45)
        y += 50
    
    menue()

fenster = tk.Tk()
fenster.title("五子棋")

cv=tk.Canvas(width=1010,height=1010,bg="lightblue")      
cv.pack()
 
lb = tk.Label(fenster,text="欢 迎 来 到 五 子 棋",bg="green")
lb.place(x=470,y=200)
bt1 = tk.Button(fenster ,text="开始游戏",bg="green",command=button1)       
bt1.place(x=500,y=300)
bt2 = tk.Button(fenster ,text="离开游戏",bg="green",command=button2)       
bt2.place(x=500,y=400)

fenster.mainloop()
