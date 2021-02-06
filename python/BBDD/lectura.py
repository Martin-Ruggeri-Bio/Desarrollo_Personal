import sqlite3

miConexion = sqlite3.connect("PrimeraBase")

miCursor = miConexion.cursor()

miCursor.execute("SELECT * FROM Productos")

variosProductos = miCursor.fetchall()

for producto in variosProductos:
    print(producto)
    print("Nombre Articulo:", producto[0], "\nSeccion:", producto[2])

miConexion.commit()

miConexion.close()
