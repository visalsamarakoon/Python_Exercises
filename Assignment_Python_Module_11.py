# 11.Inheritance

# Question 01

class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Name: {self.name}")


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        Publication.print_information(self)
        print(f"Author: {self.author}")
        print(f"Page count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        Publication.print_information(self)
        print(f"Chief Editor: {self.chief_editor}")


# Main Program

magazine1 = Magazine("Donald Duck", "Aki Hyyppä")
book1 = Book("Compartment No. 6", "Rosa Liksom", 192)

magazine1.print_information()
book1.print_information()

# ----------------------------------------------------------------------------------------------------------------------

# Question 02


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        if change >= 0:
            self.current_speed = min(self.current_speed + change, self.max_speed)
        else:
            self.current_speed = max(self.current_speed + change, 0)

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume


electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)


electric_car.accelerate(40)
gasoline_car.accelerate(30)


electric_car.drive(3)
gasoline_car.drive(3)


print(f"Electric Car: {electric_car.travelled_distance} km")
print(f"Gasoline Car: {gasoline_car.travelled_distance} km")
