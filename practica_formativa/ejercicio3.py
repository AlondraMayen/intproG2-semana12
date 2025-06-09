"""Ejercicio 3: Calcular la suma de los dígitos de un número elevado a una potencia
Planteamiento: Crea una función que reciba dos parámetros: 
un número entero positivo y un exponente. La función debe calcular 
el número elevado al exponente dado, luego sumar todos los dígitos 
del resultado y devolver esa suma. Por ejemplo, si el número es 2 
y el exponente es 3, calcula  2^3 = 8, y la suma de los dígitos es 8. 
Si el número es 5 y el exponente es 2, calcula 5^2 = 25, y la suma de los dígitos es 2 + 5 = 7."""

def suma_digitos_potencia(base, exponente):
    # Calcula la potencia
    resultado = base ** exponente

    # Convierte el resultado a cadena para poder recorrer cada dígito
    resultado_str = str(resultado)

    # Inicializa la suma
    suma = 0

    # Recorre cada carácter (dígito) y lo convierte a número para sumarlo
    for digito in resultado_str:
        suma += int(digito)

    # Devuelve la suma de los dígitos
    return suma

# Solicita los valores al usuario
base = int(input("Ingrese un número entero positivo (base): "))
exponente = int(input("Ingrese el exponente: "))

# Muestra el resultado
print(f"La suma de los dígitos de {base}^{exponente} es: {suma_digitos_potencia(base, exponente)}")
