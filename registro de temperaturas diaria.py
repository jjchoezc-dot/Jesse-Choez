# -----------------------------------------
# MATRIZ 3D: ciudades × semanas × días
# -----------------------------------------

ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Definimos la matriz 3D con temperaturas fijas
matriz_3d = [
    [   # Quito
        [15, 16, 14, 18, 20, 19, 17],  # Semana 1
        [21, 20, 22, 19, 18, 20, 21]   # Semana 2
    ],
    [   # Guayaquil
        [28, 29, 30, 31, 29, 28, 30],  # Semana 1
        [27, 26, 28, 29, 30, 31, 32]   # Semana 2
    ],
    [   # Cuenca
        [12, 13, 14, 13, 12, 15, 14],  # Semana 1
        [16, 15, 17, 18, 16, 15, 17]   # Semana 2
    ]
]

# -----------------------------------------
# Exploración de la matriz 3D
# -----------------------------------------
print("Exploración de la matriz 3D (temperaturas diarias):")
for i, ciudad in enumerate(ciudades):
    print(f"\nCiudad: {ciudad}")
    for s, semana in enumerate(matriz_3d[i]):
        print(f"  Semana {s+1}: ", end="")
        for d, temp in enumerate(semana):
            print(f"{dias[d]}={temp}°C ", end="")
        print()

# -----------------------------------------
# Cálculo de promedios por ciudad y semana
# -----------------------------------------
print("\nPromedios de temperatura por ciudad y semana:")
for i, ciudad in enumerate(ciudades):
    for s, semana in enumerate(matriz_3d[i]):
        suma = sum(semana)
        promedio = suma / len(semana)
        print(f"{ciudad} - Semana {s+1}: {promedio:.2f} °C")
