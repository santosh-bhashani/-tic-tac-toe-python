from tkinter import *
root=Tk()
list=[]
class board:
    def __init__(self,a=0,color="white"):
        self.color=color
        self.a=Canvas(root,height=1000,width=1000,bg=self.color)
        self.a.bind("<Button-1>",click)
        self.a.pack()
        self.creboard()
        self.mb=  Menubutton ( self.a, text="BOARD COLOR",bg="grey" )
        
        self.mb.menu =  Menu ( self.mb, tearoff = 0 )
        self.mb["menu"] =  self.mb.menu

        

        self.mb.menu.add_command( label="blue",command=lambda:self.bc("blue") )
        self.mb.menu.add_command ( label="green",command=lambda:self.bc("green"))
        self.mb.menu.add_command ( label="red",command=lambda:self.bc("red"))
        self.mb.menu.add_command ( label="green",command=lambda:self.bc("white") )
        self.mb.menu.add_command ( label="green",command=lambda:self.bc("orange") )
        

        self.mb.place(x=800,y=400)
        b1=Button(self.a,text="renew game",bg="white",command=self.renew1)
        b1.place(x=800,y=100)
    def x(self,g,h):
        self.linex1=self.a.create_line(g-50,h-50,g+50,h+50,width=5)
        self.linex2=self.a.create_line(g+50,h-50,g-50,h+50,width=5)
    def creboard(self):
        line1=self.a.create_line(200,0,200,600)
        line2=self.a.create_line(400,0,400,600)
        line3=self.a.create_line(0,200,600,200)
        line4=self.a.create_line(0,400,600,400)
    def o(self,g,h):
        circle=self.a.create_oval(g-50,h-50,g+50,h+50,width=5)
    def bc(self,color):
        self.a.config(bg=color)
    def cl(self,g,h,i,j):
        self.lineu1=self.a.create_line(g,h,i,j,width=5)
        
    def renew1(self):
        self.a.delete("all")
        self.creboard()
        #self.a=board()
        global list
        list=[]
        count.set(0)

        
def win2(t,u,v,w):
    global list
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
    if count.get()==9 and winner==None:
        messagebox.showinfo("winner","match tie")
        board1.renew1()
            
     
            
def win():

    win2("11","31","51",1)
    win2("13","33","53",2)
    win2("15","35","55",3)
    win2("11","13","15",4)
    win2("31","33","35",5)
    win2("51","53","55",6)
    win2("11","33","55",7)
    win2("15","33","51",8)
    
        
        
    
        
def sea(i,j):
    global list
    if ("x"+str(i)+str(j)) not in list and ("o"+str(i)+str(j)) not in list :
        if count.get()%2==0:
            board1.x(i*100,100*j)
            list.append("x"+str(i)+str(j))
        else:
            board1.o(i*100,100*j)
            list.append("o"+str(i)+str(j))
        
        count.set(count.get()+1)
        print(list)
        print(count.get())
    win()
        
    

count=IntVar()
count.set(0)

def click(event):
    
    for j in range(1,6,2):
        if(j-1)*100<event.y<(j+1)*100:
            for i in range(1,6,2):
                if (i-1)*100<event.x<(i+1)*100 :
                    sea(i,j)
                    break
            break

board1=board()

            
        


