def operador(n, m):
    return n+m


l1 = [1, 2, 3, 4, 5]
t1 = (9, 8, 7, 6, 5)

lr = list(map(operador, l1, t1))
print(l1)
print(t1)
print(lr)
