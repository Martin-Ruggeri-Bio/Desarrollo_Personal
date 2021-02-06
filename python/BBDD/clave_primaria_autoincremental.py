import sqlite3

miConexion = sqlite3.connect("Gestion_Productos_Incremental")

miCursor = miConexion.cursor()

miCursor.execute(
    '''CREATE TABLE Productos(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre_Articulo VARCHAR(50) UNIQUE,
        Precio INTERGER,
        Seccion VARCHAR(20)
        )
    ''')

variosProductos = [
    ("Camisa", 100, "Urbano"),
    ("Jarron", 20, "Ceramica"),
    ("Camion", 30, "Jugueteria"),
    ("Camiseta", 50, "Deporte")
    ]
miCursor.executemany(
    "INSERT INTO Productos VALUES(NULL,?,?,?)",
    variosProductos
    )

miConexion.commit()

miConexion.close()
