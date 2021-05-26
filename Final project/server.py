import http.client
import json

SERVER = "rest.ensembl.org"
PARAMS = "?content-type=application/json"

connection = http.client.HTTPConnection(SERVER)


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        req_line = self.requestline.split(' ')
        path = req_line[1]
        arguments = path.split('?')
        first_argument = arguments[0]
        if first_argument == "/":
            contents = Path('form-4.html').read_text()
            error_code = 200

