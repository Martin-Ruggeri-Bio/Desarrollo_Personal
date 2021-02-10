from tkinter import messagebox, StringVar, Frame
from labels_y_cuadrosTextos import Labels, CuadrosTextos
import sqlite3


class DB_service():
    def __init__(self, root):
        self.root = root
        self.miFrame = Frame(self.root)
        self.miConexion = sqlite3.connect("Usuarios")
        self.miCursor = self.miConexion.cursor()
        self.miID = StringVar()
        self.miNombre = StringVar()
        self.miPass = StringVar()
        self.miApellido = StringVar()
        self.miDireccion = StringVar()
        self.cuadroTextos = CuadrosTextos(
            self.miFrame, self.miID, self.miNombre, self.miPass,
            self.miApellido, self.miDireccion)
        self.cuadroTextos.grid()
        self.cuadroTextos.pack()
        self.labels = Labels(self.miFrame)
        self.labels.grid()
        self.labels.pack()

    def conexionDB(self):
        try:
            self.miCursor.execute(
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

    def salirAplicacion(self):
        valor = messagebox.askquestion("Salir", "¿Deseas salir?")
        if valor == "yes":
            self.root.destroy()

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
        try:
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
        except sqlite3.OperationalError:
            messagebox.showwarning("¡Atencion!", "No ingreso un ID")

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
