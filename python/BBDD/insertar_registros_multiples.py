import sqlite3

miConexion = sqlite3.connect("PrimeraBase")

miCursor = miConexion.cursor()

variosProductos = [
    ("Camisa", 100, "Deportes"),
    ("Jarron", 20, "Ceramica"),
    ("Camion", 30, "Jugueteria")
    ]
miCursor.executemany("INSERT INTO Productos VALUES(?,?,?)", variosProductos)

miConexion.commit()

miConexion.close()
