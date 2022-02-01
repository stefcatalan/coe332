# script to read the file and print its last 10 lines

words = []

with open('/usr/share/dict/words', 'r') as f:
    words = f.read().splitlines()

#finding list length
listLength = len(words)

# printing last 10 lines
for x in range(listLength - 10, listLength):
    print(words[x]) 

# printing words that start w "pyt"
for x in range(listLength):
    if(words[x].startswith("pyt")):
        print(words[x])
