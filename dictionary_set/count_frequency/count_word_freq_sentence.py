#Count frequency  if words in a sentence

sentence="Hello to the python world. The take away is the python fundamentals"
split_sentence=sentence.lower().split()

count={}

for word in split_sentence:          # count.get(key, default)
    count[word]=count.get(word,0)+1  # count.get('hii', 0)   # returns 
                                     # count.get('is', 0)    # returns 0 (not present)

print(count)
