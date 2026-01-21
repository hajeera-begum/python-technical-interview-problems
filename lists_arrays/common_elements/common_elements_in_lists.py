a = [10, 5, 20, 8,15,10, 8]
b = [10, 15, 20, 18,15,10, 80]

print(list(set(a) & set(b)))
print(list(set(a).intersection(b)))
[print(item) for item in a if item in b]
