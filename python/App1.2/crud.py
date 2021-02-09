from tkinter import messagebox, StringVar
import sqlite3


class DB_service():
    def __init__(self):
        self.miID = StringVar()
        self.miNombre = StringVar()
        self.miPass = StringVar()
        self.miApellido = StringVar()
        self.miDireccion = StringVar()

    def borrarCampos(self):
        self.miID.set("")
        self.miNombre.set("")
        self.miPass.set("")
        self.miApellido.set("")
        self.miDireccion.set("")

    def crear(self):
        miConexion = sqlite3.connect("Usuarios")
        miCursor = miConexion.cursor()
        datos = self.miNombre.get(), self.miPass.get(), self.miApellido.get(),\
            self.miDireccion.get()
        miCursor.execute(
            "INSERT INTO Datos_Usuarios VALUES(NULL, ?, ?, ?, ?)",
            (datos)
        )
        miConexion.commit()
        messagebox.showinfo("BBDD", "Registro insertado con exito")

    def leer(self):
        miConexion = sqlite3.connect("Usuarios")
        miCursor = miConexion.cursor()
        miCursor.execute(
            "SELECT * FROM Datos_Usuarios WHERE ID=" + self.miID.get())
        # nos devuelve un array con los registros
        elUsuario = miCursor.fetchall()
        for usuario in elUsuario:
            self.miID.set(usuario[0])
            self.miNombre.set(usuario[1])
            self.miPass.set(usuario[2])
            self.miApellido.set(usuario[3])
            self.miDireccion.set(usuario[4])
        miConexion.commit()

    def actualizar(self):
        miConexion = sqlite3.connect("Usuarios")
        miCursor = miConexion.cursor()
        datos = self.miNombre.get(), self.miPass.get(), self.miApellido.get(),\
            self.miDireccion.get()
        miCursor.execute(
            "UPDATE Datos_Usuarios SET\
                Nombre_Usuario=?, Password=?, Apellido=?,\
                Direccion=?" +
            "WHERE ID=" + self.miID.get(), (datos)
        )
        miConexion.commit()
        messagebox.showinfo("BBDD", "Registro actualizado con exito")

    def eliminar(self):
        miConexion = sqlite3.connect("Usuarios")
        miCursor = miConexion.cursor()
        miCursor.execute(
            "DELETE FROM Datos_Usuarios WHERE ID=" + self.miID.get())
        miConexion.commit()
        messagebox.showinfo("BBDD", "Registro borrado con exito")
