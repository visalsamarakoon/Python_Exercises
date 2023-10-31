# 9. Fundamentals of object-oriented programming

import random
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
        self.brake = -200

    def accelerate(self, change_of_speed):
        self.current_speed = self.current_speed + change_of_speed
        if self.current_speed >= self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, no_of_hours):
        self.travelled_distance = self.travelled_distance + (self.current_speed * no_of_hours)
        return self.travelled_distance

cars = []
for i in range(1, 11):
    cars.append(Car(f"ANC-{i}", random.randint(100, 200)))






new_car = Car("ABC-123", 142)
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)
new_car.drive(1.5)

print(f"The registration number is: {new_car.registration_number}")
print(f"Maximum speed: {new_car.maximum_speed}")
print(f"Current speed: {new_car.current_speed}")
print(f"After applying the emergency brake: {new_car.current_speed + new_car.brake}")
print(f"The travelled distance is: {new_car.travelled_distance}")

















