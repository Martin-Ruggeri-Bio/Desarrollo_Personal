from tkinter import messagebox
from frame_pelicula import Pelicula
import sqlite3


class PeliculaServiceDB():

    def borrarCampos(self):
        Pelicula.keyID.set("")
        Pelicula.titulo.set("")
        Pelicula.genero.set("")
        Pelicula.duracion.set("")
        Pelicula.actores.set()

    def crear(self):
        miConexion = sqlite3.connect("VideClub")
        miCursor = miConexion.cursor()
        datos = Pelicula.titulo.get(), Pelicula.genero.get(),\
            Pelicula.duracion.get(), Pelicula.actores.get()
        miCursor.execute(
            "INSERT INTO Datos_Pelicula VALUES(NULL, ?, ?, ?, ?, ?)",
            (datos)
        )
        miConexion.commit()
        messagebox.showinfo("DB", "Registro insertado con exito")

    def leer(self):
        miConexion = sqlite3.connect("VideClub")
        miCursor = miConexion.cursor()
        miCursor.execute(
            "SELECT * FROM Datos_Pelicula WHERE ID=" +
            Pelicula.keyID.get())
        # nos devuelve un array con los registros
        elUsuario = miCursor.fetchall()
        for usuario in elUsuario:
            Pelicula.keyID.set(usuario[0])
            Pelicula.titulo.set(usuario[1])
            Pelicula.genero.set(usuario[3])
            Pelicula.duracion.set(usuario[1])
            Pelicula.actores.set(usuario[4])
        miConexion.commit()

    def actualizar(self):
        miConexion = sqlite3.connect("VideClub")
        miCursor = miConexion.cursor()
        datos = Pelicula.titulo.get(), Pelicula.genero.get(),\
            Pelicula.duracion.get(), Pelicula.actores.get()
        miCursor.execute(
            "UPDATE Datos_Pelicula SET\
                Titulo=?, Genero=?,\
                Duracion=?, Actores=?" +
            "WHERE ID=" + Pelicula.keyID.get(), (datos)
        )
        miConexion.commit()
        messagebox.showinfo("DB", "Registro actualizado con exito")

    def eliminar(self):
        miConexion = sqlite3.connect("VideClub")
        miCursor = miConexion.cursor()
        miCursor.execute(
            "DELETE FROM Datos_Pelicula WHERE ID=" +
            Pelicula.keyID.get())
        miConexion.commit()
        messagebox.showinfo("DB", "Registro borrado con exito")
