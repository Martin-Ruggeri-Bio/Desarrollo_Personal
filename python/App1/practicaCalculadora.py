from tkinter import Tk, Frame, Entry, Button, StringVar

raiz = Tk()
miFrame = Frame(raiz)
miFrame.pack()
operacion = ""
resultado = 0

# ------------------PANTALLA------------------------------------
numeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="White", justify="right")

# -------------------funciones_teclado-------------------------------------


def numeroPulsado(num):
    global operacion
    if operacion != "":
        numeroPantalla.set(num)
        operacion = ""
    else:
        numeroPantalla.set(numeroPantalla.get() + num)


def suma(num):
    global operacion
    global resultado
    resultado += int(num)
    operacion = "suma"
    numeroPantalla.set(resultado)


def igual():
    global resultado
    numeroPantalla.set(resultado + int(numeroPantalla.get()))
    resultado = 0


# -------------------Fila_1------------------------------------
boton7 = Button(miFrame, text="7", width=3, command=lambda: numeroPulsado("7"))
boton8 = Button(miFrame, text="8", width=3, command=lambda: numeroPulsado("8"))
boton9 = Button(miFrame, text="9", width=3, command=lambda: numeroPulsado("9"))
botonDiv = Button(miFrame, text="%", width=3)
boton7.grid(row=2, column=1)
boton8.grid(row=2, column=2)
boton9.grid(row=2, column=3)
botonDiv.grid(row=2, column=4)

# -------------------Fila_2-------------------------------------
boton4 = Button(miFrame, text="4", width=3, command=lambda: numeroPulsado("4"))
boton5 = Button(miFrame, text="5", width=3, command=lambda: numeroPulsado("5"))
boton6 = Button(miFrame, text="6", width=3, command=lambda: numeroPulsado("6"))
botonMult = Button(miFrame, text="X", width=3)
boton4.grid(row=3, column=1)
boton5.grid(row=3, column=2)
boton6.grid(row=3, column=3)
botonMult.grid(row=3, column=4)

# -------------------Fila_3-------------------------------------
boton1 = Button(miFrame, text="1", width=3, command=lambda: numeroPulsado("1"))
boton2 = Button(miFrame, text="2", width=3, command=lambda: numeroPulsado("2"))
boton3 = Button(miFrame, text="3", width=3, command=lambda: numeroPulsado("3"))
botonRest = Button(miFrame, text="-", width=3)
boton1.grid(row=4, column=1)
boton2.grid(row=4, column=2)
boton3.grid(row=4, column=3)
botonRest.grid(row=4, column=4)

# -------------------Fila_4-------------------------------------
botonC = Button(miFrame, text=",", width=3, command=lambda: numeroPulsado(","))
boton0 = Button(miFrame, text="0", width=3, command=lambda: numeroPulsado("0"))
botonIgual = Button(miFrame, text="=", width=3, command=lambda: igual())
botonSuma = Button(miFrame, text="+", width=3,
                   command=lambda: suma(numeroPantalla.get()))
botonC.grid(row=5, column=1)
boton0.grid(row=5, column=2)
botonIgual.grid(row=5, column=3)
botonSuma.grid(row=5, column=4)

raiz.mainloop()
