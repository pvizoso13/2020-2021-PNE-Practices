n = 11
a = 0
b = 1

print(a, b, end=' ')
for i in range(2, n):
    c = a + b
    a = b
    b = c
    print(b, end=' ')
