from flask import Flask, render_template
import pandas as pd
import requests
import io

app = Flask(__name__)

@app.route('/')
def mostrar_precios():
    file_id = '1vouC--JfZgZpyQoHZ2px9FZaDhWocO_y'
    url = f'https://drive.google.com/uc?export=download&id={file_id}'

    try:
        response = requests.get(url)
        df = pd.read_excel(io.BytesIO(response.content))
        df = df.fillna('')
        return render_template('precios.html', tabla=df.to_dict(orient='records'))
    except Exception as e:
        return f"<h1>Error al cargar precios</h1><p>{e}</p>"

if __name__ == '__main__':
    app.run(debug=True)
