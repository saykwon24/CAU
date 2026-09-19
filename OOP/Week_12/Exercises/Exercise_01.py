def main():
    # Take a file name from user input
    file_name = input("Enter filename (default: nurseryrhyme.txt): ")
    if len(file_name) == 0: file_name = "nurseryrhyme.txt"
    
    file = open(file_name, "r")
    words = set()
    for line in file:
        the_words = line.split()
        for word in the_words:
            if word != "": words.add(clean_str(word))
    file.close()
    
    # Display the output
    print("The document contains %d unique words." % len(words))


## Cleans a string by making letters lowercase and removing characters that are not letters.
# @param string the string to be cleaned
# @return the cleaned string
#
def clean_str(string):
    result = ""
    for char in string:
        if char.isalpha(): result += char.lower()
    return result


main()