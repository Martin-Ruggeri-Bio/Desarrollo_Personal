import sqlite3

miConexion = sqlite3.connect("PrimeraBase")

miCursor = miConexion.cursor()

miCursor.execute("INSERT INTO Productos VALUES('Balon', 15, 'Deportes')")
miConexion.commit()

miConexion.close()
