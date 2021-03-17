from P0.Seq0 import *
filename = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
FOLDER = "../Session-04/"
for gene_file in filename:
    print("Gene ", gene_file, "---> Length: ", seq_len(FOLDER+gene_file))
