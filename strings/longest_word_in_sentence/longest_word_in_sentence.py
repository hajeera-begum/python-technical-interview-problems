sentence = "The quick brown fox jumps over the lazy dog"

words_list = sentence.split()

longest = ""

for word in words_list:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)
