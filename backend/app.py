from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    # Fazendo uma requisição à API para obter o valor do dólar em tempo real
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    dollar_rate = data['rates']['BRL']  # Obtendo o valor do dólar em relação ao real brasileiro
    return jsonify({'dollar_rate': dollar_rate})

if __name__ == '__main__':
    app.run(debug=True)
