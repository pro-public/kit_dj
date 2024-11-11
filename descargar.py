import os
import re

# Ruta del archivo
file_path = 'data/this.txt'

# Expresión regular para validar URLs
url_pattern = re.compile(
    r'^(https?:\/\/)?(www\.)?([a-zA-Z0-9\-]+\.)+[a-zA-Z]{2,}(:\d+)?(\/\S*)?$'
)

def is_valid_url(url):
    """Verifica si una URL es válida."""
    return bool(url_pattern.match(url))

def process_file(file_path):
    """Lee el archivo y procesa cada línea."""
    if not os.path.isfile(file_path):
        print(f"El archivo '{file_path}' no existe.")
        return

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            fields = line.strip().split('-')

            # Verificar que la línea tenga al menos tres campos
            if len(fields) < 3:
                print(f"Línea {line_number} no tiene suficientes campos: {line.strip()}")
                continue

            # Tercer campo es el que contiene la URL
            url = fields[2].strip()

            # Validar si el tercer campo es una URL válida
            if is_valid_url(url):
                # Ejecutar el comando spotdl
                command = f'spotdl {url}'
                print(f"Ejecutando: {command}")
                os.system(command)  # Ejecuta el comando en la terminal
            else:
                print(f"Línea {line_number} tiene una URL inválida: {url}")

# Ejecutar la función principal
process_file(file_path)

