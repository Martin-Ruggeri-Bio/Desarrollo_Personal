import sqlite3

miConexion = sqlite3.connect("Gestion_Productos_Incremental")

miCursor = miConexion.cursor()

miCursor.execute(
    "UPDATE Productos SET Precio=35 WHERE Nombre_Articulo='Jarron'"
    )

miConexion.commit()

miConexion.close()
