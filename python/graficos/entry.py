from tkinter import Tk, Frame, Entry, Label, Text, Scrollbar, Button, StringVar


# creamos el obj raiz de la clase Tk
raiz = Tk()

# creamos un titulo
raiz.title("ventana de pruebas")
raiz.config(bg="blue")

# creo mi frame
miFrame = Frame()
miFrame.config(bg="red")

# ingreso cuadro de texto
minombre = StringVar()
miapellido = StringVar()
midireccion = StringVar()

cuadroTexto = Entry(miFrame, textvariable=minombre)
cuadroTexto.grid(row=0, column=1, padx=10, pady=10)
cuadroTexto.config(fg="red", justify="right")

cuadroTexto2 = Entry(miFrame, textvariable=miapellido)
cuadroTexto2.grid(row=1, column=1, padx=10, pady=10)

cuadroTexto3 = Entry(miFrame, textvariable=midireccion)
cuadroTexto3.grid(row=2, column=1, padx=10, pady=10)

# ingreso un cuadro texto grande
textoComentario = Text(miFrame, width=20, height=10)
textoComentario.grid(row=3, column=1, padx=10, pady=10)

scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=3, column=2, sticky="nsew")

# infreso nombre
nombre = Label(miFrame, text="nombre:")
nombre.grid(row=0, column=0, sticky="w", padx=10, pady=10)

nombre2 = Label(miFrame, text="apellido:")
nombre2.grid(row=1, column=0, sticky="w", padx=10, pady=10)

nombre3 = Label(miFrame, text="direccion:")
nombre3.grid(row=2, column=0, sticky="w", padx=10, pady=10)

nombre4 = Label(miFrame, text="comentario:")
nombre4.grid(row=3, column=0, sticky="w", padx=10, pady=10)

# creo boton


def codigoBotonCompletar():
    minombre.set("Martin")
    miapellido.set("Ruggeri")
    midireccion.set("Yapeyu 637")


botonEnvio = Button(miFrame, text="Completar", command=codigoBotonCompletar)
botonEnvio.grid(row=4, column=1, padx=10, pady=10)

# empaqueto el frame dentro de la raiz
miFrame.pack()
# elijo el redimencionamiento del frame
miFrame.pack(side="left", anchor="n")

# bucle infinito que mantiene la ventana abierta
raiz.mainloop()
