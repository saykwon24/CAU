def main():
    # Create a dictionary for abbreviation-translation pairs
    transMap = buildMapping("textabbrv.txt")
    
    # Take a message to be translated
    message = input("Enter a message to be translated: ").strip().split()
    
    # Translate the abbreviative message
    translation = ""
    for abbrv in message:
        translation = translation + translateAbbrv(transMap, abbrv) + " "
    
    # Print the output
    print("The translated text is:")
    print(translation.rstrip())



## Extracts abbreviations and their corresponding English phrases from a file and builds a translation mapping.
# @param filename name of the file containing the translations
# @return a dictionary associating abbreviations with phrases
#
def buildMapping(filename):
    transMap = {}
    file = open(filename, "r")
    for line in file:
        abbrv, trans = line.rstrip().split(":")
        transMap[abbrv] = trans
    file.close()
    
    return transMap



## Translates a single abbreviation using the translation map. If the abbreviation ends with a punctuation mark, it remains part of the translation.
# @param transMap a dictionary containing the common translations
# @param abbrv a string that contains the abbreviation to be translated
# @return the word or phrase corresponding to the abbreviation. If the abbreviation cannot be translated, it is returned unchanged
#
def translateAbbrv(transMap, abbrv):
    # Determine if the word ends with punctuation marks (Assume there is no punctuations in abbrv except at the end)
    abbrv_without_punct = ""
    punctuations = ""
    for char in abbrv:
        if char in ".?!,;:": punctuations += char
        else: abbrv_without_punct += char
    
    # Translate the abbrv
    if abbrv_without_punct in transMap: word = transMap[abbrv_without_punct]
    else: word = abbrv_without_punct
    
    return word + punctuations



main()