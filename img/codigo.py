from tkinter import*
import random
from tkinter import messagebox

# cuando el usuario elige piedra 
def piedra_usuario():
    messagebox.showinfo("","opcion piedra")
    # opcion de la maquina
    maq = random.randint(1,3)
    if maq == 1: 
        resultado = "empate, la maquina eligio piedra"
    elif maq == 2:
        resultado = "perdiste, la maquina eligio papel"
    else:
        resultado = "ganaste, la maquina eligio tijera"
    t_resultados.insert(INSERT, resultado + "\n")
# cuando el usuario elige papel
def papel_usuario():
    messagebox.showinfo("","opcion papel")
    # opcion de la maquina
    maq = random.randint(1,3)
    if maq == 1: 
        resultado = "ganaste, la maquina eligio piedra"
    elif maq == 2:
        resultado = "empate, la maquina eligio papel"
    else:
        resultado = "perdiste, la maquina eligio tijera"
    t_resultados.insert(INSERT, resultado + "\n")

# cuando el usuario elige tijera
def tijera_usuario():
    messagebox.showinfo("","opcion tijera")
    # opcion de la maquina
    maq = random.randint(1,3)
    if maq == 1: 
        resultado = "perdiste, la maquina eligio piedra"
    elif maq == 2:
        resultado = "ganaste, la maquina eligio papel"
    else:
        resultado = "empate, la maquina eligio tijera"
    t_resultados.insert(INSERT, resultado + "\n")

ventana = Tk()
ventana.title("juan fernando santana cala")
ventana.geometry("900x500")
ventana.resizable(0,0)
ventana.config(bg="black")

frame_1= Frame(ventana)
frame_1.config(bg="red", width=880,height=240)
frame_1.place(x=10,y=10)

# etiqueta para el titulode la app
titulo = Label(frame_1,text=" Colegio San José de Guanenta")
titulo.config(bg="red", fg="black",font=("arial",20))
titulo.place(x=220,y=10)
# Etiqueta para subtitulo 1 de la app
subtitulo1 = Label(frame_1,text="  Especialidad en sistemas")
subtitulo1.config(bg="red",fg="black",font=("arial",18))
subtitulo1.place(x=250,y=45)
#Etiqueta subtitulo2
subtitulo2 = Label(frame_1,text="PIEDRA PAPEL O TIJERA")
subtitulo2.config(bg="red",fg="black",font=("arial",30),anchor=CENTER)
subtitulo2.place(x=180,y=120)

#_-------------------------
# frame 2 - panel de operaciones
#--------------------------
frame_2= Frame(ventana)
frame_2.config(bg="red", width=880,height=120)
frame_2.place(x=10,y=260)
img_bt_piedra = PhotoImage(file="img/piedra.png")
bt_piedra = Button(frame_2, image = img_bt_piedra, width = 105, height = 105, command=piedra_usuario)
bt_piedra.place(x =100, y = 7)
img_bt_papel = PhotoImage(file="img/papel.png")
bt_papel = Button(frame_2, image = img_bt_papel, width = 105, height = 105, command=papel_usuario)
bt_papel.place(x =337, y = 7)
img_bt_tijeras = PhotoImage(file="img/tijera.png")
bt_papel = Button(frame_2, image = img_bt_tijeras, width = 105, height = 105, command=tijera_usuario)
bt_papel.place(x = 570, y = 7)


#--------------------------
# frame 3 -Resultado
#--------------------------
frame_3= Frame(ventana)
frame_3.config(bg="red", width=880,height=120)
frame_3.place(x=14,y= 390)
# area de texto
t_resultados = Text(frame_3, width=54, height=3)
t_resultados.config(bg="red", fg="black", font=("Courier", 20))
t_resultados.pack()
#Metodo principal quedespiega la ventana en pantalla
ventana.mainloop()














