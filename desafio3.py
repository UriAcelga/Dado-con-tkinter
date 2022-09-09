#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Al ejercicio que está en "lab2_ej2.py", el de generar un 
número aleatorio del 1 al 6, ahora debemos pasarlo a una
aplicación de escritorio.

Ahora se tirará el dado presionando un botón, y el resultado se
mostrará en una caja de texto.

Antes de mostrar cada resultado se limpia la caja, dejando el
mismo resultado hasta que se vuelve a pulsar.
"""
import tkinter as tk
import random

def tirarDado():
    global dado
    dado.set(random.randint(1, 6))

ventana = tk.Tk()
ventana.title("Dado")
ventana.config(width = 150, height = 200)

titulo = tk.Label(text="Dado de 6 caras", font=("Helvetica", 12))
titulo.place(x=10, y=15)

num = tk.Label(text="Valor:", font=("Helvetica", 18))
num.place(x=40, y=100)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Creo la variable para mostrar la tirada
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
dado = tk.StringVar()

cartel = tk.Entry(
    bd = 5,
    state = tk.DISABLED,
    textvariable = dado,
    justify="center",
    font=("Helvetica", 28, "bold")    
)
cartel.place(x=40, y=140, width=70, height=40)

tirar_dado = tk.Button(text="Tirar el Dado", command=tirarDado)
tirar_dado.place(x=20, y=45, width=110, height= 40)




ventana.mainloop()