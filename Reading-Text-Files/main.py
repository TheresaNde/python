def read_file_content(filename):
    # [assignment] Add your code here 
     with open(".\Reading-Text-Files\story.txt","r") as openfile:
             read_file = openfile.read()
             return read_file
       

def count_words():
    text=read_file_content(".\Reading-Text-Files\story.txt")
    list_of_lines= text.split()
    sorer={}
    for i in list_of_lines:
        if i in sorer:
            # Increment count of word by 1
           sorer[i] += 1
        else:
            # Add the word to dictionary with count 1
            sorer[i] = 1
    return sorer 
print(count_words())
count_words()
