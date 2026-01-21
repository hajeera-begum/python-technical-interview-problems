'''
  Reverse a string without built in function
'''

alphabet_list=['l','o','v','e']
length=len(alphabet_list)
reverse_string=[] #To store appended reverse string
i=length-1
while i>=0:
    reverse_string.append(alphabet[i])
    i-=1
print(reverse_string)
