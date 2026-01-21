"""
Problem: Find the minimum and maximum elements in a list without using builtin function
"""
numbers_list = [13, 453, 45, 67, 45, 56]

min_val = numbers_list[0]
max_val = numbers_list[0]

for num in numbers_list:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Max:", max_val)
print("Min:", min_val)
