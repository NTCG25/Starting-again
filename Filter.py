def add9(x):
    return x+9

def isOdd(x):
    return x%2 != 0

def isEven(x):
    return x%2 == 0

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

b = list(filter(isEven, a))

c = list(map(add9, a))

print(b)

print(c)
