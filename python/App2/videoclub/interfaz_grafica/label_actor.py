from tkinter import Label


class LabelActor():
    def __init__(self, frameActor):
        self.idLabel = Label(
            frameActor, text="ID:")
        self.nombreLabel = Label(
            frameActor, text="Nombre:")
        self.apellidoLabel = Label(
            frameActor, text="Apellido:")
        self.direccionLabel = Label(
            frameActor, text="Edad:")

    def actorGrid(self):
        self.idLabel.grid(
            row=0, column=0, sticky="e", padx=10, pady=10)
        self.nombreLabel.grid(
            row=1, column=0, sticky="e", padx=10, pady=10)
        self.apellidoLabel.grid(
            row=2, column=0, sticky="e", padx=10, pady=10)
        self.direccionLabel.grid(
            row=3, column=0, sticky="e", padx=10, pady=10)
