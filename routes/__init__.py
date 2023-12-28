from .add_record import add_record
from .get_many_records import get_many_records
from .get_record import get_record


def make_routes():
    return {
        ('/add_record', 'PUT'): add_record,
        ('/get_many_records', 'GET'): get_many_records,
        ('/get_record', 'GET'): get_record,
    }