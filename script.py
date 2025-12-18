import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="fe693c22fb5448bd92b2fd21d079cd66",
    client_secret="825f62a5e6a14ce685ff46fc58e490ad",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-library-read"
))

# Obtener canciones
results = sp.current_user_saved_tracks(limit=50)
tracks = []

while results:
    for item in results['items']:
        track = item['track']
        tracks.append({
            'Nombre': track['name'],
            'Artista': track['artists'][0]['name'],
            'Álbum': track['album']['name'],
            'Fecha añadida': item['added_at'],
            'Duración (ms)': track['duration_ms'],
            'Popularidad': track['popularity']
        })

    if results['next']:
        results = sp.next(results)
    else:
        break

# Guardar en Excel o CSV
df = pd.DataFrame(tracks)
df.to_csv("canciones_likeadas.csv", index=False, encoding='utf-8')
