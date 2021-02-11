from tkinter import messagebox, StringVar, Frame
from frame_pelicula import Labels, CuadrosTextos
import sqlite3


class DB_servicePelicula():
    def __init__(self, root):
        self.root = root
        self.miFrame = Frame(self.root)
        self.miConexion = sqlite3.connect("VideoClub")
        self.miID = StringVar()
        self.miTitulo = StringVar()
        self.miGenero = StringVar()
        self.miDuracion = StringVar()
        self.miActor = StringVar()
        self.cuadroTextos = CuadrosTextos(
            self.miFrame, self.miID, self.miTitulo, self.miGenero,
            self.miDuracion, self.miActor)
        self.cuadroTextos.grid()
        self.cuadroTextos.pack()
        self.labels = Labels(self.miFrame)
        self.labels.grid()
        self.labels.pack()

    def conexionDB(self):
        self.miCursor = self.miConexion.cursor()
        try:
            self.miCursor.execute(
                '''CREATE TABLE Datos_Pelicula(
                    ID_Pelicula INTEGER PRIMARY KEY AUTOINCREMENT,
                    Titulo VARCHAR(50),
                    Duracion INTERGER,
                    Genero VARCHAR(50),
                    ID_Actor INTERGER,
                    FOREIGN KEY (ID_Actor) REFERENCES Datos_Actores(ID_Actor)
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
        self.miTitulo.set("")
        self.miGenero.set("")
        self.miDuracion.set("")
        self.miActor.set("")

    def crear(self):
        datos = self.miTitulo.get(), self.miGenero.get(),\
            self.miDuracion.get(), self.miActor.get()
        self.miCursor.execute(
            "INSERT INTO Datos_Pelicula VALUES(NULL, ?, ?, ?, ?)",
            (datos)
        )
        self.miConexion.commit()
        messagebox.showinfo("BBDD", "Registro insertado con exito")

    def leer(self):
        try:
            self.miCursor.execute(
                "SELECT * FROM Datos_Pelicula WHERE ID=" + self.miID.get())
            # nos devuelve un array con los registros
            laPelicula = self.miCursor.fetchall()
            for registro in laPelicula:
                self.miID.set(registro[0])
                self.miTitulo.set(registro[1])
                self.miGenero.set(registro[2])
                self.miDuracion.set(registro[3])
                self.miActor.set(registro[4])
            self.miConexion.commit()
        except sqlite3.OperationalError:
            messagebox.showwarning("¡Atencion!", "No ingreso un ID")

    def actualizar(self):
        datos = self.miTitulo.get(), self.miGenero.get(),\
            self.miDuracion.get(), self.miActor.get()
        self.miCursor.execute(
            "UPDATE Datos_Pelicula SET\
                Titulo=?, Genero=?, Duracion=?,\
                Actor=?" +
            "WHERE ID=" + self.miID.get(), (datos)
        )
        self.miConexion.commit()
        messagebox.showinfo("BBDD", "Registro actualizado con exito")

    def eliminar(self):
        self.miCursor.execute(
            "DELETE FROM Datos_Pelicula WHERE ID=" + self.miID.get())
        self.miConexion.commit()
        messagebox.showinfo("BBDD", "Registro borrado con exito")

    def listar(self):
        pass
