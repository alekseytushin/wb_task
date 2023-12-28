import sqlite3

import json

from .utils import modify_response


@modify_response
def get_many_records(req):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM records')
    records = cursor.fetchall()
    connection.close()

    return json.dumps({
        'data': [
            {"id": record[0], "body": record[1]} for record in records
        ],
        'success': True
    })