from tkinter import messagebox, StringVar, Frame
from frame_actor import Labels, CuadrosTextos
import sqlite3


class DB_serviceActor():
    def __init__(self, root):
        self.root = root
        self.miFrame = Frame(self.root)
        self.miConexion = sqlite3.connect("VideoClub")
        self.miID = StringVar()
        self.miNombre = StringVar()
        self.miApellido = StringVar()
        self.miEdad = StringVar()
        self.cuadroTextos = CuadrosTextos(
            self.miFrame, self.miID, self.miNombre,
            self.miApellido, self.miEdad)
        self.cuadroTextos.grid()
        self.cuadroTextos.pack()
        self.labels = Labels(self.miFrame)
        self.labels.grid()
        self.labels.pack()

    def conexionDB(self):
        self.miCursor = self.miConexion.cursor()
        try:
            self.miCursor.execute(
                '''CREATE TABLE Datos_Actores(
                    ID_Actor INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nombre VARCHAR(50),
                    Apellido VARCHAR(50),
                    Edad INTERGER
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
        self.miApellido.set("")
        self.miEdad.set("")

    def crear(self):
        datos = self.miNombre.get(), self.miApellido.get(), self.miEdad.get()
        self.miCursor.execute(
            "INSERT INTO Datos_Actores VALUES(NULL, ?, ?, ?)", (datos))
        self.miConexion.commit()
        messagebox.showinfo("BBDD", "Registro insertado con exito")

    def leer(self):
        try:
            self.miCursor.execute(
                "SELECT * FROM Datos_Actores WHERE ID_Actor=" +
                self.miID.get())
            # nos devuelve un array con los registros
            elActor = self.miCursor.fetchall()
            for registro in elActor:
                self.miID.set(registro[0])
                self.miNombre.set(registro[1])
                self.miApellido.set(registro[2])
                self.miEdad.set(registro[3])
            self.miConexion.commit()
        except sqlite3.OperationalError:
            messagebox.showwarning("¡Atencion!", "No ingreso un ID")

    def actualizar(self):
        datos = self.miNombre.get(), self.miApellido.get(), self.miEdad.get()
        self.miCursor.execute(
            "UPDATE Datos_Actores SET Nombre=?, Apellido=?, Edad=?" +
            "WHERE ID_Actor=" + self.miID.get(), (datos)
        )
        self.miConexion.commit()
        messagebox.showinfo("BBDD", "Registro actualizado con exito")

    def eliminar(self):
        self.miCursor.execute(
            "DELETE FROM Datos_Actores WHERE ID_Actor=" + self.miID.get())
        self.miConexion.commit()
        messagebox.showinfo("BBDD", "Registro borrado con exito")

    def listar(self):
        pass
