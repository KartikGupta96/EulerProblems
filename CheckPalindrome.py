#Checks if a string is a palindrome.

import sys

def main():
    palindrome = raw_input("Enter a word: ")
    palindrome = palindrome.replace(" ", "")
    reversedWord = reverseWord(palindrome)
    if (palindrome == reversedWord):
        print "This is a palindrome"
    else:
        print "This is not a palindrome"

def reverseWord(word):
    new_string = ""
    index = len(word)
    while (index):
        index -=1
        new_string += word[index]
    return new_string

if __name__ == "__main__":
    main()