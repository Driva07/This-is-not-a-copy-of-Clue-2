import tkinter
from tkinter import *

def funcion():
      Otraventana.state(newstate = "normal")
      root.state(newstate = "withdraw")

def funcion2():
      Otraventana.state(newstate = "withdraw")
      root.state(newstate = "normal") #state(newstate = "withdraw")root.deiconify, zoomed()

frameCnt = 50
frames = [PhotoImage(file='Dices Try 2.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
gifdados = tkinter.Label()
gifdados.pack()

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
    
    MessageBox.showinfo("puntos obtenidos ", dados) # título, mensaje




root = tkinter.Tk()
root.state(newstate = "normal")
root.resizable(0, 0)
root.title("Ventana 1")

abrirVentana2 = tkinter.Button(root, text="Abrir ventana 2", bg="green", font= ("Times New Roman", 12), fg="yellow", command=funcion)
abrirVentana2.pack()

Otraventana = tkinter.Toplevel()
Otraventana.state(newstate = "withdraw")
Otraventana.geometry("250x150+300+100")
Otraventana.title("Ventana 2")

miEtiqueta = tkinter.Label(Otraventana, text="Bienvenido a la ventana 2", bg="#252850", font=("Times New Roman", 12), fg="yellow")
miEtiqueta.pack()

abrirVentana1 = tkinter.Button(Otraventana, text="Abrir ventana principal", bg="green", font= ("Times New Roman", 12), fg="yellow", command=funcion2)
abrirVentana1.pack()

label = tkinter.Label(ventana, bg='#141414')
label.pack() 
label.place (x=10, y =140)
ventana.after(0, update, 0)

Otraventana.mainloop()
root.mainloop()