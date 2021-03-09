def fibon(n):
    a = 0
    b = 1
    if n < 0:
        return "Incorrect input!"
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


print("5th Fibonacci term: ", fibon(5))
print("10th Fibonacci term: ", fibon(10))
print("15th Fibonacci term: ", fibon(15))
