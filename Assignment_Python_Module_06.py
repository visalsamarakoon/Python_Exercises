# 06. Functions
# Question 01

import random


def dice():
    a = 0
    while a != 6:
        a = random.randint(1,6)
        print(a)
    else:
        print("It's 6")

dice()

# Question 02

def modified_dice(sides):
    x = 0
    while x != sides:
        x = random.randint(1, sides)
        print(x)
    else:
        print(f"It's {sides}")


modified_dice(50)

# Question 03

def conversion(american_gallons):
    while True:
        if american_gallons > 0:
            liters = american_gallons * 3.78541
            print(f"It's {liters} liters")
            american_gallons = int(input("Enter volume in american gallons: "))
        else:
            print("Entered negative value")
            break


value = int(input("Enter volume in american gallons: "))

conversion(value)


# Question 04

def total(no):
    list_int = []
    total_int = 0
    for elements in no.split():
        list_int.append(elements)
        elements_int = int(elements)
        total_int = elements_int + total_int
    print(f"Here is the list: {list_int}")
    print(f"Total is {total_int}")

num = input("Enter a list of numbers with spaces between each: ")

total(num)


# Question 05


def uneven(no):
    list_all = []
    even_list = []
    for all_no in no.split():
        list_all.append(all_no)
    print(f"All list: {list_all}")

    for even in no.split():
        even_int = int(even)
        if even_int % 2 == 0:
            even_list.append(even)
    print(f"Even list: {even_list}")

user_input = input("Enter a no: ")
uneven(user_input)


# Question 06

def lowest_pizza(diameter, price):
    pizza_price_list = []
    pizza_diameter_list = []
    for d in diameter.split():

        d_float_meters = float(d) * 0.01  #used 0.01 to convert cm to m
        pizza_diameter_list.append(d_float_meters)

    for p in price.split():
        p_float = float(p)
        pizza_price_list.append(p_float)

    pizza_1_unit_price = pizza_price_list[0]/(math.pi * (pizza_diameter_list[0]/2)**2)
    pizza_2_unit_price = pizza_price_list[1]/(math.pi * (pizza_diameter_list[1]/2)**2)

    print(f"pizza 1 : {pizza_1_unit_price:.2f}")
    print(f"pizza 2 : {pizza_2_unit_price:.2f}")

    if pizza_1_unit_price > pizza_2_unit_price:
        print(f"Pizza two has lower unit price. Buy pizza two")
    else:
        print(f"Pizza one has lower unit price. Buy pizza one")


pizza_diameter = input("Enter the diameter of pizza: ")
pizza_price = input("Enter the price of pizza: ")
lowest_pizza(pizza_diameter, pizza_price)