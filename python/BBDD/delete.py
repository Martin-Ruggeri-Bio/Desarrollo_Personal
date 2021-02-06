import sqlite3

miConexion = sqlite3.connect("Gestion_Productos_Incremental")

miCursor = miConexion.cursor()

miCursor.execute(
    "DELETE FROM Productos WHERE ID=2"
    )

miConexion.commit()

miConexion.close()
