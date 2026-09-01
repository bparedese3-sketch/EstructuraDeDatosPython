# Rediseñar el menú de saludar/despedir del módulo 3, pero esta vez con cada opción como función separada.
# Añade una función calcular() que pida dos números y muestre suma, resta, multiplicación y división. Nueva opción del menú.
def saludar():
    nombre = input("Nombre: ")
    print(f"¡Hola, {nombre}!")

def despedir():
    nombre = input("Nombre: ")
    print(f"¡Adiós, {nombre}!")

def calcular():
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))

    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicación: {num1 * num2}")

    if num2 != 0:
        print(f"División: {num1 / num2}")
    else:
        print("División: No se puede dividir para cero")

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Despedir")
    print("3. Salir")

while True:
    mostrar_menu()
    opcion = input("Opción: ")
    if opcion == "1":
        saludar()
    elif opcion == "2":
        despedir()
    elif opcion == "3":
        print("Adiós")
        break
    elif opcion == "4":
        calcular()
    else:
        print("Opción inválida")