"""estos son scripts en python"""
import sys

if __name__ == "__main__":
    # si es el script principal
    if len(sys.argv) == 1:
        print("Es necesario colocar al menos un argumento")
    elif sys.argv[1] == "help":
        print("puedes contactar a martinruggeri18@gmail.com")
    else:
        # imprime los argumentos del modulo
        print(sys.argv)
