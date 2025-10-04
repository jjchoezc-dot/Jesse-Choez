# Crear y escribir un archivo llamado my_notes.txt con tres líneas de notas personales
with open("my_notes.txt", "w") as file:
    file.write("Nota 1: Recordar enviar el informe antes del viernes.\n")
    file.write("Nota 2: Revisar los correos pendientes.\n")
    file.write("Nota 3: Preparar la presentación para la reunión.\n")

# Abrir el archivo para leer línea por línea usando readline() y mostrar el contenido
with open("my_notes.txt", "r") as file:
    # Leer la primera línea
    line = file.readline()
    while line:
        print(line.strip())  # Mostrar la línea sin el salto de línea extra
        line = file.readline()

# Los bloques 'with' aseguran el cierre automático del archivo, no es necesario cerrarlos manualmente
