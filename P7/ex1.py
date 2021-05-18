import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print(f"Server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(SERVER)
try:
    conn.request("GET", ENDPOINT + PARAMS)
except ConnectionRefusedError:
    print("ERROR! The database is down")
    exit()

r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")
# answer decoded (22) and json format (23)
data1 = r1.read().decode()
response = json.loads(data1)
ping = response["ping"]
if ping == 1:
    print("PING OK!!! The database is running")
