import requests

BASE_URL = 'http://127.0.0.1:8080/'


def main():
    assert {"data": [], "success": True} == requests.get(f'{BASE_URL}get_many_records').json()
    assert {"success": True} == requests.put(f'{BASE_URL}add_record?id=1&body=test').json()
    assert {"data": [{"id": 1, "body": "test"}], "success": True} == requests.get(f'{BASE_URL}get_many_records').json()
    assert {"data": [{"id": 1, "body": "test"}], "success": True} == requests.get(f'{BASE_URL}get_record?id=1').json()


if __name__ == '__main__':
    main()