from tkinter import Tk, PhotoImage, Label, Checkbutton, Frame, IntVar


root = Tk()
root.title("Ejemplo")

playa = IntVar()
montagna = IntVar()
rio = IntVar()


def opcionesViaje():
    opcionEscogida = ""
    if playa.get() == 1:
        opcionEscogida += " playa"
    if montagna.get() == 1:
        opcionEscogida += " montaña"
    if rio.get() == 1:
        opcionEscogida += " rio"
    textoFinal.config(text=opcionEscogida)


foto = PhotoImage(
    file="/home/martin/Desarrollo_Personal/python/graficos/agujero_negro.png")
Label(root, image=foto).pack()

frame = Frame(root)
frame.pack()

Label(frame, text="Elige destino", width=50).pack()
Checkbutton(frame, text="Playa", variable=playa,
            onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montagna,
            onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Rio", variable=rio,
            onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal = Label(frame)
textoFinal.pack()

root.mainloop()
