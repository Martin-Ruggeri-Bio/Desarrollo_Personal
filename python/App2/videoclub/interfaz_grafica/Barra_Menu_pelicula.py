from tkinter import Tk, Menu, Frame
from db_pelicula_service import PeliculaServiceDB
from frame_pelicula import Pelicula

# --------------------Barra de Menu------------------------
root = Tk()
framePelicula = Frame(root)
framePelicula.pack()
barraMenu = Menu(framePelicula)
# framePelicula.config(menu=barraMenu, width=300, height=300)
pelicula = PeliculaServiceDB()

DBMenu = Menu(barraMenu, tearoff=0)
DBMenu.add_command(
    label="Conectar a Pelicula", command=pelicula.conexionDB)
DBMenu.add_command(
    label="salir",
    command=pelicula.cerrarConexionDB(framePelicula))

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(
    label="Borrar campos de pelicula",
    command=pelicula.borrarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(
    label="Crear Pelicula", command=pelicula.crear)
crudMenu.add_command(
    label="Leer Pelicula", command=pelicula.leer)
crudMenu.add_command(
    label="Actualizar Pelicula", command=pelicula.actualizar)
crudMenu.add_command(
    label="Borrar Pelicula", command=pelicula.eliminar)

barraMenu.add_cascade(label="DB", menu=DBMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)

framePelicula = Frame(root)
framePelicula.pack()
pelicula = Pelicula(framePelicula)
pelicula.cuadros()
pelicula.label()

root.mainloop()
