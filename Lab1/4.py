# Problem 4
with open('classesInput.txt', 'r+') as classesInput:
    file_input = classesInput.read().split('\n')

# print(file_input)

class Template:
    def __init__(self, num, department, courseNum, courseName, cred, days, start, end, avrg):
        self.num = num
        self.department = department
        self.courseNum = courseNum
        self.courseName = courseName
        self.cred = cred
        self.days = days
        self.start = start
        self.end = end
        self.avrg = avrg

    def print_info(self):
        file_object2 = open("ClassSchedule.txt", "a")

        file_object2.write("COURSE %s: %s%s: %s\n" % (self.num, self.department, self.courseNum, self.courseName) )
        file_object2.write("Number of Credits: %s\n" % self.cred)
        file_object2.write("Days of Lectures: %s\n" % self.days)
        file_object2.write("Lecture Time: %s - %s\n" % (self.start, self.end) )
        file_object2.write("Stat: on average, students get {}% in this course\n".format(self.avrg))
        file_object2.write("\n")

        file_object2.close()

# test = Template(1, "CSE", "030", "Data Structures", 4, "Monday, Wednesday", "4:30pm", "5:45pm", "85%")
# test.print_info()

with open('ClassSchedule.txt', 'w') as file_object1:
    file_object1.truncate()

numberofcourses = file_input[0]
for x in range(int(numberofcourses)):
    placeholder = Template(x + 1, file_input[(8*x)+1], file_input[(8*x)+2], file_input[(8*x)+3], file_input[(8*x)+4], file_input[(8*x)+5], file_input[(8*x)+6], file_input[(8*x)+7], file_input[(8*x)+8])
    placeholder.print_info()

# placeholder = Template(1, file_input[1], file_input[2], file_input[3], file_input[4], file_input[5], file_input[6], file_input[7], file_input[8])
# placeholder.print_info()