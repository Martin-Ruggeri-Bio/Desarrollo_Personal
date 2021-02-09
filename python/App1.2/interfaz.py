from tkinter import Menu, Frame, Entry, Label
from conexion_DB import conexionBBDD, salirAplicacion
from crud import DB_service


class Interfaz_Menu():
    def __init__(self, root):
        self.root = root
        self.barraMenu = Menu(root)
        self.root.config(menu=self.barraMenu, width=300, height=300)
        self.bbddMenu = Menu(self.barraMenu, tearoff=0)
        self.borrarMenu = Menu(self.barraMenu, tearoff=0)
        self.crudMenu = Menu(self.barraMenu, tearoff=0)
        self.ayudaMenu = Menu(self.barraMenu, tearoff=0)
        self.ayudaMenu = Menu(self.barraMenu, tearoff=0)

    def opciones_de_menu(self):
        self.bbddMenu.add_command(label="Conectar", command=conexionBBDD)
        self.bbddMenu.add_command(label="salir", command=salirAplicacion(self.root))

        self.borrarMenu.add_command(
            label="Borrar campos", command=DB_service.borrarCampos)

        self.crudMenu.add_command(label="Crear", command=DB_service.crear)
        self.crudMenu.add_command(label="Leer", command=DB_service.leer)
        self.crudMenu.add_command(
            label="Actualizar", command=DB_service.actualizar)
        self.crudMenu.add_command(label="Borrar", command=DB_service.eliminar)

        self.ayudaMenu.add_command(label="Licencia")
        self.ayudaMenu.add_command(label="Acerca de ...")

        self.barraMenu.add_cascade(label="BBDD", menu=self.bbddMenu)
        self.barraMenu.add_cascade(label="Borrar", menu=self.borrarMenu)
        self.barraMenu.add_cascade(label="CRUD", menu=self.crudMenu)
        self.barraMenu.add_cascade(label="Ayuda", menu=self.ayudaMenu)


class Interfaz_CuadrosTextos(DB_service):
    def __init__(self, root):
        DB_service.__init__(self)
        self.miFrame = Frame(root)
        self.cuadroID = Entry(self.miFrame, textvariable=self.miID)
        self.cuadroNombre = Entry(self.miFrame, textvariable=self.miNombre)
        self.cuadroPass = Entry(self.miFrame, textvariable=self.miPass)
        self.cuadroApellido = Entry(self.miFrame, textvariable=self.miApellido)
        self.cuadroDireccion = Entry(
            self.miFrame, textvariable=self.miDireccion)

    def grid(self):
        self.cuadroID.grid(row=0, column=1, padx=10, pady=10)
        self.cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
        self.cuadroPass.grid(row=2, column=1, padx=10, pady=10)
        self.cuadroPass.config(show="?")
        self.cuadroApellido.grid(row=3, column=1, padx=10, pady=10)
        self.cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

    def pack(self):
        self.miFrame.pack()


class Interfaz_Label():
    def __init__(self, root):
        self.miFrame = Frame(root)
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
