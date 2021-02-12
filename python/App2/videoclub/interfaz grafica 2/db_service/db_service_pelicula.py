from tkinter import messagebox, StringVar, Frame
from frame.frame_pelicula import Labels, CuadrosTextos
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
        self.miActor1 = StringVar()
        self.miActor2 = StringVar()
        self.cuadroTextos = CuadrosTextos(
            self.miFrame, self.miID, self.miTitulo, self.miGenero,
            self.miDuracion, self.miActor1, self.miActor2)
        self.cuadroTextos.grid()
        self.cuadroTextos.pack()
        self.labels = Labels(self.miFrame)
        self.labels.grid()
        self.labels.pack()

    def crearDB(self):
        self.miCursor = self.miConexion.cursor()
        try:
            self.miCursor.execute(
                '''CREATE TABLE Datos_Pelicula(
                    ID_Pelicula INTEGER PRIMARY KEY AUTOINCREMENT,
                    Titulo VARCHAR(50),
                    Duracion INTERGER,
                    Genero VARCHAR(50),
                    ID_Actor1 INTERGER,
                    ID_Actor2 INTERGER,
                    FOREIGN KEY (ID_Actor1) REFERENCES \
                        Datos_Actores(ID_Actor1),
                    FOREIGN KEY (ID_Actor2) REFERENCES \
                        Datos_Actores(ID_Actor1)
                )
            ''')
            messagebox.showinfo(
                "BBDD", "Se creo una tabla nueva llamada Datos_Pelicula")
        except sqlite3.OperationalError:
            messagebox.showinfo(
                "BBDD", "Conexion con la tabla Datos_Pelicula realizada")

    def salirAplicacion(self):
        valor = messagebox.askquestion("Salir", "¿Deseas salir?")
        if valor == "yes":
            self.root.destroy()

    def borrarCampos(self):
        self.miID.set("")
        self.miTitulo.set("")
        self.miGenero.set("")
        self.miDuracion.set("")
        self.miActor1.set("")
        self.miActor2.set("")

    def crear(self):
        datos = self.miTitulo.get(), self.miGenero.get(),\
            self.miDuracion.get(), self.miActor1.get(), self.miActor2.get()
        self.miCursor.execute(
            "INSERT INTO Datos_Pelicula VALUES(NULL, ?, ?, ?, ?, ?)",
            (datos)
        )
        self.miConexion.commit()
        messagebox.showinfo("BBDD", "Registro insertado con exito")

    def leer(self):
        try:
            self.miCursor.execute(
                "SELECT * FROM Datos_Pelicula WHERE ID_Pelicula=" +
                self.miID.get())
            # nos devuelve un array con los registros
            laPelicula = self.miCursor.fetchall()
            for registro in laPelicula:
                self.miID.set(registro[0])
                self.miTitulo.set(registro[1])
                self.miGenero.set(registro[2])
                self.miDuracion.set(registro[3])
                self.miActor1.set(registro[4])
                self.miActor2.set(registro[5])
            self.miConexion.commit()
        except sqlite3.OperationalError:
            messagebox.showwarning("¡Atencion!", "No ingreso un ID")

    def actualizar(self):
        datos = self.miTitulo.get(), self.miGenero.get(),\
            self.miDuracion.get(), self.miActor1.get(), self.miActor2.get()
        self.miCursor.execute(
            "UPDATE Datos_Pelicula SET\
                Titulo=?, Genero=?, Duracion=?,\
                ID_Actor1=?, ID_Actor2=?" +
            "WHERE ID_Pelicula=" + self.miID.get(), (datos)
        )
        self.miConexion.commit()
        messagebox.showinfo("BBDD", "Registro actualizado con exito")

    def eliminar(self):
        self.miCursor.execute(
            "DELETE FROM Datos_Pelicula WHERE ID_Pelicula=" + self.miID.get())
        self.miConexion.commit()
        messagebox.showinfo("BBDD", "Registro borrado con exito")
