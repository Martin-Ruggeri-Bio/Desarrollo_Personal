from tkinter import Tk, IntVar, Radiobutton, Label


def imprimir():
    if sexOpcion.get() == 1:
        Label(root, text="has elegido masculino").pack()
    else:
        Label(root, text="has elegido femenino").pack()


root = Tk()

Label(root, text="Género:").pack()

sexOpcion = IntVar()
Radiobutton(root, text="Masculino", variable=sexOpcion,
            value=1, command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=sexOpcion,
            value=2, command=imprimir).pack()


root.mainloop()
