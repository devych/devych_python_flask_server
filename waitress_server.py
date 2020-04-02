import sys
from app import app
from waitress import serve
import hupper


def main(args=sys.argv[1:]):
    if '--reload' in args:
        reloader = hupper.start_reloader('waitress_server.main')

    serve(app, host='0.0.0.0', port=5000)


serve(app, host='0.0.0.0', port=5000)