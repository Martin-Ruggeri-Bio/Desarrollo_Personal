from tkinter import Tk, IntVar, Radiobutton, Label


def imprimir():
    if varOpcion.get() == 1:
        Label(root, text="has elegido masculino").pack()
    else:
        Label(root, text="has elegido femenino").pack()


root = Tk()

Label(root, text="Género:").pack()

varOpcion = IntVar()
Radiobutton(root, text="Masculino", variable=varOpcion,
            value=1, command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=varOpcion,
            value=2, command=imprimir).pack()


root.mainloop()
