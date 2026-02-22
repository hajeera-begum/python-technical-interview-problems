string1=input("Enter your first string: ").lower()
string2=input("Enter your second string: ").lower()

if sorted(string1)==sorted(string2):  #sorted() function creates a new list containing all items from any iterable 
                                      #(list, tuple, string, set, or dictionary) in ascending order by default, leaving the original iterable unchanged.
  print("Anagram")
else:
    print("Not an Anagram")
