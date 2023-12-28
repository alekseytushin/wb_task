import sqlite3

import json

from .utils import modify_response


@modify_response
def add_record(req):
    print(req)
    assert 'id' in req.query, 'id must be in request query'
    assert 'body' in req.query, 'body must be in request query'

    record_id = req.query['id'][0]
    body = req.query['body'][0]

    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Создаем таблицу Users
    cursor.execute(f'''INSERT INTO records(id, body) VALUES ({record_id}, '{body}')''')

    connection.commit()
    connection.close()

    return json.dumps({ 'success': True })
