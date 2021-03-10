def fibosum(n):
    addition = 0
    a = 0  # first element series
    b = 1  # second element series
    if n < 0:
        return "Incorrect format!"
    elif n == 1:
        return a
    elif n == 2:
        return a + b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
            addition = addition + b
        return addition


print("Sum of the First 5 terms of the Fibonacci terms: ", fibosum(5))
print("Sum of the First 10 terms of the Fibonacci terms: ", fibosum(10))
