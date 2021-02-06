from tkinter import Entry, StringVar
from label_actor import LabelActor


class Actor():
    def __init__(self, frameActor):
        self.frameActor = frameActor
        self.keyID = StringVar()
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.edad = StringVar()

    def cuadros(self):
        cuadroID = Entry(self.frameActor, textvariable=self.keyID)
        cuadroID.grid(row=0, column=1, padx=10, pady=10)

        cuadroNombre = Entry(self.frameActor, textvariable=self.nombre)
        cuadroNombre.grid(row=1, column=1, padx=10, pady=10)

        cuadroApellido = Entry(self.frameActor, textvariable=self.apellido)
        cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

        cuadroDireccion = Entry(self.frameActor, textvariable=self.edad)
        cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

    def label(self):
        actorLabel = LabelActor(self.frameActor)
        actorLabel.actorGrid()
