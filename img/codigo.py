from tkinter import *
from tkinter import messagebox
import random

mag = random.randint(1,3)

ventana_principal = Tk()

# Titulo de la ventana
ventana_principal.title("Juan fernando satana cala")

# Tamaño de la ventana
ventana_principal.geometry("800x500")  

# Deshabilitar boton maximizar de la ventana
ventana_principal.resizable(0,0)

# Color de fondo de la pantalla
ventana_principal.config(bg="blue")

frame_1 = Frame(ventana_principal)
frame_1.config(bg="ivory", width=780, height=240)
frame_1.place(x=10, y=10)

titulo = Label(frame_1, text="piedra_papel_tijera")
titulo.config(bg="white", fg="black", font=("Arial", 16))
titulo.place(x=300,y=10)

titulo = Label(frame_1, text="opciones del jugador")
titulo.config(bg="yellow", fg="black", font=("Arial", 16))
titulo.place(x=300,y=70)

frame_2 = Frame(ventana_principal)
frame_2.config(bg="ivory2", width=780, height=120)
frame_2.place(x=10, y=260)

img_bt_papel = PhotoImage(file="img/papel.png")
bt_papel =  Button(frame_2, image = img_bt_papel, width=105, height=105)
#bt_papel = Button(frame_2, text="papel", width=10)
bt_papel.place(x=337, y=7)

img_bt_tijera = PhotoImage(file="img/tijera.png")
bt_tijera =  Button(frame_2, image = img_bt_tijera, width=105, height=105)
#bt_tjera = Button(frame_2, text="papel", width=10)
bt_tijera.place(x=558, y=7)

img_bt_piedra = PhotoImage(file="img/piedra.png")
bt_piedra =  Button(frame_2, image = img_bt_piedra, width=105, height=105)
#bt_piedra = Button(frame_2, text="piedra", width=10)
bt_piedra.place(x=116, y=7)


frame_3= Frame(ventana_principal)
frame_3.config(bg="ivory2", width=780, height=120)
frame_3.place(x=10, y=390)


ventana_principal.mainloop()














