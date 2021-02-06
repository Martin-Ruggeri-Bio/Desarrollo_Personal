from io import open
# lectura y escritura
archivo_texto = open("archivo.txt", "r+")
# frase = "comienzo de cancion"
# archivo_texto.write(frase)
lineas_texto = archivo_texto.readlines()
lineas_texto[1] = "lineal del exterior\n"
archivo_texto.seek(0)
archivo_texto.writelines(lineas_texto)
archivo_texto.close()
