# Problem 1
numbers = input("Enter two or more numbers separated by spaces: ")
numbers = numbers.split(" ")

if len(numbers) >= 2:
    x = [float(i) for i in numbers]
    total = sum(x)
    print(total)

else:
    print("You did not enter two or more numbers separated by spaces!")