try:
    archivo = open("ej.txt", "a")
except Exception:
    print("error")
    exit()

archivo.write(", es mi primer archivo")
archivo.seek(0, 2)
archivo.write("new ")

agregar = ["Hola mundo\n", "\tHola Programadores"]
archivo.writelines(agregar)
archivo.close()

if not archivo.closed:
    archivo.write("\n el archivo no se cerro")
