import http.server
import socketserver
import json
import termcolor
from pathlib import Path


def species_get(endpoint):
    PORT = 8080
    SERVER = "rest.ensembl.org"
    print(f"\nConnecting to server: {SERVER}:{PORT}\n")
    connection = http.client.HTTPConnection(SERVER)
    try:
        connection.request("GET", endpoint)
    except ConnectionRefusedError:
        print("ERROR! The database is down")
        exit()
    response = connection.getresponse()
    print(f"Response received!: {response.status} {response.reason}\n")
    data = response.read().decode("utf-8")
    data_1 = json.loads(data)
    return data_1

PORT = 8080
PARAMS = "?content-type=application/json"
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        req_line = self.requestline.split(' ')
        path = req_line[1]
        arguments = path.split('?')
        first_argument = arguments[0]
        if first_argument == "/":
            contents = Path('index.html').read_text()
            error_code = 200
        elif first_argument == "/listSpecies":
            ENDPOINT = "info/species"
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
            elif int(third_argument) < 0 or int(third_argument) > len(species):
                contents = Path('Error.html').read_text()
                error_code = 404
            else:
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
                            <p>Limit of species selected: {third_argument}</p>
                            <p>Name(s) of the species:</p>
                            </body>
                            </html>
                            """
                error_code = 200
                for name in species[:int(third_argument)]:
                    contents += f"""<p>- {name["common_name"]}<p>"""

        else:
            contents = Path('Error.html').read_text()
            error_code = 404

        self.send_response(error_code)
        self.send_header('Content-Type', "text/html")
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))
        return


Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()