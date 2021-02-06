import sqlite3

miConexion = sqlite3.connect("PrimeraBase")
# creo mi primera tabla
miCursor = miConexion.cursor()
# ejecuto la consulta en SQL
# invalidp
miCursor.execute(
    "CREATE TABLE Productos(Nombre_articulo VARCHAR(50),\
     Precio INTEGER,\
     Seccion VARCHAR(20))")

miConexion.close()
