from flask import Flask, render_template, redirect
import requests
import logging
import json

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route("/")
def home():
    try:
        url = f"http://api-service:{81}"
        res = requests.get(url).json()
        return render_template('table.html', perfiles=res)
    except Exception as e:
        logging.debug(e)
        return {'message': 'Error en la consulta WEB'}


@app.route("/admin")
def admin():
    try:
        return render_template('admin.html', context={})
    except Exception as e:
        logging.debug(e)
        return {'message': 'Error en admin WEB'}


@app.route("/admin/insert")
def insert():
    try:
        url = f'http://api-service:{81}/admin/insert'
        requests.get(url).json()
        return redirect('/admin')
    except Exception as e:
        logging.debug(e)
        return {'message': 'Error al realizar insert WEB'}


@app.route("/admin/delete")
def delete():
    try:
        url = f'http://api-service:{81}/admin/delete'
        requests.get(url).json()
        return redirect('/admin')
    except Exception as e:
        logging.debug(e)
        return {'message': 'Error al realizar delete WEB'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=82, debug=True)
