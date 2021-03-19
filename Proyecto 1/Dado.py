# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 22:01:25 2021

@author: Daniel
"""


from tkinter import *
import time
import os

root = Tk()
frameCnt = 50
frames = [PhotoImage(file='Dices Try 2.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def funcion():
      Otraventana.state(newstate = "normal")
      root.state(newstate = "withdraw")

def funcion2():
      Otraventana.state(newstate = "withdraw")
      root.state(newstate = "normal") #state(newstate = "withdraw")root.deiconify, zoomed()


abrirVentana2 = Button(root, text="Abrir ventana 2", bg="green", font= ("Times New Roman", 12), fg="yellow", command=funcion)
abrirVentana2.pack()

Otraventana = Toplevel()
Otraventana.state(newstate = "withdraw")
Otraventana.title("Ventana 2")

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    Otraventana.after(100, update, ind)
label = Label(Otraventana)
label.pack() 
Otraventana.after(0, update, 0)

abrirVentana1 = Button(Otraventana, text="Abrir ventana principal", bg="green", font= ("Times New Roman", 12), fg="yellow", command=funcion2)
abrirVentana1.pack()

Otraventana.mainloop()
root.mainloop()