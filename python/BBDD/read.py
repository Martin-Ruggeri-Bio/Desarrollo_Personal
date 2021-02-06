import sqlite3

miConexion = sqlite3.connect("Gestion_Productos_Incremental")

miCursor = miConexion.cursor()

miCursor.execute("SELECT * FROM Productos WHERE Seccion='Ceramica'")

productos = miCursor.fetchall()
print(productos)

miConexion.commit()

miConexion.close()
