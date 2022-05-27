# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    #word= input("Enter first word here: ")
    #anagram= input("Enter first word here: ")
    if sorted(word) == sorted(anagram): #and len(word1)==len(word2)
      print("This is an anagram")
      
    else: print("This is not an anagram")
word= input("Enter first word here: ")
anagram= input("Enter second word here: ")

find_anagram(word, anagram)