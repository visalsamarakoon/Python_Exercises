# 02. Conditional Structures (if)

# Question 01
length = float(input("Enter length of the zander in centimeters: "))
gap = 42 - length
if length >= 42:
    print("Congratulations! The zander fulfils the size limit.")
else:
    print("Sorry, You are advised to release the fish back into the lake.\n"
          f"It is {gap}cm below the size limit. ")

# Question 02
cabin = input("Enter your cabin class: ")
if cabin == "LUX":
    print("upper-deck cabin with a balcony")
elif cabin == "A":
    print("above the car deck, equipped with a window")
elif cabin == "B":
    print("windowless cabin above the car deck")
elif cabin == "C":
    print("windowless cabin below the car deck")
else:
    print("Invalid cabin class")

# Question 03
gender = input("Enter your biological gender: ")
value = float(input("Enter your haemoglobin value in g/l: "))
if gender == "male" or gender == "Male":
    if value < 134:
        print("Low haemoglobin level")
    elif 134 <= value <= 167:
        print("Normal haemoglobin level")
    elif value > 167:
        print("High haemoglobin level")
    else:
        print("Invalid input!")
elif gender == "female" or gender == "Female":
    if value < 117:
        print("Low haemoglobin level")
    elif 117 <= value <= 155:
        print("Normal haemoglobin level")
    elif value > 155:
        print("High haemoglobin level")
    else:
        print("Invalid input!")
else:
    print("Invalid gender!")

# Question 04
year = int(input("Enter a desired year : "))
if year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
