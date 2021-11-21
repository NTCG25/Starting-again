timestable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
 
def func(z):
     return z*z

#print(list(map(func, li)))

#print([func(z) for z in timestable])

print([func(z) for z in timestable if z%2==0])  #-- Divisible by 2