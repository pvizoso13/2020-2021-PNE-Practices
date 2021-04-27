import http.server
import socketserver
import termcolor
import pathlib


def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')
        # IN this simple server version:
        # We are NOT processing the client's request
        if self.path == "/" or self.path == "/index.html":
            contents = read_html_file("./html/index.html")
        elif self.path == "/info/A" or self.path == "/info/A.html":
            contents = read_html_file("./html/info/A.html")
        elif self.path == "/info/C" or self.path == "/info/C.html":
            contents = read_html_file("./html/info/C.html")
        elif self.path == "/info/T" or self.path == "/info/T.html":
            contents = read_html_file("./html/info/T.html")
        elif self.path == "/info/G" or self.path == "/info/G.html":
            contents = read_html_file("./html/info/G.html")
        else:
            contents = read_html_file('./html/Error.html')


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()