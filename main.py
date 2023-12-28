from routes import make_routes
from server.server import Server


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080

    serv = Server(host, port, make_routes())
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass