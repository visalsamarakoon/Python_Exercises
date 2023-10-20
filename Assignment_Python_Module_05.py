# 05. List structures and iterative loops

# Question 01
import random
result = []
dice = int(input("How many dice do you want to roll?: "))
for i in range(dice):
    roll = random.randint(1, 6)
    result.append(roll)
total = sum(result)
print(f"Sum of the results of {dice} rolls is: {total}")

# Question 02
store = []
while True:
    user = input("Enter a number or press enter to quit: ")
    if user == "":
        break
    try:
        float_user = float(user)
        store.append(float_user)

    except ValueError:
        print("Value Error!")
store.sort(reverse=True)
print(f"The numbers in descending order are :  {store[:5]}")

store = []
for element in range(1, 6):
    while True:
        user = input("Enter a number or press enter to quit: ")
        if user == "":
            break
        try:
            float_user = float(user)
            store.append(float_user)
        except ValueError:
            print("Value Error!")
store.sort(reverse=True)
print(f"Descending order is: {store[:5]}")


# Question 03
number = int(input('Enter a number: '))
count = 0
for i in range(1, number + 1):
    if number % i == 0:
        count = count + 1

if count == 2:
    print('It is a prime no')
else:
    print('It is not a prime no')


# Question 04
city = []
for i in range(5):
    cities = input('Enter a city: ')
    city.append(cities)

for x in range(5):
    print(city[x])



