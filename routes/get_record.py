import sqlite3

import json

from .utils import modify_response


@modify_response
def get_record(req):
    assert 'id' in req.query, 'id must be in request query'

    record_id = req.query['id'][0]
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute(f'SELECT * FROM records where id = {record_id} LIMIT 1')
    records = cursor.fetchall()
    connection.close()

    return json.dumps({
        'data': [
            {"id": record[0], "body": record[1]} for record in records
        ],
        'success': True
    })
