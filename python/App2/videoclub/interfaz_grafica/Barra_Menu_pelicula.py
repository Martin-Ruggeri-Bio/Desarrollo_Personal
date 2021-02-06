from tkinter import Tk, Menu, Frame
from bbdd_pelicula_service import PeliculaServiceDDBB
from frame_pelicula import Pelicula

# --------------------Barra de Menu------------------------
root = Tk()
framePelicula = Frame(root)
framePelicula.pack()
barraMenu = Menu(framePelicula)
framePelicula.config(menu=barraMenu, width=300, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(
    label="Conectar a Pelicula", command=PeliculaServiceDDBB.conexionBBDD)
bbddMenu.add_command(
    label="salir",
    command=PeliculaServiceDDBB.cerrarConexionBBDD(framePelicula))

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(
    label="Borrar campos de pelicula",
    command=PeliculaServiceDDBB.borrarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(
    label="Crear Pelicula", command=PeliculaServiceDDBB.crear)
crudMenu.add_command(
    label="Leer Pelicula", command=PeliculaServiceDDBB.leer)
crudMenu.add_command(
    label="Actualizar Pelicula", command=PeliculaServiceDDBB.actualizar)
crudMenu.add_command(
    label="Borrar Pelicula", command=PeliculaServiceDDBB.eliminar)

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)

framePelicula = Frame(root)
framePelicula.pack()
pelicula = Pelicula(framePelicula)
pelicula.cuadros()
pelicula.label()

root.mainloop()
