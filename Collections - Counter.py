from collections import Counter

c = Counter(a=5, b=10, c=14, d=1)
d = Counter(["a","a","a","b","b","b","b","b","c","c","c","c","d"])

print(c+d)

print(c-d)

print(c & d) # Intersection

print(c | d) # Union

