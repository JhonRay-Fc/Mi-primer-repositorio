#Diccionarios en Python

# Crear un Diccionario
# Se crea un diccionario llamado informacion_personal.
informacion_personal = {
    "nombre": "Jhon",
    "edad": 18,
    "ciudad": "Guayaquil",
    "profesion": "Estudiante de Tecnologías de la Información"
}
# Acceder y Modificar los Valores
# Acceder al valor de la clave "ciudad"
print("Ciudad actual:", informacion_personal["ciudad"])

# Modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Quito"
print("Ciudad modificada:", informacion_personal["ciudad"])

# 3. Verificar la existencia de Claves y Agregar
# Se verifica si la clave "telefono" existe en el diccionario.
# Si no existe, se agrega.
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "593-997666403"
    print("Se agregó la clave 'telefono'.")

# 4. Eliminar una Clave
# Se elimina la clave "edad" del diccionario.
if "edad" in informacion_personal:
    del informacion_personal["edad"]
    print("Se eliminó la clave 'edad'.")

# 5. Imprimir el Diccionario Final
# Se imprime el diccionario completo después de todas las operaciones.
print("\nDiccionario final:")
print(informacion_personal)