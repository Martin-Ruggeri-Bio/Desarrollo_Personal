import re

lista_nombres = [
    'Ana Gomez',
    'Maria Martin',
    'Sandra Lopez',
    'Sandra Martin',
    'Ñata',
    'Niños',
    'Niñas',
    'Camion',
    'Camión'
]

for elemento in lista_nombres:
    # empieza
    if re.findall('^Sandra', elemento):
        print(elemento)
print("\n")
for elemento in lista_nombres:
    # termina
    if re.findall('Martin$', elemento):
        print(elemento)
print("\n")
for elemento in lista_nombres:
    # que tenga
    if re.findall('[Ñ]', elemento):
        print(elemento)
print("\n")
for elemento in lista_nombres:
    # cualquiera de las 2
    if re.findall('Niñ[oa]s', elemento):
        print(elemento)
print("\n")
for elemento in lista_nombres:
    if re.findall('Cami[oó]n', elemento):
        print(elemento)
print("\n")
for elemento in lista_nombres:
    # rangos
    if re.findall('[o-z]$', elemento):
        print(elemento)
print("\n")
# negacion del rango
for elemento in lista_nombres:
    if re.findall('[^o-z]$', elemento):
        print(elemento)
print("\n")
