from tkinter import messagebox
from frame_actor import Actor
import sqlite3


class ActorServiceDB():

    def borrarCampos(self):
        Actor.keyID.set("")
        Actor.nombre.set("")
        Actor.apellido.set("")
        Actor.edad.set("")

    def crear(self):
        miConexion = sqlite3.connect("VideClub")
        miCursor = miConexion.cursor()
        datos = Actor.nombre.get(), Actor.apellido.get(), Actor.edad.get()
        miCursor.execute(
            "INSERT INTO Datos_Actor VALUES(NULL, ?, ?, ?, ?, ?)",
            (datos)
        )
        miConexion.commit()
        messagebox.showinfo("DB", "Tabla Datos_Pelicula creada con exito")

    def leer(self):
        miConexion = sqlite3.connect("VideClub")
        miCursor = miConexion.cursor()
        miCursor.execute(
            "SELECT * FROM Datos_Actor WHERE ID=" +
            Actor.keyID.get())
        # nos devuelve un array con los registros
        elUsuario = miCursor.fetchall()
        for usuario in elUsuario:
            Actor.keyID.set(usuario[0])
            Actor.nombre.set(usuario[1])
            Actor.apellido.set(usuario[3])
            Actor.edad.set(usuario[4])
        miConexion.commit()

    def actualizar(self):
        miConexion = sqlite3.connect("VideClub")
        miCursor = miConexion.cursor()
        datos = Actor.nombre.get(), Actor.apellido.get(), Actor.edad.get()
        miCursor.execute(
            "UPDATE Datos_Actor SET\
                Nombre_Usuario=?, Password=?, Apellido=?,\
                Direccion=?, Comentarios=?" +
            "WHERE ID=" + Actor.keyID.get(), (datos)
        )
        miConexion.commit()
        messagebox.showinfo("DB", "Registro actualizado con exito")

    def eliminar(self):
        miConexion = sqlite3.connect("VideClub")
        miCursor = miConexion.cursor()
        miCursor.execute(
            "DELETE FROM Datos_Actor WHERE ID=" +
            Actor.keyID.get())
        miConexion.commit()
        messagebox.showinfo("DB", "Registro borrado con exito")
