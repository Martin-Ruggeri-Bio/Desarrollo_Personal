from io import open

archivo_texto = open("archivo.txt", "r")
texto = archivo_texto.read()
archivo_texto.seek(0)
lineas_texto = archivo_texto.readlines()
archivo_texto.seek(0)
texto_2 = archivo_texto.read(11)
# posicionarme en el medio del texto + 2
archivo_texto.seek(0)
archivo_texto.seek(len(archivo_texto.read())/2 + 2)
texto_3 = archivo_texto.read()
archivo_texto.close()
print(texto)
print(lineas_texto)
print(texto_2)
print(texto_3)
