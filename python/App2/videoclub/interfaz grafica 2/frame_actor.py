from tkinter import Entry, Label


class CuadrosTextos():
    def __init__(self, miFrame, miID, miNombre, miApellido, miEdad):
        self.miFrame = miFrame
        self.cuadroID = Entry(self.miFrame, textvariable=miID)
        self.cuadroNombre = Entry(self.miFrame, textvariable=miNombre)
        self.cuadroApellido = Entry(self.miFrame, textvariable=miApellido)
        self.cuadroedad = Entry(self.miFrame, textvariable=miEdad)

    def grid(self):
        self.cuadroID.grid(row=0, column=2, padx=10, pady=10)
        self.cuadroNombre.grid(row=1, column=2, padx=10, pady=10)
        self.cuadroApellido.grid(row=2, column=2, padx=10, pady=10)
        self.cuadroedad.grid(row=3, column=2, padx=10, pady=10)

    def pack(self):
        self.miFrame.pack()


class Labels():
    def __init__(self, miFrame):
        self.miFrame = miFrame
        self.idLabel = Label(self.miFrame, text="ID:")
        self.nombreLabel = Label(self.miFrame, text="Nombre:")
        self.apellidoLabel = Label(self.miFrame, text="Apellido:")
        self.edadLabel = Label(self.miFrame, text="Edad:")

    def grid(self):
        self.idLabel.grid(row=0, column=1, sticky="e", padx=10, pady=10)
        self.nombreLabel.grid(row=1, column=1, sticky="e", padx=10, pady=10)
        self.apellidoLabel.grid(row=2, column=1, sticky="e", padx=10, pady=10)
        self.edadLabel.grid(row=3, column=1, sticky="e", padx=10, pady=10)

    def pack(self):
        self.miFrame.pack()
