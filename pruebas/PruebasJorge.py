import datetime

# Obtener fecha y hora actual
ahora = datetime.datetime.now()
print("Fecha y hora actual:", ahora)

# Formatear fecha y hora (ej: 09/04/2026 15:30:00)
formato = ahora.strftime("%d/%m/%Y %H:%M:%S")
print("Formateado:", formato)

nombre_archivo = "Estadisticas_" +str(ahora)+ ".txt"

with open(nombre_archivo, "w", encoding="utf-8") as f:
    f.write("Hola, este es un archivo nuevo.\n")
    f.write("Segunda línea.\n")

# Añade contenido al final
with open(nombre_archivo, "a", encoding="utf-8") as f:
    f.write("Esta línea se añade al final.\n")
