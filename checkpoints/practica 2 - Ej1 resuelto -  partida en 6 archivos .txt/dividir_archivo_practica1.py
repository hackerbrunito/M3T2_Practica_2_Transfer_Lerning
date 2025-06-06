def dividir_archivo_txt(nombre_archivo, num_partes=6):
    """
    Divide un archivo .txt en el número especificado de partes
    
    Args:
        nombre_archivo (str): Nombre del archivo a dividir
        num_partes (int): Número de partes en las que dividir el archivo
    """
    try:
        # Leer el archivo completo
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        
        # Calcular el tamaño de cada parte
        longitud_total = len(contenido)
        tamaño_parte = longitud_total // num_partes
        
        print(f"Archivo: {nombre_archivo}")
        print(f"Tamaño total: {longitud_total} caracteres")
        print(f"Tamaño por parte: aproximadamente {tamaño_parte} caracteres")
        print("-" * 50)
        
        # Dividir el contenido en partes
        for i in range(num_partes):
            inicio = i * tamaño_parte
            
            # Para la última parte, incluir todo lo que quede
            if i == num_partes - 1:
                fin = longitud_total
            else:
                fin = (i + 1) * tamaño_parte
            
            # Extraer la parte correspondiente
            parte_contenido = contenido[inicio:fin]
            
            # Crear nombre del archivo de salida
            nombre_base = nombre_archivo.replace('.txt', '')
            nombre_salida = f"{nombre_base}_parte_{i+1}.txt"
            
            # Guardar la parte en un nuevo archivo
            with open(nombre_salida, 'w', encoding='utf-8') as archivo_salida:
                archivo_salida.write(parte_contenido)
            
            print(f"Creado: {nombre_salida} ({len(parte_contenido)} caracteres)")
        
        print("-" * 50)
        print("¡División completada exitosamente!")
        
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{nombre_archivo}'")
    except Exception as e:
        print(f"Error inesperado: {e}")


import sys

# Ejemplo de uso
if __name__ == "__main__":
    # Verificar si se pasó un archivo como parámetro
    if len(sys.argv) > 1:
        nombre_archivo = sys.argv[1]
        print(f"Usando archivo desde parámetro: {nombre_archivo}")
    else:
        # Si no se pasa parámetro, usar nombre por defecto
        nombre_archivo = "mi_archivo.txt"
        print(f"No se especificó archivo, usando: {nombre_archivo}")
    
    # Verificar si se especificó número de partes (opcional)
    if len(sys.argv) > 2:
        try:
            num_partes = int(sys.argv[2])
            print(f"Dividiendo en {num_partes} partes")
        except ValueError:
            print("El segundo parámetro debe ser un número. Usando 6 partes por defecto.")
            num_partes = 6
    else:
        num_partes = 6
        print("Dividiendo en 6 partes por defecto")
    
    print("=" * 50)
    
    # Dividir el archivo
    dividir_archivo_txt(nombre_archivo, num_partes)