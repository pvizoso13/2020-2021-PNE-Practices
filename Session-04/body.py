from pathlib import Path

FILENAME = "RNU6_269P.txt"

file_contents = Path(FILENAME).read_text()

index_start = file_contents.find("\n")
seq_dna = file_contents[index_start+1:]
print(seq_dna)
