#Fibonacci series:
n = int(input("Enter number of terms: "))

a=0
b=1

for i in range(n):
    print(a, end=" ")
    #a, b = b, a + b
    temp = a + b
    a = b
    b = temp

#Output: Enter number of terms: 5
# 0 1 1 2 3 
