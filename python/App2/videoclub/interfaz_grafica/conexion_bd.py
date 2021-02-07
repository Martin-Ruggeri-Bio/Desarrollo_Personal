from tkinter import messagebox
from Barra_Menu import TablaService
import sqlite3


class ConexionDB():
    def conectar_tablas(self, root, eleccion):
        miConexion = sqlite3.connect("VideClub")
        miCursor = miConexion.cursor()
        try:
            miCursor.execute(
                '''CREATE TABLE Datos_Actor(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nombre_Actor VARCHAR(50),
                    Apellido VARCHAR(50),
                    Edad INTERGER,
                )'''
                '''CREATE TABLE Datos_Pelicula(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Titulo VARCHAR(50),
                    Duracion INTERGER,
                    Genero VARCHAR(50)
                    Actores VARCHAR(100),
                )
            ''')
            messagebox.showinfo("DB", "DB creada con exito")
        except sqlite3.OperationalError:
            messagebox.showwarning("¡Atencion!", "La DB ya existe")
        TablaService(root, eleccion)

    def cerrarConexionDB(self, frame):
        valor = messagebox.askquestion(
            "Salir", "¿Deseas salir de la aplicacion?")
        if valor == "yes":
            frame.destroy()
