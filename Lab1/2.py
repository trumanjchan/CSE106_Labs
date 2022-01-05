# Problem 2
sentence = input("Enter a sentence: ")
number = input("Enter the number of times to repeat: ")

file_object = open("CompletedPunishment.txt", "w")
file_object.write( (sentence + "\n") * int(number) )

file_object.close()