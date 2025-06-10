mi_ruta= "C:\\Users\\alond\\OneDrive\\Documentos\\semana12\\datos\\"
mi_archivo = open(mi_ruta + 'datos.txt', 'r')
contenido = mi_archivo.read()
print(contenido)
mi_archivo.close()