word = input("Enter word: ")

i = 0
while i < len(word) // 2:
    if word[i] != word[len(word) - 1 - i]:
        print("Not palindrome")
        break
    i = i + 1
else:
    print("Palindrome")
