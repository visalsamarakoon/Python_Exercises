# 04. While loops (while)

# Question 01
num = 1
while num <= 1000:
    num = num + 1
    if num % 3 == 0:
        print(num)

# Question 02
inches = float(input("Enter inches: "))
while inches > 0:
    centimeters = inches * 2.54
    print(centimeters)
    inches = int(input("Enter inches: "))
print("Enter a positive number!")

# Question 03
smallest = None
largest = None
while True:
    number = input("Enter a number or press enter to quit: ")
    if number == "":
        break
    try:
        float_number = float(number)
    except ValueError:
        print("Invalid input. Enter a valid number: ")
        continue
    if smallest is None or float_number < smallest:
        smallest = float_number
    if largest is None or float_number > largest:
        largest = float_number
if smallest is not None and largest is not None:
    print(f"The smallest number is: {smallest}")
    print(f"The largest number is: {largest}")
else:
    print("No valid numbers were entered.")

# Question 04
import random
combination = random.randint(1, 10)
number = int(input("Enter a number between 1 and 10: "))
while number != combination:
    if number < combination:
        print("Too low")
    else:
        print("Too high")
    number = int(input("Enter a number from 1 and 7: "))
print("Correct")

# Question 05
username = input("Enter username: ")
password = input("Enter password: ")
attempt = 1
while attempt < 5:
    if username == "python" and password == "rules":
        print("Welcome")
        break
    else:
        print("The username or password is incorrect")
        username = input("Enter username again: ")
        password = input("Enter password again: ")
        attempt = attempt + 1
else:
    print("Access Denied")

# Question 06
import random
points = float(input("Enter the number of points you want to generate: "))
circle_points = 0
square_points = 0
for i in range(int(points ** 2)):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    circle = x ** 2 + y ** 2
    if circle <= 1:
        circle_points = circle_points + 1
    square_points = square_points + 1
pi = 4 * circle_points / square_points
print(f"Pi value is: {pi}")
