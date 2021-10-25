def echodeltabravo(j):
    return lambda a: a * j

mydoublernumber = echodeltabravo(4)
mytriplernumber = echodeltabravo(7)

print(mydoublernumber(1000000000))
print(mytriplernumber(1000000000))
