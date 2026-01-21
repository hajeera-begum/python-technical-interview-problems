word = input("Enter word: ")

i = 0
while i < len(word) // 2:
    if word[i] != word[len(word) - 1 - i]:   #Eg: MADAM word[0]!=word[4]- False ; word[1]!=word[3]0 False  ; word[2]<2 fasle --Out of the while loop
        print("Not palindrome")              #Eg:HELLO word[0]!=word[4] - True ---Not palindrome
        break
    i = i + 1
else:
    print("Palindrome")
