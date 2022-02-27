import sys

def main1():
    function = sys.argv[1]
    if function == "show_most_three":
        for i in range(2, len(sys.argv)):
            mostThree(sys.argv[i])
            print("\n")
    else:
        print("function does not exist")

def main2():
    files_in = input("Enter selected files: ")
    files = files_in.split(", ")
    for file in files:
        mostThree(file)


def mostThree(filename): # strings all functions together
    print("List of most common 3 word sequences in " + filename)
    text = getText(filename)
    formattedText = formatText(text)
    hashmap = makeHash(formattedText)
    hashmap2 = makeHash2(hashmap)
    result = mostCommonSequence(hashmap, hashmap2)
    for threeWords in result:
        print(threeWords)
    return(result)

def getText(filename): #reads text in file
    file = open(filename,"r")
    text = file.read()
    file.close()
    return(text)

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

def makeHash(arrText): # creates a hashmap of every 3 word combo and their instances
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

def mostCommonSequence(hashmap, hashmap2): # creates and array of every 3 word combo ordered from most to least instances 
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


if (__name__ == "__main__"):
    try:
        main1()
    except:
        main2()