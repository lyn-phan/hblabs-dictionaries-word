# put your code here.

# define funcation(file):
#    open file 
#    strip non-alpha characters and right hand indent (.rstrip)
#    make each word .lower()
#    count_of_word_in_file = {"word": number}
#    for loop that is iterating over words not characters:
#        define count_of_word_file =  get function + 1
#    return count_of_word_in_file 
#    close file
#     

def get_word_count(file_name):
    """return count for each word in file."""
    file = open(file_name)
    
    count_of_word_in_file = {}
    
    for line in file:
        line = line.lower()
        line = line.rstrip()
        line = line.split(" ")
        for item in line:
            item = item.rstrip(",").rstrip("?").rstrip(".")
        for word in line:
            count_of_word_in_file[word] = count_of_word_in_file.get(word, 0) + 1
        for word, count in count_of_word_in_file.items():
            print(word, count)

    
get_word_count("test.txt")

# Return a copy of the string with trailing characters removed. 
# The chars argument is a string specifying the set of characters to be removed. 
# If omitted or None, the chars argument defaults to removing whitespace. 
# The chars argument is not a suffix; rather, all combinations of its values are stripped:



