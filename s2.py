import pandas as pd
import time
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

# Autenticación
sp = Spotify(auth_manager=SpotifyClientCredentials(
    client_id="fe693c22fb5448bd92b2fd21d079cd66",
    client_secret="825f62a5e6a14ce685ff46fc58e490ad"

))
# Leer tu CSV
df = pd.read_csv("canciones_likeadas.csv")

# Crear lista para géneros
generos = []

# Buscar género por artista
for artista in df['Artista']:
    try:
        resultados = sp.search(q=f"artist:{artista}", type='artist', limit=1)
        items = resultados['artists']['items']
        if items:
            generos.append(", ".join(items[0]['genres']))
        else:
            generos.append("Desconocido")
    except Exception as e:
        generos.append("Error")
    time.sleep(0.1)  # evitar rate limit

# Agregar columna al DataFrame
df["Géneros"] = generos

# Guardar nuevo CSV
df.to_csv("canciones_con_genero.csv", index=False, encoding="utf-8")
