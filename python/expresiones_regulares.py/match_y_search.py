import re

nombre1 = "Sandra Lopez"
nombre2 = "Antonio Gomez"
nombre3 = "Maria Lopez"
nombre4 = "sandra1 Lopez1"
nombre5 = "1sandra Lopez"

# match siempre busca al principio
if re.match("Sandra", nombre1):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")

# ignorar el camel case
if re.match("Sandra", nombre4, re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")

# sustituir un caracter por un punto
if re.match(".aria", nombre3):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")

# buscar un numero al principio
if re.match("\\d", nombre5):
    print("Hemos encontrado el numero")
else:
    print("No lo hemos encontrado")
if re.match("......\\d", nombre4):
    print("Hemos encontrado el numero")
else:
    print("No lo hemos encontrado")

# buscar un numero o caracter en toda la cadena
if re.search("\\d", nombre4):
    print("Hemos encontrado el numero")
else:
    print("No lo hemos encontrado")
if re.search("Lopez", nombre4):
    print("Hemos encontrado el numero")
else:
    print("No lo hemos encontrado")
