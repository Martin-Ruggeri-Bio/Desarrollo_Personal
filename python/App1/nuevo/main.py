from interfaz import Interfaz_Menu
from tkinter import Tk

if __name__ == "__main__":
    root = Tk()
    menu = Interfaz_Menu(root)
    menu.opciones_de_menu()
    root.mainloop()
