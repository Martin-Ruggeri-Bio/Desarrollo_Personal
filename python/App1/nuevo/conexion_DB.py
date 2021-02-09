from tkinter import messagebox
import sqlite3


def conexionBBDD():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    try:
        miCursor.execute(
            '''CREATE TABLE Datos_Usuarios(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre_Usuario VARCHAR(50),
                Password VARCHAR(10),
                Apellido VARCHAR(50),
                Direccion VARCHAR(50)
            )
        ''')
        messagebox.showinfo("BBDD", "BBDD creada con exito")
    except sqlite3.OperationalError:
        messagebox.showwarning("¡Atencion!", "La BBDD ya existe")


def salirAplicacion(root):
    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    if valor == "yes":
        root.destroy()
