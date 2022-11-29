import json
from flask import Flask
from faker import Faker
from sqlalchemy import create_engine
import itertools
import logging

app = Flask(__name__)
faker = Faker()

logging.basicConfig(level=logging.DEBUG)


def FakerRandom():
    insert_query = []
    perfiles = [dict(itertools.islice(faker.profile().items(), 6))
                for data in range(13)]
    for perfil in perfiles:
        sql = ""
        for key, val in perfil.items():
            if key == 'current_location':
                coordenadas = [str(coordenada) for coordenada in val]
                perfil.update(
                    current_location=json.dumps({"coordenadas": coordenadas})
                )
        valores = (str(list(perfil.values())).replace('\\', '')[1:-1])
        # logging.debug(valores)
        sql = f"""
        INSERT INTO perfil(
            trabajo,empresa,ssn,residencia,direccion,grupo_sanguineo
            )
        VALUES ({valores});""".replace('\n', '')
        insert_query.append(sql)
    # logging.debug(insert_query[0])
    return insert_query


def exec_query(list_querys_string=[], query_type=''):
    db_name = 'db'
    db_user = 'user'
    db_pass = 'password'
    db_host = 'database-service'
    db_port = '5432'

    try:
        db_string = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
        db = create_engine(db_string)

        if query_type == 'insert':
            for query in list_querys_string:
                db.execute(query)
        elif query_type == 'select':
            for query in list_querys_string:
                result = db.execute(query).fetchall()
                return json.dumps([dict(row) for row in result])
        elif query_type == 'delete':
            for query in list_querys_string:
                db.execute(query)
        return {'message': "Proceso ejecutado correctamente"}

    except Exception as e:
        logging.debug(e)


@app.route('/insert')
def insert_perfil():
    try:
        exec_query(FakerRandom(), "insert")
        return {'message': f"Exito al crear registros"}
    except Exception as e:
        logging.debug(e)
        return {'message': "Error al crear registros"}


@app.route('/select')
def select_perfil():
    query = 'SELECT * FROM perfil'
    try:
        data = json.loads(exec_query([query], "select"))
        return json.dumps(data)
    except Exception as e:
        logging.debug(e)
        return {'message': "Error en select"}


@app.route('/delete')
def delete_perfil():
    query = 'DELETE FROM perfil'
    try:
        exec_query([query], "delete")
        return {'message': "Exito en delete"}
    except Exception as e:
        logging.debug(e)
        return {'message': "Error en delete"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
