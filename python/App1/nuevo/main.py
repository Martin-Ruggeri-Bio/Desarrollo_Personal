from barraMenu import BarraMenu
from tkinter import Tk


class App():
    def __init__(self):
        self.root = Tk()
        self.barraMenu = BarraMenu(self.root)

    def InterfazGrafica(self):
        self.barraMenu.opciones_de_menu()
        self.root.mainloop()


if __name__ == "__main__":
    administracion = App()
    administracion.InterfazGrafica()
