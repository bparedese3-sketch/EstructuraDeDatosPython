#Dado un texto, retorna un diccionario con la frecuencia de cada palabra (ignora mayúsculas). Al final, imprime la palabra que más se repite.
texto = "El perro y el gato y el perro"
conteo = {}
for palabra in texto.lower().split():
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(conteo)

mas = max(conteo, key=conteo.get)
print(f"Más repetida: '{mas}' ({conteo[mas]} veces)")