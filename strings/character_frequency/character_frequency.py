"""
Program to count the frequency of characters in a string.
"""
word=input("Give your string please: ").lower()
count={}
for char in word:
    if char in count:
        count[char]+=1
    else:
        count[char]=1
print(f"\n{count}\n")
