from tkinter import messagebox, StringVar
from labels_y_cuadrosTextos import Labels, CuadrosTextos
import sqlite3


class DB_service():
    def __init__(self, miFrame):
        self.miConexion = sqlite3.connect("Usuarios")
        self.miCursor = self.miConexion.cursor()
        self.miID = StringVar()
        self.miNombre = StringVar()
        self.miPass = StringVar()
        self.miApellido = StringVar()
        self.miDireccion = StringVar()
        self.cuadroTextos = CuadrosTextos(
            miFrame, self.miID, self.miNombre, self.miPass,
            self.miApellido, self.miDireccion)
        self.cuadroTextos.grid()
        self.cuadroTextos.pack()
        self.labels = Labels(miFrame)
        self.labels.grid()
        self.labels.pack()

    def borrarCampos(self):
        self.miID.set("")
        self.miNombre.set("")
        self.miPass.set("")
        self.miApellido.set("")
        self.miDireccion.set("")

    def crear(self):
        datos = self.miNombre.get(), self.miPass.get(), self.miApellido.get(),\
            self.miDireccion.get()
        self.miCursor.execute(
            "INSERT INTO Datos_Usuarios VALUES(NULL, ?, ?, ?, ?)",
            (datos)
        )
        self.miConexion.commit()
        messagebox.showinfo("BBDD", "Registro insertado con exito")

    def leer(self):
        self.miCursor.execute(
            "SELECT * FROM Datos_Usuarios WHERE ID=" + self.miID.get())
        # nos devuelve un array con los registros
        elUsuario = self.miCursor.fetchall()
        for usuario in elUsuario:
            self.miID.set(usuario[0])
            self.miNombre.set(usuario[1])
            self.miPass.set(usuario[2])
            self.miApellido.set(usuario[3])
            self.miDireccion.set(usuario[4])
        self.miConexion.commit()

    def actualizar(self):
        datos = self.miNombre.get(), self.miPass.get(), self.miApellido.get(),\
            self.miDireccion.get()
        self.miCursor.execute(
            "UPDATE Datos_Usuarios SET\
                Nombre_Usuario=?, Password=?, Apellido=?,\
                Direccion=?" +
            "WHERE ID=" + self.miID.get(), (datos)
        )
        self.miConexion.commit()
        messagebox.showinfo("BBDD", "Registro actualizado con exito")

    def eliminar(self):
        self.miCursor.execute(
            "DELETE FROM Datos_Usuarios WHERE ID=" + self.miID.get())
        self.miConexion.commit()
        messagebox.showinfo("BBDD", "Registro borrado con exito")
