from tkinter import *


def crear(numero):
    contador = 0
    rows = 0
    a = Tk()

    while contador < numero:
        
        button = Button(a, text = "Ayy"). grid(row = rows, column = contador)
        rows +=1
        contador += 1
        if  rows ==4:
            rows = 0

    a.mainloop()
    
    
