try:
    archivo = open("ej.txt", "w")
except Exception:
    print("error")
    exit()

archivo.write("Hello world")
archivo.close()
