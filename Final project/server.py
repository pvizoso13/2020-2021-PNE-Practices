import http.client
import json

def species_get(endpoint):
    PORT = 8080
    SERVER = "rest.ensembl.org"
    print(f"\nConnecting to server: {SERVER}:{PORT}\n")
    connection = http.client.HTTPConnection(SERVER)
    try:
        connection.request("GET", ENDPOINT + PARAMS)
    except ConnectionRefusedError:
        print("ERROR! The database is down")
        exit()
    response = connection.getresponse()
    print(f"Response received!: {response.status} {response.reason}\n")
    data = response.read().decode("utf-8")
    data_1 = json.loads(data)
    return data_1

SERVER = "rest.ensembl.org"
PARAMS = "?content-type=application/json"



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
        elif first_argument == "/listSpecies":
            ENDPOINT = "/info/species"
            species =