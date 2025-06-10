"""Ejercicio 1: Diario Personal
• Problema: Escribe un programa que funcione como un diario simple. Cada vez que se
ejecute, debe solicitar al usuario una entrada de texto y la guardará, junto con la fecha y hora
actual, en un archivo llamado diario.txt. Cada nueva entrada debe añadirse al final del
archivo sin borrar las anteriores.
• Paso a paso:
1. Importar el módulo datetime para obtener la fecha y hora.
2. Solicitar al usuario que ingrese el texto para su entrada del diario.
3. Abrir el archivo diario.txt en modo de adición ('a').
4. Escribir la fecha y hora actual, seguida de la entrada del usuario. Asegurarse de
añadir un salto de línea para separar las entradas.
5. Cerrar el archivo.
6. Mostrar un mensaje de confirmación al usuario.
"""
import datetime

mi_ruta = r"C:\Users\alond\OneDrive\Documentos\semana12\diario.txt"
mi_archivo = open (mi_ruta + 'diario.txt', 'a')
texto = input("Escribe la entrada de tu diario: ")
fecha_hora = datetime.datetime.now()
mi_archivo.write(f"{fecha_hora}-{texto}\n")
mi_archivo.close()
print("Tu entrada ha sido guardada con éxito")