import xml.etree.ElementTree as ET

# Ruta del archivo NML
file_path = 'data/this.nml'

# Función para extraer el título y el artista de cada track y guardarlos en un archivo .txt
def extract_tracks_to_txt(nml_file, output_file):
    # Parsear el archivo XML
    tree = ET.parse(nml_file)
    root = tree.getroot()

    # Crear/abrir el archivo de salida
    with open(output_file, 'w', encoding='utf-8') as f_out:
        # Recorrer cada entrada (track) dentro de <COLLECTION>
        for entry in root.findall(".//ENTRY"):
            title = entry.get('TITLE')
            artist = entry.get('ARTIST')
            
            # Verificar si ambos valores existen y escribirlos en el archivo
            if title and artist:
                f_out.write(f"{title} - {artist}\n")

# Definir la ruta del archivo de salida
output_file = 'data/this.txt'

# Ejecutar la función para extraer y guardar los datos
extract_tracks_to_txt(file_path, output_file)

# Mensaje de éxito
print(f"Los datos han sido guardados en {output_file}")

