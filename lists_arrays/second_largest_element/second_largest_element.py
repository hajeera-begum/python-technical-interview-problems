"""
Problem: Find the second largest number in a list
Approach: Using sort function
Time Complexity: O(n log n)
Space Complexity: O(1)
"""
numbers_list = [13, 453, 45, 67, 45, 56]
numbers_list.sort()
print("Sorted list:", numbers_list)
print("Second largest number:", numbers_list[-2])
