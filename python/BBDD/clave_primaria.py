import sqlite3

miConexion = sqlite3.connect("Gestion_Productos")

miCursor = miConexion.cursor()

miCursor.execute(
    '''CREATE TABLE Productos(
        Codigo_Articulo VARCHAR(4) PRIMARY KEY,
        NOmbre_Articulo VARCHAR(50),
        Precio INTERGER,
        Seccion VARCHAR(20)
        )
    ''')

variosProductos = [
    ("AR01", "Camisa", 100, "Urbano"),
    ("AR02", "Jarron", 20, "Ceramica"),
    ("AR03", "Camion", 30, "Jugueteria"),
    ("AR04", "Camiseta", 50, "Deporte")
    ]
miCursor.executemany(
    "INSERT INTO Productos VALUES(?,?,?,?)",
    variosProductos
    )

miConexion.commit()

miConexion.close()
