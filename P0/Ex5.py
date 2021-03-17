from P0.Seq0 import *

filename = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
bases = ["A", "C", "T", "G"]
FOLDER = "../Session-04/"
for gene_file in filename:
    print("Gene", gene_file, ":", seq_count(FOLDER+gene_file))
