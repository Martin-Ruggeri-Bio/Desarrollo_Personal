def palindromo(frase):
    frase = frase.replace(" ", "")
    return frase == frase[::-1]
    # :: no regresa la cadena al reves


frase = "anita lava la tina"
print(palindromo(frase))
