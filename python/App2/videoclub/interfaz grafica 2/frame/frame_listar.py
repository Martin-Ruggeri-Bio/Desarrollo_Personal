from tkinter import Label, Text, Scrollbar


class CuadrosTextos():
    def __init__(self, miFrame):
        self.miFrame = miFrame
        self.textoComentario = Text(
            miFrame, width=20, height=10)
        self.scrollVert = Scrollbar(
            miFrame, command=self.textoComentario.yview)

    def grid(self):
        self.textoComentario.grid(row=5, column=1, padx=10, pady=10)
        self.scrollVert.grid(row=5, column=2, sticky="nsew")
        self.textoComentario.config(yscrollcommand=self.scrollVert.set)

    def pack(self):
        self.miFrame.pack()


class Labels():
    def __init__(self, miFrame):
        self.miFrame = miFrame
        self.comentariosLabel = Label(miFrame, text="Comentarios:")

    def grid(self):
        self.comentariosLabel.grid(
            row=5, column=0, sticky="e", padx=10, pady=10)

    def pack(self):
        self.miFrame.pack()
