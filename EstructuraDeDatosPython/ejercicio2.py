#Ejercicio 2: Leer tres notas de un estudiante y mostrar su promedio.
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

promedio =  (nota1 + nota2 + nota3) / 3

if promedio >= 7:
    print (f"El promedio es: {promedio:.1f}",", aprobado" )
else:
     print (f"El promedio es: {promedio:.1f}",", reprobado")




