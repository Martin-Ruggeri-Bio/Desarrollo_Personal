from tkinter import Tk, Menu, Frame
from db_Actor_service import ActorServiceDB
from frame_actor import Actor


# --------------------Barra de Menu------------------------
root = Tk()
frameActor = Frame(root)
frameActor.pack()
barraMenu = Menu(frameActor)
# frameActor.config(menu=barraMenu, width=300, height=300)
actor = ActorServiceDB()

dbMenu = Menu(barraMenu, tearoff=0)
dbMenu.add_command(
    label="Conectar a Actor", command=actor.conexionDB)
dbMenu.add_command(
    label="salir", command=actor.cerrarConexionDB(frameActor))

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(
    label="Borrar campos de actores",
    command=actor.borrarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(
    label="Crear Actor", command=actor.crear)
crudMenu.add_command(
    label="Leer Actor", command=actor.leer)
crudMenu.add_command(
    label="Actualizar Actor", command=actor.actualizar)
crudMenu.add_command(
    label="Borrar Actor", command=actor.eliminar)

barraMenu.add_cascade(label="DB", menu=dbMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)

actor = Actor(frameActor)
actor.cuadros()
actor.label()

root.mainloop()
