from tkinter import Entry, Label


class CuadrosTextos():
    def __init__(self, miFrame, miID, miTitulo, miGenero,
                 miDuracion, miActor1, miActor2):
        self.miFrame = miFrame
        self.cuadroID = Entry(self.miFrame, textvariable=miID)
        self.cuadroTitulo = Entry(self.miFrame, textvariable=miTitulo)
        self.cuadroGenero = Entry(self.miFrame, textvariable=miGenero)
        self.cuadroDuracion = Entry(self.miFrame, textvariable=miDuracion)
        self.cuadroActor1 = Entry(self.miFrame, textvariable=miActor1)
        self.cuadroActor2 = Entry(self.miFrame, textvariable=miActor2)

    def grid(self):
        self.cuadroID.grid(row=0, column=2, padx=10, pady=10)
        self.cuadroTitulo.grid(row=1, column=2, padx=10, pady=10)
        self.cuadroGenero.grid(row=2, column=2, padx=10, pady=10)
        self.cuadroDuracion.grid(row=3, column=2, padx=10, pady=10)
        self.cuadroActor1.grid(row=4, column=2, padx=10, pady=10)
        self.cuadroActor2.grid(row=5, column=2, padx=10, pady=10)

    def pack(self):
        self.miFrame.pack()


class Labels():
    def __init__(self, miFrame):
        self.miFrame = miFrame
        self.idLabel = Label(self.miFrame, text="ID:")
        self.tituloLabel = Label(self.miFrame, text="Titulo:")
        self.generoLabel = Label(self.miFrame, text="Genero:")
        self.duracionLabel = Label(self.miFrame, text="Duracion:")
        self.actorLabel1 = Label(self.miFrame, text="ID_Actor1:")
        self.actorLabel2 = Label(self.miFrame, text="ID_Actor2:")

    def grid(self):
        self.idLabel.grid(row=0, column=1, sticky="e", padx=10, pady=10)
        self.tituloLabel.grid(row=1, column=1, sticky="e", padx=10, pady=10)
        self.generoLabel.grid(row=2, column=1, sticky="e", padx=10, pady=10)
        self.duracionLabel.grid(row=3, column=1, sticky="e", padx=10, pady=10)
        self.actorLabel1.grid(row=4, column=1, sticky="e", padx=10, pady=10)
        self.actorLabel2.grid(row=5, column=1, sticky="e", padx=10, pady=10)

    def pack(self):
        self.miFrame.pack()
