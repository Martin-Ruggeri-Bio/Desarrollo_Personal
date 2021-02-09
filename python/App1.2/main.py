from interfaz import Interfaz_CuadrosTextos, Interfaz_Label, Interfaz_Menu
from tkinter import Tk

if __name__ == "__main__":
    root = Tk()
    menu = Interfaz_Menu(root)
    menu.opciones_de_menu()
    cuadros_de_textos = Interfaz_CuadrosTextos(root)
    cuadros_de_textos.grid()
    cuadros_de_textos.pack()
    labels = Interfaz_Label(root)
    labels.grid()
    labels.pack()
    root.mainloop()
