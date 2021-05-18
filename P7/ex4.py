import http.client
import termcolor
import json
from Seq1 import Seq

GENES = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362',
}

BASES = ["A", "C", "T", "G"]

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"
PARAMS = "?content-type=application/json"
name = input("Write the name of the gene: ")
REQ = ENDPOINT + GENES[name] + PARAMS
URL = SERVER + REQ

print(f"Server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(SERVER)
try:
    conn.request("GET", REQ)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the server")
    exit()

r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")
data1 = r1.read().decode()
gene = json.loads(data1)

termcolor.cprint("Gene", "blue", end="")
print(f"Gene: {name}")
termcolor.cprint("Description", "blue", end="")
print(f"Description: {gene['desc']}")

gene_str = gene['seq']
s = Seq(gene_str)

length = s.len()
termcolor.cprint("Total length", "blue", end="")
print(f": {length}")
# count_base function defined in P1 Seq1 class Seq
for e in BASES:
    count = s.count_base(e)
    percentage = round(s.count_base(e) * (100 / s.len()), 2)
    termcolor.cprint(f"{e}", "green", end="")
    print(f": {count} {percentage}%")

dictionary = s.count()
list_values = list(dictionary.values())
max_base = max(list_values)

termcolor.cprint("Most frequent Base", "blue", end="")
print(f":{BASES[list_values.index(max_base)]}")