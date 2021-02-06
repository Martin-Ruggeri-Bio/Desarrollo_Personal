from functools import reduce


mi_funcion = lambda valor1, valor2: valor1 + valor2
formato = lambda sentencia: "¿{}?".format(sentencia)
no_valor = lambda: 10
resultado1 = mi_funcion(4, 6)
resultado2 = formato("puedo hacer un pregunta")
resultado3 = no_valor()
print(resultado1)
print(resultado2)
print(resultado3)

l1 = [1, -2, 1, -4]
l2 = [5, 3, 6, 7]
s1 = "hello word"
s2 = ("H", "E", "L", "L", "O", "_", "w", "O", "R", "D")

fc_map = list(map(lambda n, m: n+m, l1, l2))
fc_filter = list(filter(lambda n: n == "o", s1))
fc_reduce_int = reduce(lambda n, m: n+m, l2)
fc_reduce_str = reduce(lambda n, m: n+m, s2)

print(fc_map)
print(fc_filter)
print(fc_reduce_int)
print(fc_reduce_str)
