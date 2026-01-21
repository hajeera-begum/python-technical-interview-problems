target=6
num=[5,5,2,4,6,3,3]
pair=[]
for i in range(len(num)):
    for j in range(i+1, len(num)):
        #print("I:",num[i])
        #print("J:",num[j])
        if num[i]+num[j]==target:
            pair.append((num[i],num[j])) #Should put 2 brackets here for append to accept 2 arguments
            
print(pair)
