import http.client
import json
import termcolor
from pathlib import Path


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
            species = species_get(ENDPOINT+PARAMS)["species"]
            if len(arguments) > 1:
                second_argument = arguments[1]
                third_argument = second_argument.split('=')[1]
            else:
                third_argument = ""
            if third_argument == "":
                contents = f"""
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                          <title> List of species </title >
                        </head >
                        <body>
                        <body style="background-color: LimeGreen">
                        <p>Total number of species: {len(species)}</p>
                        <p>Limit of species selected: {len(species)}</p>
                        <p>Name(s) of the species:</p>
                        </body>
                        </html>
                        """
                error_code = 200
                for name in species:
                    contents += f"""<p>- {name["common_name"]}<p>"""
                contents += f"""<a href="/">Main page</a>"""
            elif third_argument
