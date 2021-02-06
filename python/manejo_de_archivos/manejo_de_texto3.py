from io import open

archivo_texto = open("archivo.txt", "a")
frase = "\n es un dia de sol"
archivo_texto.write(frase)
archivo_texto.close()
