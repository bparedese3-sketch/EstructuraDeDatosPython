#Dada la lista ["a", "b", "a", "c", "b", "d"], retorna una nueva lista sin duplicados respetando el orden de la primera aparición. (Con set se pierde el orden — hay que combinar set + list.)
datos = ["a", "b", "a", "c", "b", "d"]
vistos = set()
resultado = []
for x in datos:
    if x not in vistos:
        vistos.add(x)
        resultado.append(x)
print(resultado)  # ['a', 'b', 'c', 'd']