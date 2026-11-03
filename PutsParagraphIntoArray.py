def ReadFromFile(filename):
        
    strip = "\n"
    with open(filename) as readfile:
        everything = readfile.read()
        paragraphs = everything.split(strip)
            
    return paragraphs
    
paragraphs=ReadFromFile("Assets/paragraph_list.txt")
print(paragraphs)
for loop in range(len(paragraphs)):
    print(paragraphs[loop])
    print("")

split=" "
for loop in range(len(paragraphs)):
    words=paragraphs[loop].split(split)
    print(words)


