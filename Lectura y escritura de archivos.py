# Lectura y Escritura de Archivos
file_name = "my_notes.txt"
# Escritura de Archivo de Texto: my_notes.txt
# Abrimos en modo "w" (write) y escribimos tres líneas.
try:
    archivo = open(file_name, "w")  # Apertura para escritura [cite: 85]
    # Uso conciso de write() para las tres líneas.
    archivo.write("Apuntes rapidos sobre Python:\n")
    archivo.write("La funcion open() requiere el nombre del archivo y el modo de interaccion.\n")
    archivo.write("Para la lectura linea por linea se usa el metodo readline().\n")

except Exception as e:
    print(f"Error durante la escritura: {e}")

finally:
    # 3. Cierre de Archivos: Es esencial cerrar el archivo.
    if 'archivo' in locals() and not archivo.closed:
        archivo.close()

# 2. Lectura de Archivo de Texto: my_notes.txt
# Abrimos en modo "r" (read) y leemos línea por línea.
try:
    archivo = open(file_name, "r")  # Apertura para lectura [cite: 87]

    print("\n--- Contenido Leído (Línea por Línea) ---")

    # Uso del metodo readline() para leer las lineas.
    linea1 = archivo.readline()  # Lee la primera línea
    linea2 = archivo.readline()  # Lee la segunda línea
    linea3 = archivo.readline()  # Lee la tercera línea

    # Mostrar cada línea leída (strip() para remover el salto de línea).
    print(f"L1: {linea1.strip()}")
    print(f"L2: {linea2.strip()}")
    print(f"L3: {linea3.strip()}")
    print("------------------------------------------")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo {file_name} para lectura.")
except Exception as e:
    print(f"Error durante la lectura: {e}")

finally:
    # 3. Cierre de Archivos: Cierre final del archivo.
    if 'archivo' in locals() and not archivo.closed:
        archivo.close()