from tkinter import messagebox
from frame_pelicula import Pelicula
import sqlite3


class PeliculaServiceDB():
    def conexionDB(self):
        miConexion = sqlite3.connect("VideClub")
        miCursor = miConexion.cursor()
        try:
            miCursor.execute(
                '''CREATE TABLE Datos_Pelicula(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Titulo VARCHAR(50),
                    Duracion INTERGER,
                    Genero VARCHAR(50)
                    Actores VARCHAR(100),
                )
            ''')
            messagebox.showinfo(
                "DB", "Tabla Datos_Pelicula creada con exito")
        except sqlite3.OperationalError:
            messagebox.showwarning("¡Atencion!", "La DB ya existe")

    def cerrarConexionDB(self, framePelicula):
        valor = messagebox.askquestion(
            "Salir", "¿Deseas salir de la aplicacion?")
        if valor == "yes":
            framePelicula.destroy()

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
