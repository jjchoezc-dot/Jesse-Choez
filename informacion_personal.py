# Crear el diccionario con datos iniciales
informacion_personal = {
    "nombre": "Carlos Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor para la "profesion" de la persona
# Nota: La clave "profesion" ya existe, para agregar otra profesión, podemos usar otra clave.
informacion_personal["profesion_secundaria"] = "Docente"

# Verificar si la clave "telefono" existe; si no, agregarla con un número ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593987654321"

# Eliminar la clave "edad" ya que no es necesaria
del informacion_personal["edad"]

# Imprimir el diccionario final después de todas las modificaciones
print(informacion_personal)
