from tkinter import Tk, Menu, messagebox, filedialog


def infoAdicional():
    messagebox.showinfo("Procesador de Martin",
                        "Procesador de textos version 2020")


def avisoLicencia():
    messagebox.showwarning("Licencia de Martin", "Producto bajo licencia GNU")


def salirAplicacion():
    valor = messagebox.askquestion("salir", "¿Desea Salir de la aplicacion?")
    if valor == "yes":
        root.destroy()


def cerrarArchivo():
    valor = messagebox.askokcancel("salir", "¿Desea Salir de la aplicacion?")
    if valor:
        root.destroy()


def guardarArchivo():
    valor = messagebox.askretrycancel(
        "Reintentar", "No es posible guardar un documento que no existe")
    if not valor:
        root.destroy()


def abreFichero():
    fichero = filedialog.askopenfilename(
        title="Abrir",
        initialdir="/home/martin",
        filetypes=(("Ficheros de Python", "*.py"),
                   ("Ficheros de Texto", "*.txt")))
    print(fichero)


root = Tk()
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir", command=abreFichero)
archivoMenu.add_command(label="Guardar", command=guardarArchivo)
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarArchivo)
archivoMenu.add_command(label="Salir", command=salirAplicacion)


edicionMenu = Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")
edicionMenu.add_command(label="Borrar")

herramientasMenu = Menu(barraMenu)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=avisoLicencia)
ayudaMenu.add_command(label="Acerca de ...", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=edicionMenu)
barraMenu.add_cascade(label="Herramientas", menu=herramientasMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

root.mainloop()
