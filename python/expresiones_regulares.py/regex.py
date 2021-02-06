import re

cadena = "Vamos a aprender python. Vamos a aprender expresiones regulares"
texto_buscado = "aprender"
texto_encontrado = re.search(texto_buscado, cadena)

if texto_encontrado is not None:
    print("He encontrado el texto")
    print(texto_encontrado.start())
    print(texto_encontrado.end())
    print(texto_encontrado.span())
    print(re.findall(texto_buscado, cadena))
    print(len(re.findall(texto_buscado, cadena)))
else:
    print("No he encontrado el texto")
