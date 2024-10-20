# Nombre del archivo
archivo = "this.txt"

# Abrir el archivo y procesar cada línea
with open(archivo, "r", encoding="utf-8") as file:
    for linea in file:
        # Eliminar espacios en blanco al principio y final de la línea
        linea = linea.strip()

        # Separar por el símbolo "-"
        if "-" in linea:
            tema, artista = linea.split(" - ", 1)
            print(f"Tema: {tema}, Artista: {artista}")
        else:
            print(f"Línea con formato incorrecto: {linea}")

