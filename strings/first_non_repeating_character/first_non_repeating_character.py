"""
Find the first non-repeating character in a string.
"""

word=input("Give your string please: ").lower()
count={} #Creating empty dictionary to store key,value pairs of my word
for char in word: 
    if char in count:
        count[char]+=1
    else:
        count[char]=1
for char in word:
    if count[char] == 1:
        print("First non-repeating character:", char)
        break
else:
    print("No non-repeating character found")
