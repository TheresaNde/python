# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from fileinput import filename
from typing import Text


def read_file_content(filename):
    # [assignment] Add your code here 
     with open(filename) as f:
         return f.read()
        # for line in f:
           #print(line)

#read_file_content("Reading-Text-Files\story.txt")

def count_words(read_file_content):
    text = read_file_content ("Reading-Text-Files\story.txt")
      #read_file_content = open("Reading-Text-Files\story.txt", "r")
    #assignment] Add your code here
    sorer=dict()
    list_of_lines= text.split("\n")
    for line in list_of_lines:
    #text = open ("Reading-Text-Files\story.txt", "r")
       #sorer=dict()
       line = line.strip()
       line = line.lower()
       words = line.split(" ")

       for word in words:
        # Check if the word is already in dictionary
        if word in sorer:
            # Increment count of word by 1
            sorer[word] = sorer[word] + 1
        else:
            # Add the word to dictionary with count 1
             sorer[word] = 1
        return sorer #{"as": 10, "would": 20}
#print(count_words(read_file_content))
print(count_words(read_file_content))
    #return {"as": 10, "would": 20}