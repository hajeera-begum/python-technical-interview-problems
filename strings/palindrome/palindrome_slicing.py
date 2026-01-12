"""
Problem: Check whether a given string is a palindrome.
Approach: Slicing
Description:
- The string is reversed using Python slicing [::-1]
- The original string is compared with its reversed version

Time Complexity: O(n)
Space Complexity: O(n)
    Original string  → m a d a m
    Reversed string  → m a d a m   ← new copy created
Reversing the string using slicing takes O(n) time and O(n) space because a new reversed string is created.
The more characters in the string, the more time it takes to process it.
"""

def palindrome(text):
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("No")


print("Welcome to the Palindrome program")


def start():
    while True:
        text = input("Please enter the string: ")
        palindrome(text)

        play = input("Do you want to continue? Yes/No: ").lower()
        if play != "yes":
            print("Thank You for using this program")
            break


start()
