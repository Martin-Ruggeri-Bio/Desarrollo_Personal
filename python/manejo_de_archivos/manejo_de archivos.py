from io import open

archivo_texto = open("archivo.txt", "w")
frase = "es un estupendodo dia"
archivo_texto.write(frase)
archivo_texto.close()
