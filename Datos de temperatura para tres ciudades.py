# Matriz 3D para almacenar datos de temperaturas en ciudades del Ecuador
# Dimensión 1: Ciudades (Guayaquil, Cuenca, Manta)
# Dimensión 2: Semanas (4 semanas)
# Dimensión 3: Días de la semana (7 días)
temperaturas_ecuador = [
    # Guayaquil
    [
        # Semana 1
        [{"day": "Lunes", "temp": 30}, {"day": "Martes", "temp": 31}, {"day": "Miércoles", "temp": 32}, {"day": "Jueves", "temp": 30}, {"day": "Viernes", "temp": 33}, {"day": "Sábado", "temp": 34}, {"day": "Domingo", "temp": 32}],
        # Semana 2
        [{"day": "Lunes", "temp": 29}, {"day": "Martes", "temp": 30}, {"day": "Miércoles", "temp": 31}, {"day": "Jueves", "temp": 30}, {"day": "Viernes", "temp": 32}, {"day": "Sábado", "temp": 33}, {"day": "Domingo", "temp": 31}],
        # Semana 3
        [{"day": "Lunes", "temp": 31}, {"day": "Martes", "temp": 32}, {"day": "Miércoles", "temp": 33}, {"day": "Jueves", "temp": 31}, {"day": "Viernes", "temp": 34}, {"day": "Sábado", "temp": 35}, {"day": "Domingo", "temp": 33}],
        # Semana 4
        [{"day": "Lunes", "temp": 30}, {"day": "Martes", "temp": 31}, {"day": "Miércoles", "temp": 32}, {"day": "Jueves", "temp": 31}, {"day": "Viernes", "temp": 33}, {"day": "Sábado", "temp": 34}, {"day": "Domingo", "temp": 32}]
    ],
    # Cuenca
    [
        # Semana 1
        [{"day": "Lunes", "temp": 18}, {"day": "Martes", "temp": 19}, {"day": "Miércoles", "temp": 20}, {"day": "Jueves", "temp": 19}, {"day": "Viernes", "temp": 21}, {"day": "Sábado", "temp": 22}, {"day": "Domingo", "temp": 20}],
        # Semana 2
        [{"day": "Lunes", "temp": 17}, {"day": "Martes", "temp": 18}, {"day": "Miércoles", "temp": 19}, {"day": "Jueves", "temp": 18}, {"day": "Viernes", "temp": 20}, {"day": "Sábado", "temp": 21}, {"day": "Domingo", "temp": 19}],
        # Semana 3
        [{"day": "Lunes", "temp": 19}, {"day": "Martes", "temp": 20}, {"day": "Miércoles", "temp": 21}, {"day": "Jueves", "temp": 20}, {"day": "Viernes", "temp": 22}, {"day": "Sábado", "temp": 23}, {"day": "Domingo", "temp": 21}],
        # Semana 4
        [{"day": "Lunes", "temp": 18}, {"day": "Martes", "temp": 19}, {"day": "Miércoles", "temp": 20}, {"day": "Jueves", "temp": 19}, {"day": "Viernes", "temp": 21}, {"day": "Sábado", "temp": 22}, {"day": "Domingo", "temp": 20}]
    ],
    # Manta
    [
        # Semana 1
        [{"day": "Lunes", "temp": 27}, {"day": "Martes", "temp": 28}, {"day": "Miércoles", "temp": 29}, {"day": "Jueves", "temp": 28}, {"day": "Viernes", "temp": 30}, {"day": "Sábado", "temp": 31}, {"day": "Domingo", "temp": 29}],
        # Semana 2
        [{"day": "Lunes", "temp": 26}, {"day": "Martes", "temp": 27}, {"day": "Miércoles", "temp": 28}, {"day": "Jueves", "temp": 27}, {"day": "Viernes", "temp": 29}, {"day": "Sábado", "temp": 30}, {"day": "Domingo", "temp": 28}],
        # Semana 3
        [{"day": "Lunes", "temp": 28}, {"day": "Martes", "temp": 29}, {"day": "Miércoles", "temp": 30}, {"day": "Jueves", "temp": 29}, {"day": "Viernes", "temp": 31}, {"day": "Sábado", "temp": 32}, {"day": "Domingo", "temp": 30}],
        # Semana 4
        [{"day": "Lunes", "temp": 27}, {"day": "Martes", "temp": 28}, {"day": "Miércoles", "temp": 29}, {"day": "Jueves", "temp": 28}, {"day": "Viernes", "temp": 30}, {"day": "Sábado", "temp": 31}, {"day": "Domingo", "temp": 29}]
    ]
]
# Lista de los nombres de cada ciudad
ciudades_nombres = ["Guayaquil", "Cuenca", "Manta"]

# Iterar a través de cada ciudad y semana para calcular el promedio de las temperaturas
for ciudad_idx, ciudad_data in enumerate(temperaturas_ecuador):
    print(f"--- Promedios de temperaturas para {ciudades_nombres[ciudad_idx]} ---")

    # El bucle interior itera sobre cada semana de la ciudad
    for semana_idx, semana_data in enumerate(ciudad_data):
        # Sumar todas las temperaturas en la semana actual
        suma_temperaturas = sum([dia["temp"] for dia in semana_data])

        # Calcular el promedio
        promedio = suma_temperaturas / len(semana_data)

        # Mostrar el resultado
        print(f"Semana {semana_idx + 1}: {promedio:.2f} grados")