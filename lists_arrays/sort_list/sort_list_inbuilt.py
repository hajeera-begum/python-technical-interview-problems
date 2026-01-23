number=input("Please enter the numbers with space separation: ")

#Convert to list with comma/space separation
#num=number.split(',') #Comma separation
num=number.split() #Space separation
#print(num)
sort=sorted(num)
print(sort)

if num==sort:
    print("List is sorted")
else:
    print("List is not sorted")
