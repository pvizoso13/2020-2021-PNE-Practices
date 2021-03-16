from pathlib import Path

FILENAME = "U5.txt"

file_contents = Path(FILENAME).read_text()

index_start = file_contents.find("\n")
seq_dna = file_contents[index_start+1:]
print("Body of the U5.txt file: ")
print(seq_dna)
