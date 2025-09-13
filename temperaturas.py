def calcular_promedio_temperaturas(datos):
    """
    Calcula la temperatura promedio para cada ciudad.

    Parámetros:
    datos (dict): Diccionario donde la clave es el nombre de la ciudad y el valor
                  es una lista con las temperaturas semanales.

    Retorna:
    dict: Diccionario con la ciudad como clave y la temperatura promedio como valor.
    """
    promedios = {}
    for ciudad, temperaturas in datos.items():
        if len(temperaturas) == 0:
            promedio = 0
        else:
            promedio = sum(temperaturas) / len(temperaturas)
        promedios[ciudad] = promedio
    return promedios


# Ejemplo de datos
datos_temperaturas = {
    "CiudadA": [20, 22, 19, 21],
    "CiudadB": [25, 24, 23, 26],
    "CiudadC": [18, 17, 19, 16]
}

# Probar la función
if __name__ == "__main__":
    promedios = calcular_promedio_temperaturas(datos_temperaturas)
    print("Temperaturas promedio por ciudad:", promedios)
