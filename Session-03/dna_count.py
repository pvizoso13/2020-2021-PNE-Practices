dna = input("Enter the dna chain you want to analyze: ")
count_a = 0
count_c = 0
count_t = 0
count_g = 0
for base in dna:
    if base == "A":
        count_a += 1
    elif base == "C":
        count_c += 1
    elif base == "T":
        count_t += 1
    elif base == "G":
        count_g += 1

print("Total length: ", len(dna))
print("A: ", count_a)
print("C: ", count_c)
print("T: ", count_t)
print("G: ", count_g)
