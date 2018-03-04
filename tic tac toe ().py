from tkinter import *
from random import *
from time import *
root=Tk()
flagfor2=IntVar()
list=[]
listo=["1 1","1 3","1 5","3 1","3 3","3 5","5 1","5 3","5 5"]
liststart=["1 1","5 1","5 5","1 5"]
listsecond=["1 3","3 5","3 1","5 3"]
listse=["1 1","1 5","5 1","5 5"]
pl=IntVar()

class board:
    def __init__(self,a=0,color="white"):
        
        self.color=color
        self.a=Canvas(root,height=1000,width=1000,bg=self.color)
        
        self.a.pack()
        self.mainmenu()
        
        
        
        
        
        

        
    def x(self,g,h):
        self.linex1=self.a.create_line(g-50,h-50,g+50,h+50,width=5)
        self.linex2=self.a.create_line(g+50,h-50,g-50,h+50,width=5)
    def mainmenu(self):
        
        self.fra=Frame(self.a,bg="white")
        self.fra.place(x=500,y=300)
        self.b1=Button(self.fra,text="play with cpu",command=self.cpu).pack(pady=20)
        self.b2=Button(self.fra,text="Two player game",command=self.player).pack()
        
    def creboard(self):
        self.a.pack_forget()
        line1=self.a.create_line(200,0,200,600)
        line2=self.a.create_line(400,0,400,600)
        line3=self.a.create_line(0,200,600,200)
        line4=self.a.create_line(0,400,600,400)
        self.mb=  Menubutton ( self.a, text="BOARD COLOR",bg="grey" )
        
        self.mb.menu =  Menu ( self.mb, tearoff = 0 )
        self.mb["menu"] =  self.mb.menu

        

        self.mb.menu.add_command( label="blue",command=lambda:self.bc("blue") )
        self.mb.menu.add_command ( label="green",command=lambda:self.bc("green"))
        self.mb.menu.add_command ( label="red",command=lambda:self.bc("red"))
        self.mb.menu.add_command ( label="white",command=lambda:self.bc("white") )
        self.mb.menu.add_command ( label="orange",command=lambda:self.bc("orange") )
        self.mb.place(x=800,y=400)
        self.b1=Button(self.a,text="renew game",bg="white",command=self.renew1)
        self.b1.place(x=800,y=100)
        self.b2=Button(self.a,text="change player options",command=self.renew2).place(x=800,y=300)
        self.a.bind("<Button-1>",click)
        self.a.pack()
    def o(self,g,h):
        circle=self.a.create_oval(g-50,h-50,g+50,h+50,width=5)
    def bc(self,color):
        self.a.config(bg=color)
    def cl(self,g,h,i,j):
        self.lineu1=self.a.create_line(g,h,i,j,width=5)
    def cpu(self):
        self.fra.destroy()
        pl.set(1)
        self.creboard()
    def player(self):
        self.fra.destroy()
        pl.set(0)
        self.creboard()
        
        
    def renew1(self):
        self.a.delete("all")
        self.creboard()
        #self.a=board()
        global list
        global listo
        global listsecond
        global listse
        
        list=[]
        count.set(0)
        flagfor2.set(0)
        
        listo=["1 1","1 3","1 5","3 1","3 3","3 5","5 1","5 3","5 5"]
        listsecond=["1 3","3 5","3 1","5 3"]
        listse=["1 1","1 5","5 1","5 5"]
    def renew2(self):
        
        
        self.renew1()
        self.mainmenu()

        
def win2(t,u,v,w=0):
    global list
    print(list)
    winner=None
    if ("x"+t in list and "x"+u in list and "x"+v in list) or ("o"+t in list and "o"+u in list and "o"+v in list):  
        if w==1:
            board1.cl(0,100,600,100)
        elif w==2:
            board1.cl(0,100+200,600,100+200)
        elif w==3:
            board1.cl(0,100+200+200,600,100+200+200)
        elif w==4:
            board1.cl(100,0,100,600)
        elif w==5:
            board1.cl(100+200,0,100+200,600)
        elif w==6:
            board1.cl(100+200+200,0,100+200+200,600)
        elif w==7:
            board1.cl(0,0,600,600)
        
        else:
            board1.cl(0,600,600,0)
        if count.get()%2==0 and winner==None:
            messagebox.showinfo("winner","0 wins")
            winner=1
        elif count.get()%2!=0 and winner==None:
            messagebox.showinfo("winner","x wins")
            winner=1
            board1.renew1()
    else:
        if count.get()==9:
            
            messagebox.showinfo("winner","tie")
            board1.renew1()
        
    
    
            
     
            
def win():
    if count.get()!=10:
        win2("11","31","51",1)
        win2("13","33","53",2)
        win2("15","35","55",3)
        win2("11","13","15",4)
        win2("31","33","35",5)
        win2("51","53","55",6)
        win2("11","33","55",7)
        win2("15","33","51",8)
    '''elif count.get()==9 :
            messagebox.showinfo("winner","match tie")
            board1.renew1()'''
    
        
        
    
        
def sea(i,j):
    global list
    global listo
    global listse
    if ("x"+str(i)+str(j)) not in list and ("o"+str(i)+str(j)) not in list :
        
        if count.get()%2==0:
            board1.x(i*100,100*j)
            list.append("x"+str(i)+str(j))
            
        else:
            board1.o(i*100,100*j)
            list.append("o"+str(i)+str(j))

        listo.remove(str(i)+" "+str(j))
        if str(i)+" "+str(j) in listsecond:
            listsecond.remove(str(i)+" "+str(j))
        if str(i)+" "+str(j) in listse:
            listse.remove(str(i)+" "+str(j))
        count.set(count.get()+1)
        print(list)
        print(count.get())
        
    win()
        
    

count=IntVar()
count.set(0)

def click(event):
    global listo
    
    for j in range(1,6,2):
        if(j-1)*100<event.y<(j+1)*100:
            for i in range(1,6,2):
                if (i-1)*100<event.x<(i+1)*100 :
                    sea(i,j)
                    
                    break
            break
    if pl.get()==1:
        if count.get()%2!=0:
            cpum()
    
    
        
def cpu():
    if ("x11" in list and "x13" in list and "x15" not in list and "1 5" in listo) :
        sea(1,5)
    elif ("x13" in list and "x15" in list and "x11" not in list and "1 1" in listo):
        sea(1,1)
        
    elif ("x11" in list and "x15" in list and "x13" not in list and "1 3" in listo):
        sea(1,3)
    elif ("x31" in list and "x33" in list and "x35" not in list and "3 5" in listo):
        sea(3,5)
        
    elif ("x31" in list and "x35" in list and "x33" not in list and "3 3" in listo):
        sea(3,3)
    elif ("x33" in list and "x35" in list and "x31" not in list and "3 1" in listo):
        sea(3,1)
        
    elif ("x51" in list and "x55" in list and "x53" not in list and "5 3" in listo):
        sea(5,3)
    elif ("x53" in list and "x55" in list and "x51" not in list and "5 1" in listo):
        sea(5,1)
        
    elif ("x51" in list and "x53" in list and "x55" not in list and "5 5" in listo):
        sea(5,5)
    elif ("x11" in list and "x31" in list and "x51" not in list and "5 1" in listo):
        sea(5,1)
        
    elif ("x11" in list and "x51" in list and "x31" not in list and "3 1" in listo):
        sea(3,1)
    elif ("x31" in list and "x51" in list and "x11" not in list and "1 1" in listo):
        sea(1,1)
        
    elif ("x13" in list and "x33" in list and "x53" not in list and "5 3" in listo):
        sea(5,3)
    elif ("x13" in list and "x53" in list and "x33" not in list and "3 3" in listo):
        sea(3,3)
        
    elif ("x33" in list and "x53" in list and "x13" not in list and "1 3" in listo):
        sea(1,3)
    elif ("x15" in list and "x35" in list and "x55" not in list and "5 5" in listo):
        sea(5,5)
        
    elif ("x15" in list and "x55" in list and "x35" not in list and "3 5" in listo):
        sea(3,5)
    elif ("x35" in list and "x55" in list and "x15" not in list and "1 5" in listo):
        sea(1,5)
        
    elif ("x11" in list and "x33" in list and "x55" not in list and "5 5" in listo):
        sea(5,5)
    elif ("x11" in list and "x55" in list and "x33" not in list and "3 3" in listo):
        sea(3,3)
        
    elif ("x33" in list and "x55" in list and "x11" not in list and "1 1" in listo):
        sea(1,1)
    elif ("x15" in list and "x33" in list and "x51" not in list and "5 1" in listo):
        sea(5,1)
        
    elif ("x15" in list and "x51" in list and "x33" not in list and "3 3" in listo):
        sea(3,3)
    elif ("x33" in list and "x51" in list and "x15" not in list and "1 5" in listo):
        sea(1,5)
    else:
        if count.get()==3:
            if flagfor2.get()==1:
                p2w()
                x=randint(0,len(listsecond)-1)
                t2=listsecond[x].split()
                sea(int(t2[0]),int(t2[1]))
            else:
                p3w()
                x=randint(0,len(listse)-1)
                t2=listse[x].split()
                sea(int(t2[0]),int(t2[1]))
                
        else:
            x=randint(0,len(listo)-1)
            tl=listo[x].split()
            sea(int(tl[0]),int(tl[1]))
def cpustart():
    if "x33" not in list and not ("x13" in list or "x53" in  list or "x31" in list or "x35" in list):
        flagfor2.set(1)
        sea(3,3)
    elif "x33" not in list and ("x13" in list or "x53" in  list or "x31" in list or "x35" in list):
        flagfor2.set(2)
        sea(3,3)
        
    elif "x33" in list:
        flagfor2.set(2)
        x=randint(0,len(liststart)-1)
        t2=liststart[x].split()
        sea(int(t2[0]),int(t2[1]))

        
        
        
            
            
    
def cpumain():
    if ("o11" in list and "o13" in list and "o15" not in list and "1 5" in listo) :
        sea(1,5)
    elif ("o13" in list and "o15" in list and "o11" not in list and "1 1" in listo):
        sea(1,1)
        
    elif ("o11" in list and "o15" in list and "o13" not in list and "1 3" in listo):
        sea(1,3)
    elif ("o31" in list and "o33" in list and "o35" not in list and "3 5" in listo):
        sea(3,5)
        
    elif ("o31" in list and "o35" in list and "o33" not in list and "3 3" in listo):
        sea(3,3)
    elif ("o33" in list and "o35" in list and "o31" not in list and "3 1" in listo):
        sea(3,1)
        
    elif ("o51" in list and "o55" in list and "o53" not in list and "5 3" in listo):
        sea(5,3)
    elif ("o53" in list and "o55" in list and "o51" not in list and "5 1" in listo):
        sea(5,1)
        
    elif ("o51" in list and "o53" in list and "o55" not in list and "5 5" in listo):
        sea(5,5)
    elif ("o11" in list and "o31" in list and "o51" not in list and "5 1" in listo):
        sea(5,1)
        
    elif ("o11" in list and "o51" in list and "o31" not in list and "3 1" in listo):
        sea(3,1)
    elif ("o31" in list and "o51" in list and "o11" not in list and "1 1" in listo):
        sea(1,1)
        
    elif ("o13" in list and "o33" in list and "o53" not in list and "5 3" in listo):
        sea(5,3)
    elif ("o13" in list and "o53" in list and "o33" not in list and "3 3" in listo):
        sea(3,3)
        
    elif ("o33" in list and "o53" in list and "o13" not in list and "1 3" in listo):
        sea(1,3)
    elif ("o15" in list and "o35" in list and "o55" not in list and "5 5" in listo):
        sea(5,5)
        
    elif ("o15" in list and "o55" in list and "o35" not in list and "3 5" in listo):
        sea(3,5)
    elif ("o35" in list and "o55" in list and "o15" not in list and "1 5" in listo):
        sea(1,5)
        
    elif ("o11" in list and "o33" in list and "o55" not in list and "5 5" in listo):
        sea(5,5)
    elif ("o11" in list and "o55" in list and "o33" not in list and "3 3" in listo):
        sea(3,3)
        
    elif ("o33" in list and "o55" in list and "o11" not in list and "1 1" in listo):
        sea(1,1)
    elif ("o15" in list and "o33" in list and "o51" not in list and "5 1" in listo):
        sea(5,1)
        
    elif ("o33" in list and "o51" in list and "o15" not in list and "1 5" in listo):
        sea(1,5)
    elif ("o15" in list and "o51" in list and "o33" not in list and "3 3" in listo):
        sea(3,3)
    else:
        cpu()
    
def p2w():
    global list
    global listsecond
    if "x13" in list:
        listsecond.remove("5 3")
    elif "x53" in list:
        listsecond.remove("1 3")
    elif "x31" in list:
        listsecond.remove("3 5")
    elif "x35" in list:
        listsecond.remove("3 1")
def cpum():
    if count.get()!=0:
        print(listo)
        if count.get()==1:
            cpustart()
        
        
        else:
            cpumain()
board1=board()
def p3w():
    global list
    global listse
    if "x13" in list and "x31" in list:
        listse.remove("5 5")
    elif "x13" in list and "x35" in list:
        listse.remove("5 1")
    elif "x35" in list and "x53" in list:
        listse.remove("1 1")
    elif "x53" in list and "x31" in list:
        listse.remove("1 5")
 
            
        


