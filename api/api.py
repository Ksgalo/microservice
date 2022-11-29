from unittest import result
from flask import Flask
import requests
import logging
import json

app = Flask(__name__)


@app.route('/')
def home():
    try:
        url = f'http://faker-service:{80}/select'
        res = requests.get(url).json()
        return json.dumps(res)
    except Exception as e:
        logging.debug(e)
        return {'message': 'Error al realizar consulta API'}


@app.route('/admin/insert')
def insert():
    try:
        url = f'http://faker-service:{80}/insert'
        res = requests.get(url).json()
        return json.dumps(res)
    except Exception as e:
        logging.debug(e)
        return {'message': 'Error al realizar insert API'}


@app.route('/admin/delete')
def delete():
    try:
        url = f'http://faker-service:{80}/delete'
        res = requests.get(url).json()
        return json.dumps(res)
    except Exception as e:
        logging.debug(e)
        return {'message': 'Error al realizar delete API'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
