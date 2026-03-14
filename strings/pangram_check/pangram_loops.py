import string
a_to_z_list = list(string.ascii_lowercase)

string='The quick brown fox jumps over the lazy dog'
#string=input("Enter the String: ").lower()
for letter in a_to_z_list:
    if letter not in string:
        print("Not Pangarm")
        break
else:
    print("Pangram")
