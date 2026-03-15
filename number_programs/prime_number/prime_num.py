#Prime Numbers : 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, and 97
n=int(input("Enter the number: "))

if n<=1:
    print("Not prime")
else:
    for i in range(2,n): #Eg: n=10, 10%2==0--> Not prime
        if n%i==0:
            print("Not prime")
            break
    else:                        #for else block. Here else block runs if break doesnt happen in the above 'if' loop
            print("Prime ")
      
