
from tkinter import Tk
from botones import Botones


class App():
    def __init__(self):
        self.root = Tk()
        self.boton = Botones(self.root)

    def InterfazGrafica(self):
        self.boton.elegir()
        self.root.mainloop()


if __name__ == "__main__":
    administracion = App()
    administracion.InterfazGrafica()
