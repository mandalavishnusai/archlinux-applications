#!/usr/bin/env python3

from tkinter import *
import subprocess
import os


def installpackage():
    string1=e1.get()
    inp1=string1[26:-4]
    buildpath="programs"





    print(subprocess.run(["git","clone",string1]))
    os.chdir(inp1)
    print(subprocess.run(["makepkg","-si"]))




#creating the application main window.
top = Tk()


top.title("AUR package downloader")
top.geometry("780x150")
top.config(bg='#d8d8d8')
top.resizable(width=False, height=False)

Label(top,text="Enter AUR url  ",font=("arial",20)).grid(row=0,sticky=W,pady=4)

e1=Entry(top,width=32,font=('Arial 24'))

e1.grid(row=0,column=1,padx=10,pady=10)

Button(top,text="close",command=top.quit,fg='red',activebackground='#8B0000',activeforeground='black',width=12,font=("arial",14)).grid(row=2,column=0,sticky=W,pady=4,padx=15)

Button(top,text="install",command=installpackage,fg="red",activebackground='#00FF00',activeforeground='black',width=12,font=("arial",14)).grid(row=2,column=1,sticky=W,pady=4,padx=50)


#Entering the event main loop
top.mainloop()
