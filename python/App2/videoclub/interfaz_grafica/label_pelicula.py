from tkinter import Label


class LabelPelicula():
    def __init__(self, framePelicula):
        self.idLabel = Label(
            framePelicula, text="ID:")
        self.tituloLabel = Label(
            framePelicula, text="Titulo:")
        self.generoLabel = Label(
            framePelicula, text="Genero:")
        self.duracionLabel = Label(
            framePelicula, text="Duracion:")
        self.actoresLabel = Label(
            framePelicula, text="Actores:")

    def peliculaGrid(self):
        self.idLabel.grid(
            row=0, column=0, sticky="e", padx=10, pady=10)
        self.tituloLabel.grid(
            row=1, column=0, sticky="e", padx=10, pady=10)
        self.generoLabel.grid(
            row=3, column=0, sticky="e", padx=10, pady=10)
        self.duracionLabel.grid(
            row=4, column=0, sticky="e", padx=10, pady=10)
        self.actoresLabel.grid(
            row=4, column=0, sticky="e", padx=10, pady=10)
