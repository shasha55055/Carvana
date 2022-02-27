import sys

#main function to execute in comman line
def main1(): 
    function = sys.argv[1]
    if function == "show_most_three":
        for i in range(2, len(sys.argv)):
            mostThree(sys.argv[i])
            print("\n")
    else:
        print("function does not exist")
        
#main function to execute fo stdin
def main2(): 
    files_in = input("Enter selected files: ")
    files = files_in.split(", ")
    for file in files:
        mostThree(file)

# strings all submethods together
def mostThree(filename): 
    print("List of most common 3 word sequences in " + filename)
    text = getText(filename)
    formattedText = formatText(text)
    hashmap = makeHash(formattedText)
    hashmap2 = makeHash2(hashmap)
    result = mostCommonSequence(hashmap, hashmap2)
    for threeWords in result:
        print(threeWords)
    return(result)

# reads text in txt file
def getText(filename): 
    file = open(filename,"r")
    text = file.read()
    file.close()
    return(text)

# formats text to remove upper case, punctuation, tabs, and empty lines
# parses formatted text into a list of individual words
def formatText(text): #formats all text for parsing
    punc = '''!()-[]{;}:'"\,<>./\n?@#$%^&*_~'''
    for char in text:
        if char in punc:
            if char == "\n":
                text = text.replace(char, " ")
            else:
                text = text.replace(char, "")
    result = text.lower().split(" ")
    while("" in result):
        result.remove("")   
    return(result)

# creates a dictionary of every 3 word sequence and number of instances
def makeHash(arrText): 
    hashmap = {}
    for i in range(len(arrText)):
        if(i + 2 < len(arrText)):
            look = arrText[i] + " " + arrText[i + 1] + " " + arrText[i + 2]
        else:
            look = ""
        
        if look not in hashmap:
            hashmap[look] = 1
        else:
            hashmap[look] += 1

    return(hashmap)

# creates dictionary of number of instances and a list of three word sequences
# matches three word sequences to the number representing their number of instances
def makeHash2(hashmap): # creates a hashmap of number of instances and a string array of 3 word combos
    hashmap2 = {}
    for key, value in hashmap.items():
        if key == "":
            pass
        elif value not in hashmap2:
            hashmap2[value] = [key]
        else:
            hashmap2[value].append(key)
       
    return(hashmap2)

# creates a list of every three word sequence ordered from most common to least common
def mostCommonSequence(hashmap, hashmap2): 
    num_arr = []
    for key in hashmap2:
        num_arr.append(key)
    num_arr.sort()
    num_arr = num_arr[::-1]
    
    final_size = 0
    if len(hashmap) > 100:
        final_size = 100
    else:
        final_size = len(hashmap)

    final_arr = []
    for key in num_arr:
        for string in hashmap2[key]:
            final_arr.append(string + " - " + str(key))
    final_arr = final_arr[0:final_size]

    return(final_arr)

# main function that allows for either stdin or command line prompts
if (__name__ == "__main__"):
    try:
        main1()
    except:
        main2()
