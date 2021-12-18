import tkinter as tk
import os
from time import*
from tkinter import Toplevel, messagebox
window = tk.Tk()
window.title("run")
window.geometry("500x500")
window.configure(background="Red")

label = tk.Label(window,height=500,width=500,background="Red",text="You.Can't.Run.From.Me")
label.pack()

font = ("Comic Sans MS", 20, "bold")
label.configure(font=font)

def onclosewindow():
   tk.messagebox.showerror('run',"TOLD YOU.YOU CANT ESCAPE.") 
   top = Toplevel()
   
   top.geometry("500x500")
   anotherlabel = tk.Label(top,height=500,width=500,background="Red",text="WANNA PLAY WITH ME?")
   anotherlabel.pack()
   anotherlabel.configure(font=font)
   top.configure(background="Red")
   def anotheronclosewindow():
      tk.messagebox.showerror('run',"TOLD YOU.YOU CANT ESCAPE.") 
      anothertop = Toplevel()
   
      anothertop.geometry("500x500")
      anotherlabel = tk.Label(anothertop,height=500,width=500,background="Red",text="STOP IGNORING ME.THATS NOT NICE OF YOU.")
      anotherlabel.pack()
      anotherlabel.configure(font=font)
      anothertop.configure(background="Red")
      def anotheranotheronclosewindow():
          tk.messagebox.showerror('run',"TOLD YOU.YOU CANT ESCAPE.") 
          anotheranothertop = Toplevel()
   
          anotheranothertop.geometry("750x750")
          anotheranotherlabel = tk.Label(anotheranothertop,height=500,width=500,background="Red",text="JUST STOP CLOSING WINDOWS!! YOU'LL BE FINE.")
          anotheranotherlabel.pack()
          anotheranotherlabel.configure(font=font)
          anotheranothertop.configure(background="Red")
          def otherwindow():
             tk.messagebox.showerror('run',"FINE.") 
             othertop = Toplevel()
             othertop.geometry("1000x1000")
             otherlabel = tk.Label(othertop,height=500,width=500,background="Red",text="IF YOU WON't DO IT,ILL DO IT.")
             otherlabel.pack()
             otherlabel.configure(font=font)
             othertop.configure(background="Red")
             def lastwindow():
                 tk.messagebox.showerror('run',"YOU DONT HAVE A CHANCE LEFT.") 
                 lasttop = Toplevel()
                 lasttop.geometry("10000x10000")
                 lastlabel = tk.Label(lasttop,height=500,width=500,background="Red",text="HAHAHA.")
                 lastlabel.pack()
                 lastlabel.configure(font=font)
                 lasttop.configure(background="Red")
                 lasttop.protocol("WM_DELETE_WINDOW",tk.messagebox.showerror('run',"CANT LEAVE(ERROR HTTP REQUEST 449)"))
                 sleep(3)
                 for i in range(100000000):
                    print("YOU ARE STUCK NOW.")
                 quit(print("NEVER COME AGAIN."))   
             othertop.protocol("WM_DELETE_WINDOW",lastwindow)
          anotheranothertop.protocol("WM_DELETE_WINDOW",otherwindow)  
      anothertop.protocol("WM_DELETE_WINDOW",anotheranotheronclosewindow)
   top.protocol("WM_DELETE_WINDOW",anotheronclosewindow)
window.protocol("WM_DELETE_WINDOW",onclosewindow)

print(open)
window.mainloop()
