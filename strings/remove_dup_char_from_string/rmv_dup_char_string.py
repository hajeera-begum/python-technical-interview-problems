word="Hajeeera"
count={}
for char in word:
    if char in count:
        count[char]+=1
    else: 
        count[char]=1
print(count)
result=[]
for i in count:
    result.append(i)
    #print(i)

 
print(result)
string="".join(result)
print(string)
