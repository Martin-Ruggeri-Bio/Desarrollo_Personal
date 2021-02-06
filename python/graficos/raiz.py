from tkinter import Tk, Frame, Label, PhotoImage


# creamos el obj raiz de la clase Tk
raiz = Tk()
# creamos un titulo
raiz.title("ventana de pruebas")
# damos dimensiones fijas
raiz.resizable(1, 1)
# agregar icono
# raiz.iconbitmap("icono.ico")
# resolucion
raiz.geometry("750x500")
# cambiar el color de fondo
raiz.config(bg="blue")
# creo mi frame
miFrame = Frame()
miFrame.config(bg="red")
miFrame.config(width="650", height="400")
# cambio el ancho del borde
miFrame.config(bd=35)
# cambio el estilo del borde (groove, sunken)
miFrame.config(relief="groove")
# cambio el estilo del cursor (hand2, pirate)
miFrame.config(cursor="hand2")
# empaqueto el frame dentro de la raiz
# elijo posicion (left, right, top, bottom)(n, s, e, w)

# elijo el redimencionamiento del frame
miFrame.pack(side="left", anchor="n")
# elijo el redimencionamiento del frame (x, y, both, none)
# miFrame.pack(fill="x")

# coloco imagen (png o gif)
miImagen = PhotoImage(
      file="/home/martin/Desarrollo_Personal/python/graficos/agujero_negro.gif"
      )
Label(miFrame, image=miImagen).pack()
# ingreso texto, color, tamaño, tipo, etc
Label(miFrame, text="hola alumnos de python", fg="blue",
      font=("Comic Sans MS", 20)).pack()
# otra forma de empaquetar sin modificar el frame
# miLabel.place(x=100, y=100)
# bucle infinito que mantiene la ventana abierta
raiz.mainloop()
