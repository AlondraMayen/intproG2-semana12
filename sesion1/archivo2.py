try:
    mi_ruta = "C:\\Users\\alond\\OneDrive\\Documentos\\semana12" 
    
    mi_archivo = open(mi_ruta + "notas.txt, 'w")
    mi_archivo.write("Hola mundo...")
    mi_archivo.close()
    
except Exception:
    print("Error")