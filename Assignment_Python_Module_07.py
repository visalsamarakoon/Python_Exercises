# Question 01

seasons = ("Spring", "Summer", "Autumn", "Winter")

month = int(input("Enter a no of a month: "))
if month == 12 or month == 1 or month == 2:
    print(f"It is {seasons[3]}")
elif month == 3 or month == 4 or month == 5:
    print(f"It is {seasons[0]}")
elif month == 6 or month == 7 or month == 8:
    print(f"It is {seasons[1]}")
elif month == 9 or month == 10 or month == 11:
    print(f"It is {seasons[2]}")
else:
    print("Enter a valid no of a month")


# Question 02
names = {}

while True:
    add_names = input("Enter a name: ")
    for i in names:
        if add_names == '':
            break
        elif add_names == i:
            print("Existing name")
        else:
            print("New name")
            names.add(add_names)



print(names)