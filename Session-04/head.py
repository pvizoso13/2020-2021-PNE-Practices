from pathlib import Path

FILENAME = "RNU6_269P.txt"

file_contents = Path(FILENAME).read_text()

print("The first line of the RNU6_269P.txt file: ")
print(file_contents.split("\n")[0])
