import pandas as pd
import requests
import io

file_id = '1vouC--JfZgZpyQoHZ2px9FZaDhWocO_y'
url = f'https://drive.google.com/uc?export=download&id={file_id}'

try:
    response = requests.get(url)
    df = pd.read_excel(io.BytesIO(response.content))
    print("✅ Excel cargado correctamente")
    print(df.head())  # Muestra las primeras filas
except Exception as e:
    print("❌ Error al cargar el Excel:")
    print(e)
