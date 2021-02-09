from tkinter import messagebox
from tabla_service import TablaService
import sqlite3


class ConexionDB():
    def __init__(self, root):
        self.root = root

    def conectar_tablas(self, frame_elegido):
        self.miConexion = sqlite3.connect("VideClub")
        self.miCursor = self.miConexion.cursor()
        try:
            self.miCursor.execute(
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
        self.tabla = TablaService(self.root)
        self.tabla.frame(frame_elegido)

    def cerrarConexionDB(self, frame_o_root):
        self.valor = messagebox.askquestion(
            "Salir", "¿Deseas salir de la aplicacion?")
        if self.valor == "yes":
            frame_o_root.destroy()
