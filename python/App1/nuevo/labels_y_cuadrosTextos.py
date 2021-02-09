from tkinter import Entry, Label


class CuadrosTextos():
    def __init__(self, miFrame, miID, miNombre,
                 miPass, miApellido, miDireccion):
        self.miFrame = miFrame
        self.cuadroID = Entry(self.miFrame, textvariable=miID)
        self.cuadroNombre = Entry(self.miFrame, textvariable=miNombre)
        self.cuadroPass = Entry(self.miFrame, textvariable=miPass)
        self.cuadroApellido = Entry(self.miFrame, textvariable=miApellido)
        self.cuadroDireccion = Entry(self.miFrame, textvariable=miDireccion)

    def grid(self):
        self.cuadroID.grid(row=0, column=1, padx=10, pady=10)
        self.cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
        self.cuadroPass.grid(row=2, column=1, padx=10, pady=10)
        self.cuadroPass.config(show="?")
        self.cuadroApellido.grid(row=3, column=1, padx=10, pady=10)
        self.cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

    def pack(self):
        self.miFrame.pack()


class Labels():
    def __init__(self, miFrame):
        self.miFrame = miFrame
        self.idLabel = Label(self.miFrame, text="ID:")
        self.nombreLabel = Label(self.miFrame, text="Nombre:")
        self.passwordLabel = Label(self.miFrame, text="Password:")
        self.apellidoLabel = Label(self.miFrame, text="Apellido:")
        self.direccionLabel = Label(self.miFrame, text="Direccion:")

    def grid(self):
        self.idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)
        self.nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.passwordLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)
        self.apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)
        self.direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

    def pack(self):
        self.miFrame.pack()
