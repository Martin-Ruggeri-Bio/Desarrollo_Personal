from tkinter import Tk, Menu, Frame
from bbdd_Actor_service import ActorServiceDDBB
from frame_actor import Actor


# --------------------Barra de Menu------------------------
root = Tk()
frameActor = Frame(root)
frameActor.pack()
barraMenu = Menu(frameActor)
frameActor.config(menu=barraMenu, width=300, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(
    label="Conectar a Actor", command=ActorServiceDDBB.conexionBBDD)
bbddMenu.add_command(
    label="salir", command=ActorServiceDDBB.cerrarConexionBBDD(frameActor))

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(
    label="Borrar campos de actores",
    command=ActorServiceDDBB.borrarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(
    label="Crear Actor", command=ActorServiceDDBB.crear)
crudMenu.add_command(
    label="Leer Actor", command=ActorServiceDDBB.leer)
crudMenu.add_command(
    label="Actualizar Actor", command=ActorServiceDDBB.actualizar)
crudMenu.add_command(
    label="Borrar Actor", command=ActorServiceDDBB.eliminar)

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)

actor = Actor(frameActor)
actor.cuadros()
actor.label()

root.mainloop()
