import random
import datetime
import sys
import time

# elige un valor del intervalo
# incluye
valor = random.randint(0, 10)
print(valor)

# elige un valor de la lista
lista = [True, "Strings", 23, False]
valor = random.choice(lista)
print(valor)

# desordena una lista
print(lista)
random.shuffle(lista)
print(lista)

print(datetime.datetime.now())

for i in range(100):
    # time nos permite colocar el delay
    time.sleep(0.5)
    # nos escribe la barra de progreso o texto
    # /r nos permite que se sobreescriba en el mismo espacio de memoria
    # el primer % es para concatenar y el segundo es el que quiero concatenar
    sys.stdout.write("\r %d %%" % i)
    # flush nospermite que se repita
    sys.stdout.flush()
