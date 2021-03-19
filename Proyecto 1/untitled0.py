# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 19:34:17 2021

@author: Daniel
"""
#------------------LIBRERIAS-----------------------------------------------------------------
import tkinter
from tkinter import *
import tkinter.scrolledtext as st
from tkinter import messagebox as MessageBox
import time
import os
import random
#--------------------VENTANA PRINCIPAL---------------------------------------------------------

ventana = tkinter.Tk()
ventana.geometry("2000x1000")
ventana.title("THIS IS NOT A COPY OF CLUE")
ventana.configure(bg='#141414')
ventana.resizable(False, False)
#-------------------VARIABLES-------------------------------------------------------------
global dados
global acumuladordados 
dados = 0
acumuladordados = 0


#-------------------RANDOMIZADOR----------------------------------------------------------

Weapon = ['AW', 'BW', 'CW', 'DW', 'EW']
Room = ['AR', 'BR', 'CR', 'DR', 'ER']
People = ['AP', 'BP', 'CP', 'DP', 'EP']
History = ['AH', 'BH', 'CH', 'DH', 'EH','FH', 'GH']

#-------------------FUNCIONES-------------------------------------------------------------
def ronny1():
    champ = PhotoImage(file='Ronny_face.png')
    ventana.geometry("1800x1000")
    personajes.destroy()
  
def king1():
    champ = PhotoImage(file='The King.png')
    ventana.geometry("1800x1000")
    personajes.destroy()
    
def coronel1():
    champ = PhotoImage(file='Coronel_face.png')
    ventana.geometry("1800x1000")
    personajes.destroy()
    
def wendy1():
    champ = PhotoImage(file='Wendy_face.png')
    ventana.geometry("1800x1000")
    personajes.destroy()
    
def annie1():
    champ = PhotoImage(file='Annie_face.png')
    ventana.geometry("1800x1000")
    personajes.destroy()

################################################################################################################################################
########################### ETIQUETAS ##########################################################################################################
################################################################################################################################################

titulo = tkinter.Label(ventana, text = "CLUE", font = "Algerian 100")
titulo.place(x =100, y =00)
titulo.configure(bg='#141414', fg='white')

label1 = tkinter.Label(ventana, text = "Puntos actules ", font = "Arial 15")
label1.pack()
label1.place (x = 300, y = 180)
label1.configure(bg='#141414',fg='white')

label2 = tkinter.Label(ventana, text = acumuladordados, font = "Arial 15")
label2.pack()
label2.place(x = 300, y = 220)
label2.configure(bg='white')


#------------------MAPA-------------------------------------------------------------------------

canvas = Canvas(width = 1024, height = 1024, bg='black')
canvas.pack()

photo = PhotoImage(file='Mapa CLUE.PNG')
#La imagen del mapa debe estar en el mismo lugar que el ejecutable.
canvas.create_image(0,0, image = photo , anchor=NW)
canvas.configure(bg='#141414')
canvas.place(x=750, y = 0)


   
################################################################################################################################################
###########################  DADOS ##########################################################################################################
################################################################################################################################################

frameCnt = 50
frames = [PhotoImage(file='Dices Try 2.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
gifdados = tkinter.Label()
gifdados.pack()


Otraventana = Toplevel()
Otraventana.state(newstate = "withdraw")
Otraventana.title("Ventana 2")
Otraventana.configure(bg='#141414')


def update(ind):

   frame = frames[ind]
   ind += 1
   if ind == frameCnt:
       ind = 0
   label.configure(image=frame)
   ventana.after(100, update, ind)
def onclick():
    global dados
    global acumuladordados  
    dados = random.randint(2, 12)
    acumuladordados = acumuladordados + dados
    label2.config(text = acumuladordados)
    puntosdado2.config(text = dados)
    
    Otraventana.state(newstate = "normal")
    ventana.state(newstate = "withdraw")
    
def funcion2():
      Otraventana.state(newstate = "withdraw")
      ventana.state(newstate = "normal") #state(newstate = "withdraw")root.deiconify, zoomed()

botondado =tkinter.Button(ventana, text = "Girar dado", padx = 64, pady = 5,command= onclick, font = "Arial 15" )
botondado.pack()
botondado.place(x = 10, y = 450)
label = tkinter.Label(ventana, bg='#141414')
label.pack() 
label.place (x=10, y =140)
Otraventana.after(0, update, 0)

#----------------------GIF DADOS---------------------------------

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

puntosdado = tkinter.Label(Otraventana, text = "Puntos obtenidos", font = "Arial 15")
puntosdado.pack()
puntosdado.configure(bg='#141414',fg='white')

puntosdado2 = tkinter.Label(Otraventana, text = dados, font = "Arial 15")
puntosdado2.pack()
puntosdado2.configure(bg='white')

abrirVentana1 = Button(Otraventana, text="Regresar a Pantalla principal", bg="green", font= ("Times New Roman", 12), fg="yellow", command=funcion2)
abrirVentana1.pack()



################################################################################################################################################
####################  SELECCION ##########################################################################################################
################################################################################################################################################

champ1 = PhotoImage(file='Ronny_face.png')
champ2 = PhotoImage(file='The King_face1.png')
champ3 = PhotoImage(file='Coronel_face.png')
champ4 = PhotoImage(file='Wendy_face.png')
champ5 = PhotoImage(file='Annie_face.png')

ventannie = Toplevel()
ventannie.state(newstate = "withdraw")
ventannie.title("ANNIE")
ventannie.configure(bg='#141414')

personajes = Canvas(width = 2000, height = 1000, bg='black')
personajes.pack()
personajes.configure(bg='#141414')
personajes.place(x=0, y = 0)

wendy = PhotoImage(file='Wendy.PNG')
personajes.create_image(-10,50, image = wendy, anchor=NW)

ronny = PhotoImage(file='Ronny.PNG')
personajes.create_image(260,50, image = ronny, anchor=NW)

annie = PhotoImage(file='Annie.PNG')
personajes.create_image(1050,50, image = annie, anchor=NW)

king = PhotoImage(file='The King_1.PNG')
personajes.create_image(600,50, image = king, anchor=NW)

coronel = PhotoImage(file='El Coronel.PNG')
personajes.create_image(1550,50, image = coronel, anchor=NW)

# -------------------------ventana info-----------------------------------------

def ventronnyoff():
      ventronny.state(newstate = "withdraw")
      ventana.state(newstate = "normal") 
      
def ventkingoff():
      ventking.state(newstate = "withdraw")
      ventana.state(newstate = "normal")
      
def ventcoroneloff():
      ventcoronel.state(newstate = "withdraw")
      ventana.state(newstate = "normal") 

def ventwendyoff():
      ventwendy.state(newstate = "withdraw")
      ventana.state(newstate = "normal")
      
def ventannieoff():
      ventannie.state(newstate = "withdraw")
      ventana.state(newstate = "normal")
    
      
#------regresar a selección--------------------------------------------------------------------------

def ventronny1():
    ventronny.state(newstate = "normal")
    ventana.state(newstate = "withdraw") 
     
def ventking1():
    ventking.state(newstate = "normal")
    ventana.state(newstate = "withdraw")    
    
def ventcoronel1():
    Otraventana.state(newstate = "normal")
    ventana.state(newstate = "withdraw")
    
def ventwendy1():
    Otraventana.state(newstate = "normal")
    ventana.state(newstate = "withdraw")     
    
def ventannie1():
    Otraventana.state(newstate = "normal")
    ventana.state(newstate = "withdraw")

#

#-------------ventanas info-----------------------------------------------------------------------------

   
ventronny = Toplevel()
ventronny.geometry("900x300")
ventronny.state(newstate = "withdraw")
ventronny.title("RONNY")
ventronny.configure(bg='#141414')

personajes1 = Canvas(ventronny, bg='black')
personajes1.pack()
personajes1.configure(bg='#141414')
personajes1.place(x=0, y = 0)
ronnyimg = PhotoImage(file='Ronny.PNG')
personajes1.create_image(0,0, image = ronnyimg, anchor=NW)

lbronny = tkinter.Label(ventronny, text = "Puntos obtenidos", font = "Arial 15")
lbronny.pack()
lbronny.configure(bg='#141414',fg='white')
lb2ronny = tkinter.Label(Otraventana, text = "hola", font = "Arial 15")
lb2ronny.pack()
lb2ronny.configure(bg='white')

regreso1 = Button(ventronny, text="Regresar a selección", bg="green", font= ("Times New Roman", 12), fg="yellow", command=ventannieoff)
regreso1.pack()



ventking = Toplevel()
ventking.state(newstate = "withdraw")
ventking.title("THE KING")
ventking.configure(bg='#141414')

botonking = Button(ventking, text = "Girar dado", padx = 64, pady = 5,command= onclick, font = "Arial 15" )
botonking.pack()
botonking.place(x = 10, y = 450)
labelk =  Label(ventana, bg='#141414')
labelk.pack() 
labelk.place (x=10, y =140)



ventcoronel = Toplevel()
ventcoronel.state(newstate = "withdraw")
ventcoronel.title("EL CORONEL")
ventcoronel.configure(bg='#141414')

botoncoro = Button(ventcoronel, text = "Girar dado", padx = 64, pady = 5,command= onclick, font = "Arial 15" )
botoncoro.pack()
botoncoro.place(x = 10, y = 450)
labelc =  Label(ventana, bg='#141414')
labelc.pack() 
labelc.place (x=10, y =140)



ventwendy = Toplevel()
ventwendy.state(newstate = "withdraw")
ventwendy.title("WENDY")
ventwendy.configure(bg='#141414')

botonwendy = Button(ventwendy, text = "Girar dado", padx = 64, pady = 5,command= onclick, font = "Arial 15" )
botonwendy.pack()
botonwendy.place(x = 10, y = 450)
labelw = tkinter.Label(ventana, bg='#141414')
labelw.pack() 
labelw.place (x=10, y =140)




botonannie = Button(ventannie, text = "Girar dado", padx = 64, pady = 5,command= onclick, font = "Arial 15")
botonannie.pack()
botonannie.place(x = 10, y = 450)
labela = tkinter.Label(ventana, bg='#141414')
labela.pack() 
labela.place (x=10, y =140)




personajes = Canvas(width = 2000, height = 1000, bg='black')
personajes.pack()
personajes.configure(bg='#141414')
personajes.place(x=0, y = 0)

wendy = PhotoImage(file='Wendy.PNG')
personajes.create_image(-10,50, image = wendy, anchor=NW)

ronny = PhotoImage(file='Ronny.PNG')
personajes.create_image(260,50, image = ronny, anchor=NW)

annie = PhotoImage(file='Annie.PNG')
personajes.create_image(1050,50, image = annie, anchor=NW)

king = PhotoImage(file='The King_1.PNG')
personajes.create_image(600,50, image = king, anchor=NW)

coronel = PhotoImage(file='El Coronel.PNG')
personajes.create_image(1550,50, image = coronel, anchor=NW)



#--------VENTANAS ACEPTAR CHAMP----------------------------------------------------------------------

def ronny1():
    ventana.geometry("1800x1000")
    canvas2 = Canvas(width = 1024, height = 1024, bg='black')
    canvas2.create_image(0,0, image = champ1 , anchor=NW)
    canvas2.place(x=0, y = 100)
    canvas2.pack()
    personajes.destroy()  
    
def king1():
    ventana.geometry("1800x1000")
    canvas2 = Canvas(width = 1024, height = 1024, bg='black')
    canvas2.create_image(0,0, image = champ2 , anchor=NW)
    canvas2.place(x=0, y = 100)
    canvas2.pack()
    personajes.destroy()
    
def coronel1():
    ventana.geometry("1800x1000")
    canvas2 = Canvas(width = 1024, height = 1024, bg='black')
    canvas2.create_image(0,0, image = champ3 , anchor=NW)
    canvas2.place(x=0, y = 100)
    canvas2.pack()
    personajes.destroy()

def wendy1():
    ventana.geometry("1800x1000")
    canvas2 = Canvas(width = 1024, height = 1024, bg='black')
    canvas2.create_image(0,0, image = champ4 , anchor=NW)
    canvas2.place(x=0, y = 100)
    canvas2.pack()
    personajes.destroy()

def annie1():
    ventana.geometry("1800x1000")
    canvas2 = Canvas(width = 1024, height = 1024, bg='black')
    canvas2.create_image(0,0, image = champ5 , anchor=NW)
    canvas2.place(x=0, y = 100)
    canvas2.pack()
    personajes.destroy()    
    


botonronny =tkinter.Button(personajes, text = "Ronny",command= ventronny1,bg = "#141414",fg = "white", font = "Arial 15")
botonronny.pack()
botonronny.place(x = 460, y = 950)

botonking =tkinter.Button(personajes, text = "The King",command= ventking1,bg = "#141414",fg = "white", font = "Arial 15")
botonking.pack()
botonking.place(x = 800, y = 950)

botoncoronel =tkinter.Button(personajes, text = "El Coronel",command= ventcoronel1,bg = "#141414" ,fg = "white", font = "Arial 15")
botoncoronel.pack()
botoncoronel.place(x = 1750, y = 950)

botonwendy =tkinter.Button(personajes, text = "Wendy" ,command= ventwendy1,bg = "#141414" ,fg = "white", font = "Arial 15")
botonwendy.pack()
botonwendy.place(x = 100, y = 950)

botonannie =tkinter.Button(personajes, text = "Annie",command= ventannie1,bg = "#141414" ,fg = "white", font = "Arial 15")
botonannie.pack()
botonannie.place(x = 1300, y = 950)




botonronny2 =tkinter.Button(personajes, text = "SELECT",command= ronny1,bg = "#141414",fg = "white", font = "Arial 15")
botonronny2.pack()
botonronny2.place(x = 560, y = 950)

botonking2 =tkinter.Button(personajes, text = "SELECT",command= king1,bg = "#141414",fg = "white", font = "Arial 15")
botonking2.pack()
botonking2.place(x = 900, y = 950)

botoncoronel2 =tkinter.Button(personajes, text = "SELECT",command= coronel1,bg = "#141414" ,fg = "white", font = "Arial 15")
botoncoronel2.pack()
botoncoronel2.place(x = 1850, y = 950)

botonwendy2 =tkinter.Button(personajes, text = "SELECT" ,command= wendy1,bg = "#141414" ,fg = "white", font = "Arial 15")
botonwendy2.pack()
botonwendy2.place(x = 200, y = 950)

botonannie2 =tkinter.Button(personajes, text = "SELECT",command= annie1,bg = "#141414" ,fg = "white", font = "Arial 15")
botonannie2.pack()
botonannie2.place(x = 1400, y = 950)

ventronny.mainloop()
ventcoronel.mainloop()
ventking.mainloop()
ventwendy.mainloop()
ventannie.mainloop()
Otraventana.mainloop()
ventana.mainloop()