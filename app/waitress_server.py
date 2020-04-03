import sys
from app.webapp import app
from waitress import serve
import hupper


def main(args=sys.argv[1:]):
    if '--reload' in args:
        reloader = hupper.start_reloader('app.waitress_server.main')
        reloader.watch_files(['foo.ini'])

    serve(app, host='0.0.0.0', port=5000)
