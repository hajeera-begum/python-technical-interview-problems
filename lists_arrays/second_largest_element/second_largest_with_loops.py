a = [10, 5, 20, 8,15]

largest = a[0]
second = a[0]

for num in a:
    if num>largest:
        largest=num

for num in a:
    if num!=largest and num>second:
        second=num
print("Second largest: ", second)
