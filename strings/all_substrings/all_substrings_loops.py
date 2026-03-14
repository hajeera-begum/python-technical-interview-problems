word='abcd'
all_substrings=[]
length=len(word)

for i in range(length):
    for j in range(i+1, length+1):  #Iteration 1: range(1,5) , So j value starts from 1
        all_substrings.append(word[i:j])
        
print(all_substrings)

#Output: ['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']
