def calcular_temperatura_promedio(datos_ciudades):
    """
    Esta función calcula la temperatura promedio de cada ciudad.
    Toma un diccionario de ciudades y sus temperaturas como entrada.
    """
    promedios = {}  # Este diccionario guardará los resultados

    #Iteramos sobre cada ciudad en el diccionario de datos
    for ciudad, semanas in datos_ciudades.items():
        total_temperatura = 0
        total_dias = 0

        #Iteramos sobre cada semana para obtener los datos
        for semana in semanas:
            # Iteramos sobre cada día de la semana para sumar las temperaturas
            for dia, temp in semana.items():
                total_temperatura += temp
                total_dias += 1

        #Calculamos el promedio y lo guardamos en el diccionario de promedios
        promedio = total_temperatura / total_dias
        promedios[ciudad] = promedio

    return promedios


#Datos de temperaturas de tus clases anteriores
temperaturas_ciudades = {
    'Guayaquil': [
        {'Lunes': 30, 'Martes': 30, 'Miércoles': 30, 'Jueves': 30, 'Viernes': 30, 'Sábado': 30, 'Domingo': 30},
        {'Lunes': 29, 'Martes': 30, 'Miércoles': 31, 'Jueves': 30, 'Viernes': 30, 'Sábado': 30, 'Domingo': 30}
    ],
    'Cuenca': [
        {'Lunes': 18, 'Martes': 18, 'Miércoles': 18, 'Jueves': 19, 'Viernes': 18, 'Sábado': 18, 'Domingo': 19},
        {'Lunes': 17, 'Martes': 17, 'Miércoles': 17, 'Jueves': 18, 'Viernes': 18, 'Sábado': 18, 'Domingo': 18}
    ],
    'Manta': [
        {'Lunes': 26, 'Martes': 26, 'Miércoles': 27, 'Jueves': 27, 'Viernes': 26, 'Sábado': 27, 'Domingo': 27},
        {'Lunes': 26, 'Martes': 28, 'Miércoles': 27, 'Jueves': 28, 'Viernes': 27, 'Sábado': 28, 'Domingo': 28}
    ]
}

#Llama a la función y guarda el resultado
promedios_ciudades = calcular_temperatura_promedio(temperaturas_ciudades)

#Imprime el resultado
for ciudad, promedio in promedios_ciudades.items():
    print(f'Temperatura promedio en {ciudad}: {promedio:.2f} grados')