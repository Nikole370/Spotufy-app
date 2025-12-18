import pandas as pd

# Cargar archivo CSV
df = pd.read_csv("canciones_con_genero.csv")

# Reemplazar valores nulos si los hubiera
df["Géneros"] = df["Géneros"].fillna("Desconocido")

# Separar géneros múltiples por coma y expandir filas
df_generos = df["Géneros"].str.split(",", expand=True).stack().reset_index(drop=True)
df_generos = df_generos.str.strip()  # Eliminar espacios

# Contar ocurrencias de cada género
conteo = df_generos.value_counts().reset_index()
conteo.columns = ["Género", "Cantidad"]

# Mostrar en orden descendente
print(conteo)
