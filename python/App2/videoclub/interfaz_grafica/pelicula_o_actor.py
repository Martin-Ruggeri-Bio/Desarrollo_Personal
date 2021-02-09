from tkinter import Tk, Frame, Button, Menu
from conexion_bd import ConexionDB


class App_VideoClub():
    def __init__(self, root):
        self.root = root
        self.actor = 1
        self.pelicula = 0
        self.mimenu = self.menu()
        self.botones = self.button()

    def menu(self):
        barraMenu = Menu(self.root)
        salir = Menu(barraMenu, tearoff=0)
        ayudaMenu = Menu(barraMenu, tearoff=0)

        salir.add_command(
            label="Actor", command=ConexionDB(
                self.root).conectar_tablas(self.actor))
        salir.add_command(
            label="Pelicula", command=ConexionDB(
                self.root).conectar_tablas(self.pelicula))
        salir.add_command(
            label="salir", command=ConexionDB(self.root).cerrarConexionDB)

        ayudaMenu.add_command(label="Licencia")
        ayudaMenu.add_command(label="Acerca de ...")

        barraMenu.add_cascade(label="DB", menu=salir)
        barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

    def button(self):
        botones = Frame(self.root)
        botones.pack()

        botonActor = Button(
            botones, text="Actor", command=ConexionDB(
                self.root).conectar_tablas(self.actor))
        botonActor.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        botonPelicula = Button(
            botones, text="Pelicula", command=ConexionDB(
                self.root).conectar_tablas(self.pelicula))
        botonPelicula.grid(row=1, column=1, sticky="e", padx=10, pady=10)


if __name__ == "__main__":
    root = Tk()
    app = App_VideoClub(root)
    root.mainloop
