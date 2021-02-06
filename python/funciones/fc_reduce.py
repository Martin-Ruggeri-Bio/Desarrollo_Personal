from functools import reduce


def concatenar(a, b):
    return a+b


s1 = ("H", "E", "L", "L", "O", "_", "w", "O", "R", "D")
sr = reduce(concatenar, s1)

print(type(s1))
print(s1)
print(type(sr))
print(sr)
