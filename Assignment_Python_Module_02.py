# 02. Variables and interactive programs

# Question 01
name = input("Enter you name: ")
print(f"Hello, {name}!")

# Question 02
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"The area of the circle is: {area}")

# Question 03
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = (length * 2) + (width * 2)
area = length * width
print(f"The perimeter of rectangle is: {perimeter}")
print(f"The area of rectangle is: {area}")

# Question 04
first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))
third = int(input("Enter the third integer: "))
total = (first + second + third)
product = (first * second * third)
average = (first + second + third)/3
print(f"The sum, product and average of your numbers are: \nSum = {total}\nProduct = {product}\nAverage = {average}")

# Question 05
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
grams = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)
print(f"The weight in modern units:\n{int(grams // 1000)} kilograms and {grams % 1000:.2f}")

# Question 06 Part 01
import random
number_1 = random.randint(0,9)
number_2 = random.randint(0,9)
number_3 = random.randint(0,9)
print(f"Your 3-digit code is: {number_1}{number_2}{number_3}")

# Question 06 Part 02
import random
number_1 = random.randint(1,6)
number_2 = random.randint(1,6)
number_3 = random.randint(1,6)
number_4 = random.randint(1,6)
print(f"Your 4-digit code is: {number_1}{number_2}{number_3}{number_4}")