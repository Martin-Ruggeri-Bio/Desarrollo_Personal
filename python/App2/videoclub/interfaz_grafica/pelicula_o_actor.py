from tkinter import Tk, Frame, Button, messagebox, Menu
from db_Actor_service import ActorServiceDB
from db_pelicula_service import PeliculaServiceDB


def salirAplicacion(self):
    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    if valor == "yes":
        root.destroy()


root = Tk()
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)
actor = ActorServiceDB()
pelicula = PeliculaServiceDB()

dbMenu = Menu(barraMenu, tearoff=0)
dbMenu.add_command(
    label="Conectar a Pelicula", command=pelicula.conexionDB)
dbMenu.add_command(
    label="Conectar a Actor", command=actor.conexionDB)
dbMenu.add_command(
    label="salir", command=salirAplicacion)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de ...")

barraMenu.add_cascade(label="DB", menu=dbMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

eleccion = Frame(root)
eleccion.pack()

botonActor = Button(
    eleccion, text="Actor", command=actor.conexionDB)
botonActor.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonPelicula = Button(
    eleccion, text="Pelicula", command=pelicula.conexionDB)
botonPelicula.grid(row=1, column=1, sticky="e", padx=10, pady=10)

root.mainloop()
