"""Ejercicio 2: Convertir un número decimal a binario
Planteamiento: Escribe una función que reciba un número entero positivo 
y devuelva una cadena con su representación en binario (base 2). 
Por ejemplo, si se ingresa 10, la función debe devolver "1010". 
No uses funciones integradas de conversión a binario; implementa la lógica dividiendo 
el número y construyendo la cadena manualmente."""

def decimal_a_binario(n):
    # Si el número es 0, el binario es "0"
    if n == 0:
        return "0"
    
    # Variable para guardar los restos (dígitos binarios)
    binario = ""

    # Mientras el número sea mayor que 0
    while n > 0:
        # Obtenemos el residuo de dividir entre 2 (0 o 1)
        residuo = n % 2 # % = modulo

        # Convertimos el residuo a cadena y lo agregamos al inicio
        binario = str(residuo) + binario # str = convierte un valor a cadena de texto

        # Dividimos el número entre 2 (división entera)
        n = n // 2

    # Devolvemos la cadena binaria final
    return binario

# Solicita al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Llama a la función y muestra el resultado
print(f"El número {numero} en binario es: {decimal_a_binario(numero)}")