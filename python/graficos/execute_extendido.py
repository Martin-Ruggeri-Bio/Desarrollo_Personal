import sqlite3
from tkinter import messagebox, END, StringVar, Entry, Text, Frame, Scrollbar,\
                    Tk


def crear():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute(
        "INSERT INTO Datos_Usuarios VALUES(\
            NULL, '" + miNombre.get() + "',\
            '" + miPass.get() + "',\
            '" + miApellido.get() + "',\
            '" + miDireccion.get() + "',\
            '" + textoComentario.get("1.0", END) + "'\
        )"
    )
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro insertado con exito")


def actualizar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute(
        "UPDATE Datos_Usuarios SET\
            Nombre_Usuario='" + miNombre.get() + "',\
            Password='" + miPass.get() + "',\
            Apellido='" + miApellido.get() + "',\
            Direccion='" + miDireccion.get() + "',\
            Comentarios='" + textoComentario.get("1.0", END) + "'\
            WHERE ID=" + miID.get()
    )
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado con exito")


root = Tk()
miFrame = Frame(root)
miFrame.pack()

miID = StringVar()
miNombre = StringVar()
miPass = StringVar()
miApellido = StringVar()
miDireccion = StringVar()

cuadroID = Entry(miFrame, textvariable=miID)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)

cuadroPass = Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="?")

cuadroApellido = Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion = Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario = Text(miFrame, width=20, height=10)
textoComentario.grid(row=5, column=1, padx=10, pady=10)

scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)
