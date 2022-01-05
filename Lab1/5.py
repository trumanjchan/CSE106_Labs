# Problem 5
import json

file_object = open('grades.txt', 'r+')
data = file_object.read()
grades = json.loads(data)
print(grades)

initialStep = input("1) Create\n2) View\n3) Edit\n4) Delete\nYou would like to: ")

if initialStep == "1":     # works
    w1 = input("Create Student Name (First Last): ")
    w2 = input("Create student's Grade (float): ")
    grades[w1] = float(w2)
    with open("grades.txt", "w") as outfile:
        json.dump(grades, outfile)

    print(grades)
elif initialStep == "2":     # works
    x = input("View whose grade (First Last): ")
    print(grades[x])

elif initialStep == "3":     # works
    y1 = input("Edit whose grade (First Last): ")
    y2 = input("Edit grade to (float): ")
    grades[y1] = float(y2)
    with open("grades.txt", "w") as outfile:
        json.dump(grades, outfile)

    print(grades)
elif initialStep == "4":     # potentially works
    z = input("Delete grade (First Last): ")
    grades.pop(z)
    with open("grades.txt", "w") as outfile:
        json.dump(grades, outfile)

    print(grades)

file_object.close()
