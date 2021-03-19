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

Weapon = ['Puño americano', 'Daga', 'Baston retractil', 'Veneno', 'Revolver']
Room = ['Cocina', 'Librero', 'Estudio', 'Sala Comun', 'Salon de Baile']
People = ['Ronny', 'The King', 'El Coronel', 'Wendy', 'Annie']
History = ['Final 1', 'Final 2', 'Final 3', 'Final 4', 'Final 5']

################################################################################################################################################
########################### ETIQUETAS ##########################################################################################################
################################################################################################################################################

titulo = tkinter.Label(ventana, text = "CLUE", font = "Algerian 100")
titulo.place(x =100, y =00)
titulo.configure(bg='#141414', fg='white')

label1 = tkinter.Label(ventana, text = "Puntos actules ", font = "Arial 15")
label1.pack()
label1.place (x = 350, y = 180)
label1.configure(bg='#141414',fg='white')

label2 = tkinter.Label(ventana, text = acumuladordados, font = "Arial 15")
label2.pack()
label2.place(x = 350, y = 220)
label2.configure(bg='white')



#------------------MAPA-------------------------------------------------------------------------

canvas = Canvas(width = 1024, height = 1024, bg='black')
canvas.pack()

photo = PhotoImage(file='Mapa CLUE.PNG')
#La imagen del mapa debe estar en el mismo lugar que el ejecutable.
canvas.create_image(0,0, image = photo , anchor=NW)
canvas.configure(bg='#141414')
canvas.place(x=750, y = 0)

canvas2 = Canvas(width = 300, height = 300, bg='black')
canvas2.place( x=0, y = 0)
canvas2.pack()

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



################################################################################################################################################
########################### BOTONES ##########################################################################################################
################################################################################################################################################

#....................VENTANA PRINCIPAL......................................................

botondado =tkinter.Button(ventana, text = "Girar dado", padx = 64, pady = 5,command= onclick, font = "Arial 15" )
botondado.pack()
botondado.place(x = 10, y = 480)

#--------------------VENTANA DADOS----------------------------------------------------------
abrirVentana1 = Button(Otraventana, text="Regresar a Pantalla principal", bg="black", font= ("Times New Roman", 12), fg="white", command=funcion2)
abrirVentana1.pack()
################################################################################################################################################
########################### BOTONES ##########################################################################################################
################################################################################################################################################


def next2():
    Historia2.destroy()  
    
Historia2 = Canvas(width = 1800, height = 1000, bg='black')
Historia2.pack()
Historia2.configure(bg='#141414')
Historia2.place(x=0, y = 0)

titulo2 = tkinter.Label(Historia2, text = "A continuación:", font = "Algerian 90")
titulo2.place(x =100, y =10)
titulo2.configure(bg='#141414', fg='white')

T2 = tkinter.Text(Historia2, height=30, width=80)
T2.pack()
quote2 = """Al momento de la celebración del ensayo es obvio que se debe de dar un brindis, al momento en 
el que los invitados dar un trago al burbujeante sabor de la champaña no se percatan de que tal bebida 
cuenta con un ingrediente extra, 15 minutos después de haber bebido de la copa, se van desmayando uno a
 uno de donde se encuentran y quienes son, fue en aquel momento en el cual el asesino toma la decisión 
 de efectuar su atentado, el asesino sabiendo que se acaba el tiempo para recoger el cadáver decide 
 llevarlo a otra habitación solo teniendo 5 opciones: la cocina, la librería, el estudio, la sala común,
 y por último el salón de baile, toma el cuerpo desmayado de la victima llevándolo a una habitación realiza
 la ejecución y rápidamente escondiendo el arma homicida y dejando el cadáver en la habitación y
 regresado al comedor para tomar de la copa para así pasar desapercibido.
Despiertas inconsciente en el comedor, te percatas de que, así como tú te estas levantando los demás 
invitados están recuperando su aliento y fuerzas, pues ninguno de ellos sabe que ha sucedido, y deciden
 recorrer las habitaciones para descubrir pistas de lo que ha ocurrido.
"""
T2.insert(tkinter.END, quote2)
T2.configure(bg = '#141414', fg = 'red',font=('Tempus Sans ITC', 28, 'bold'))
T2.place(x=30, y =150)

botonnext2 =tkinter.Button(Historia2, text = "Siguiente",command= next2 ,bg = "#141414" ,fg = "white", font = "Arial 15")
botonnext2.pack()
botonnext2.place(x = 1500, y = 50)


def next1():
    Historia1.destroy()  

Historia1 = Canvas(width = 1800, height = 1000, bg='black')
Historia1.pack()
Historia1.configure(bg='#141414')
Historia1.place(x=0, y = 0)

titulo1 = tkinter.Label(Historia1, text = "Inicio:", font = "Algerian 90")
titulo1.place(x =100, y =10)
titulo1.configure(bg='#141414', fg='white')

T = tkinter.Text(Historia1, height=30, width=62)
T.pack()
quote = """Estando cercas las fechas de la nupcia entre Duquesa Qin y el magnate "Papa" Jhons se realizan los 
ensayos de dicha celebracion en la mansion de Ronald, pues este es el padrino. 
Entre los invitaos mas destacados se encuentra el ya mencionado dueño del monopolio McDonald: Ronal "Ronny" McDonald, el excoronel Harold  "El Coronel" Sanders, la famosa ingeniera Annie 
Copeland,la multimilloniaria Wendy Lou Thomas, el autoproclamado "The King". 
Y en un acto para afiansar negocios con Jhon se encuentra el destacado hombre de negocios y 
aristocrata Julios "Little" Caesar, entre otros invitados allegados a la pareja."""
T.insert(tkinter.END, quote)
T.configure(bg = '#141414', fg = 'red',font=('Tempus Sans ITC', 30, 'bold'))
T.place(x=30, y =150)

botonnext1 =tkinter.Button(Historia1, text = "Siguiente",command= next1 ,bg = "#141414" ,fg = "white", font = "Arial 15")
botonnext1.pack()
botonnext1.place(x = 1500, y = 50)

def next0():
    ventana.geometry("1800x1000")
    Historia0.destroy()  
    
    
Historia0 = Canvas(width = 1800, height = 1100, bg='black')
Historia0.pack()
Historia0.place(x = 0, y= 0)
Historia0.configure(bg='#141414')
carta = PhotoImage(file='carta.PNG')
Historia0.create_image(400,0, image = carta, anchor=NW)

T1 = tkinter.Text(Historia0, height=10, width=10)
T1.pack()
quote1 = """Has recibido 
una carta...."""
T1.insert(tkinter.END, quote1)
T1.configure(bg = '#141414', fg = 'red',font=('Tempus Sans ITC', 30, 'bold'))
T1.place(x=0, y =0)

botonnext0 =tkinter.Button(Historia0, text = "Siguiente",command= next0 ,bg = "#141414" ,fg = "white", font = "Arial 15")
botonnext0.pack()
botonnext0.place(x = 20, y = 350)


################################################################################################################################################
####################  SELECCION ##########################################################################################################
################################################################################################################################################

def ronny():
    champ = PhotoImage(file='Ronny_face.png')
    
def king():
    champ = PhotoImage(file='The King.png')
    
def coronel():
    champ = PhotoImage(file='Coronel_face.png')
    
def wendi():
    champ = PhotoImage(file='Wendy_face.png')
    
def annie():
    champ = PhotoImage(file='Annie_face.png')
    
    
personajes = Canvas(width = 2000, height = 1000, bg='black')
personajes.pack()
personajes.configure(bg='#141414')
personajes.place(x=0, y = 0)

ronny = PhotoImage(file='Ronny.PNG')
king = PhotoImage(file='The King_1.PNG')
coronel = PhotoImage(file='El Coronel.PNG')
wendy = PhotoImage(file='Wendy.PNG')
annie = PhotoImage(file='Annie.PNG')

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


#La imagen del mapa debe estar en el mismo lugar que el ejecutable.
champ1 = PhotoImage(file='Ronny_face.png')
champ2 = PhotoImage(file='The King_face1.png')
champ3 = PhotoImage(file='Coronel_face.png')
champ4 = PhotoImage(file='Wendy_face.png')
champ5 = PhotoImage(file='Annie_face.png')


def ronny1():
    ventana.geometry("1500x1100")
    canvas2.create_image(0,0, image = champ1 , anchor=NW)
    canvas2.place( x=10, y = 150)
    personajes.destroy()  
    
def king1():
    ventana.geometry("1500x1100")
    canvas2.create_image(0,0, image = champ2 , anchor=NW)
    canvas2.place( x=10, y = 150)
    personajes.destroy()  
    
def coronel1():
    ventana.geometry("1500x1100")
    canvas2.create_image(0,0, image = champ3 , anchor=NW)
    canvas2.place( x=10, y = 150)
    personajes.destroy()  

def wendy1():
    ventana.geometry("1500x1100")
    canvas2.create_image(0,0, image = champ4 , anchor=NW)
    canvas2.place( x=10, y = 150)
    personajes.destroy()  

def annie1():
    ventana.geometry("1500x1100")
    canvas2.create_image(0,0, image = champ5 , anchor=NW)
    canvas2.place( x=10, y = 150)
    personajes.destroy()     
    
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
    

def ventronny1():
    ventronny.state(newstate = "normal")
    ventana.state(newstate = "withdraw") 
    
def ventking1():
    ventking.state(newstate = "normal")
    ventana.state(newstate = "withdraw")    
    
def ventcoronel1():
    ventcoronel.state(newstate = "normal")
    ventana.state(newstate = "withdraw")
    
def ventwendy1():
    ventwendy.state(newstate = "normal")
    ventana.state(newstate = "withdraw")     
    
def ventannie1():
    ventannie.state(newstate = "normal")
    ventana.state(newstate = "withdraw")
    
    
#--------RONNY----------------------------------------------------------------
    
ventronny = Toplevel()
ventronny.geometry("900x300")
ventronny.state(newstate = "withdraw")
ventronny.title("RONNY")
ventronny.configure(bg='#141414')

personajes1 = Canvas(ventronny, bg='black')
personajes1.pack()
personajes1.configure(bg='#141414')
personajes1.place(x=0, y = 0)
personajes1.create_image(0,0, image = ronny, anchor=NW)

lbronny = tkinter.Label(ventronny, text = "Puntos obtenidos", font = "Arial 15")
lbronny.pack()
lbronny.configure(bg='#141414',fg='white')
lb2ronny = tkinter.Label(ventronny, text = "hola", font = "Arial 15")
lb2ronny.pack()
lb2ronny.configure(bg='white')

regreso1 = Button(ventronny, text="Regresar a selección", bg="green", font= ("Times New Roman", 12), fg="yellow", command=ventkingoff)
regreso1.pack()


#------------KING------------------------------------------------------------

ventking = Toplevel()
ventking.state(newstate = "withdraw")
ventking.title("THE KING")
ventking.configure(bg='#141414')

personajes2 = Canvas(ventking, bg='black')
personajes2.pack()
personajes2.configure(bg='#141414')
personajes2.place(x=0, y = 0)
personajes2.create_image(0,0, image = ronny, anchor=NW)

lbking = tkinter.Label(ventking, text = "Puntos obtenidos", font = "Arial 15")
lbking.pack()
lbking.configure(bg='#141414',fg='white')
lb2king = tkinter.Label(ventking, text = "hola", font = "Arial 15")
lb2king.pack()
lb2king.configure(bg='white')

regreso3 = Button(ventking, text="Regresar a selección", bg="green", font= ("Times New Roman", 12), fg="yellow", command=ventcoroneloff)
regreso3.pack()


#-------------CORONEL---------------------------------------------------------

ventcoronel = Toplevel()
ventcoronel.state(newstate = "withdraw")
ventcoronel.title("EL CORONEL")
ventcoronel.configure(bg='#141414')

personajes3 = Canvas(ventcoronel, bg='black')
personajes3.pack()
personajes3.configure(bg='#141414')
personajes3.place(x=0, y = 0)
personajes3.create_image(0,0, image = ronny, anchor=NW)

lbcoronel = tkinter.Label(ventcoronel, text = "Puntos obtenidos", font = "Arial 15")
lbcoronel.pack()
lbcoronel.configure(bg='#141414',fg='white')
lb2coronel = tkinter.Label(ventcoronel, text = "hola", font = "Arial 15")
lb2coronel.pack()
lb2coronel.configure(bg='white')

regreso2 = Button(ventcoronel, text="Regresar a selección", bg="green", font= ("Times New Roman", 12), fg="yellow", command=ventronnyoff)
regreso2.pack()

#------------WENDY---------------------------------------------------------

ventwendy = Toplevel()
ventwendy.state(newstate = "withdraw")
ventwendy.title("THE KING")
ventwendy.configure(bg='#141414')

personajes4 = Canvas(ventwendy, bg='black')
personajes4.pack()
personajes4.configure(bg='#141414')
personajes4.place(x=0, y = 0)
personajes4.create_image(0,0, image = ronny, anchor=NW)

lbwendy = tkinter.Label(ventwendy, text = "Puntos obtenidos", font = "Arial 15")
lbwendy.pack()
lbwendy.configure(bg='#141414',fg='white')
lb2wendy = tkinter.Label(ventwendy, text = "hola", font = "Arial 15")
lb2wendy.pack()
lb2wendy.configure(bg='white')

regreso4 = Button(ventwendy, text="Regresar a selección", bg="green", font= ("Times New Roman", 12), fg="yellow", command=ventwendyoff)
regreso4.pack()


#------------ANNIE---------------------------------------------------------

ventannie = Toplevel()
ventannie.state(newstate = "withdraw")
ventannie.title("THE KING")
ventannie.configure(bg='#141414')

personajes5 = Canvas(ventannie, bg='black')
personajes5.pack()
personajes5.configure(bg='#141414')
personajes5.place(x=0, y = 0)
personajes5.create_image(0,0, image = ronny, anchor=NW)

lbannie = tkinter.Label(ventannie, text = "Puntos obtenidos", font = "Arial 15")
lbannie.pack()
lbannie.configure(bg='#141414',fg='white')
lb2annie = tkinter.Label(ventannie, text = "hola", font = "Arial 15")
lb2annie.pack()
lb2annie.configure(bg='white')

regreso5 = Button(ventannie, text="Regresar a selección", bg="green", font= ("Times New Roman", 12), fg="yellow", command=ventannieoff)
regreso5.pack()

#-------------BOTONES INCIALES------------------------------------------------

botonronny =tkinter.Button(personajes, text = "Ronny",command= ventronny1,bg = "#141414",fg = "white", font = "Arial 15")
botonronny.pack()
botonronny.place(x = 410, y = 950)

botonking =tkinter.Button(personajes, text = "The King",command= ventking1,bg = "#141414",fg = "white", font = "Arial 15")
botonking.pack()
botonking.place(x = 800, y = 950)

botoncoronel =tkinter.Button(personajes, text = "El Coronel",command= ventcoronel1,bg = "#141414" ,fg = "white", font = "Arial 15")
botoncoronel.pack()
botoncoronel.place(x = 1735, y = 950)

botonwendy =tkinter.Button(personajes, text = "Wendy" ,command= ventwendy1,bg = "#141414" ,fg = "white", font = "Arial 15")
botonwendy.pack()
botonwendy.place(x = 100, y = 950)

botonannie =tkinter.Button(personajes, text = "Annie",command= ventannie1,bg = "#141414" ,fg = "white", font = "Arial 15")
botonannie.pack()
botonannie.place(x = 1300, y = 950)




botonronny =tkinter.Button(personajes, text = "SELECT",command= ronny1,bg = "#141414",fg = "white", font = "Arial 15")
botonronny.pack()
botonronny.place(x = 488, y = 950)

botonking =tkinter.Button(personajes, text = "SELECT",command= king1,bg = "#141414",fg = "white", font = "Arial 15")
botonking.pack()
botonking.place(x = 900, y = 950)

botoncoronel =tkinter.Button(personajes, text = "SELECT",command= coronel1,bg = "#141414" ,fg = "white", font = "Arial 15")
botoncoronel.pack()
botoncoronel.place(x = 1850, y = 950)

botonwendy =tkinter.Button(personajes, text = "SELECT" ,command= wendy1,bg = "#141414" ,fg = "white", font = "Arial 15")
botonwendy.pack()
botonwendy.place(x = 185, y = 950)

botonannie =tkinter.Button(personajes, text = "SELECT",command= annie1,bg = "#141414" ,fg = "white", font = "Arial 15")
botonannie.pack()
botonannie.place(x = 1370, y = 950)
   
# Configuración de la raíz
opcion = StringVar()



################################################################################################################################################
####################  MAIN ##########################################################################################################
################################################################################################################################################


ventana.mainloop()
Otraventana.mainloop()