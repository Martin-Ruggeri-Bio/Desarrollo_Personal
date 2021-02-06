def filtro_str(elem):
    return(elem == "o")


def filtro_int(elem):
    return(elem > 0)


s1 = "hello word"
l1 = [1, -3, 2, -7, 8, 3]

lr = list(filter(filtro_int, l1))
ls = list(filter(filtro_str, s1))

print(l1)
print(lr)
print(ls)
