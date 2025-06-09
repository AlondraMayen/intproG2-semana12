"""Ejercicio 1: Calcular el factorial de un número

Planteamiento: Crea una función que reciba un número entero no negativo como parámetro
y devuelva su factorial. El factorial de un número n es el producto de todos los enteros 
positivos desde 1 hasta n (por ejemplo, 5! = 5 * 4 * 3 2   1 = 120). 
Asegúrate de manejar el caso especial donde n = 0, que devuelve 1."""

def factorial(n):
    # Si el número es negativo, se devuelve un mensaje de error
    if n < 0:
        return "Error: el número debe ser no negativo"

    # Si el número es 0, el factorial es 1 por definición
    if n == 0:
        return 1

    # Se inicializa el resultado
    resultado = 1

    # Se calcula el factorial multiplicando desde 1 hasta n
    for i in range(1, n + 1):
        resultado *= i

    # Se devuelve el resultado final
    return resultado

# Solicita al usuario el número
numero = int(input("Ingrese un número entero no negativo: "))

# Llama a la función y muestra el resultado
print(f"El factorial de {numero} es {factorial(numero)}")