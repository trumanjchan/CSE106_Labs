# Problem 3
x = input("Enter a word: ")

file_object = open('PythonSummary.txt', 'r')
data = file_object.read()

data = data.replace("-", " ")     # didn't work in for loop: wordlist[i] = wordlist[i].replace("-", " ")
wordlist = data.split()
# print(wordlist)

for i in range( len(wordlist) ):
    wordlist[i] = wordlist[i].lower()
    wordlist[i] = wordlist[i].replace(".", "")
    wordlist[i] = wordlist[i].replace("!", "")
    wordlist[i] = wordlist[i].replace("?", "")

# print(wordlist)

print("The word " + x + " occurs " + str( wordlist.count(x.lower()) ) + " times.")

file_object.close()