import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Tus credenciales de Spotify (las obtienes al crear la app en Spotify Developer)
client_id = "TU_CLIENT_ID"
client_secret = "TU_CLIENT_SECRET"

# Configurar autenticación con la API de Spotify
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Nombre del archivo de entrada/salida
archivo = "this.txt"

def buscar_en_spotify(tema, artista):
    query = f"{tema} {artista}"
    resultado = sp.search(q=query, type='track', limit=1)
    tracks = resultado.get('tracks', {}).get('items', [])
    if tracks:
        # Si se encontró un resultado, devolver la URL del primer track
        return tracks[0]['external_urls']['spotify']
    return "not found"

# Leer el archivo original
with open(archivo, "r", encoding="utf-8") as file:
    lineas = file.readlines()

# Reescribir el archivo con las URLs de Spotify
with open(archivo, "w", encoding="utf-8") as file:
    for linea in lineas:
        linea = linea.strip()
        if "-" in linea:
            tema, artista = linea.split(" - ", 1)
            url_spotify = buscar_en_spotify(tema, artista)
            file.write(f"{tema} - {artista} - {url_spotify}\n")
        else:
            file.write(f"{linea} - formato incorrecto\n")

