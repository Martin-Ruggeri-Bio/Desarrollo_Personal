from tkinter import Tk, Frame, Button, messagebox, Menu
from bbdd_Actor_service import ActorServiceDDBB
from bbdd_pelicula_service import PeliculaServiceDDBB


def salirAplicacion(self):
    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    if valor == "yes":
        root.destroy()


root = Tk()
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(
    label="Conectar a Pelicula", command=PeliculaServiceDDBB.conexionBBDD)
bbddMenu.add_command(
    label="Conectar a Actor", command=ActorServiceDDBB.conexionBBDD)
bbddMenu.add_command(
    label="salir", command=salirAplicacion)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de ...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

eleccion = Frame(root)
eleccion.pack()

botonCrear = Button(
    eleccion, text="Actor", command=ActorServiceDDBB.conexionBBDD)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer = Button(
    eleccion, text="Pelicula", command=PeliculaServiceDDBB.conexionBBDD)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

root.mainloop()
