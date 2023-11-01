# 10. Association

elevators = []
class Building:
    def __init__(self, bottom_floor, top_floor, no_of_elevators):
        self.no_of_elevators = no_of_elevators
        for i in range(self.no_of_elevators):
            elevators.append(self.no_of_elevators)
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor


class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, floor):
        while floor > self.current_floor and floor < self.top_floor:
            if floor > self.current_floor:
                self.floor_up()
            elif floor < self.current_floor:
                self.floor_down()
            else:
                print("Invalid floor!")

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor = self.current_floor + 1
            print(f"The elevator is now in {self.current_floor}th floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor = self.current_floor - 1
            print(f"The elevator is now in {self.current_floor}th floor.")

    def run_elevator(self, elevator_number, destination_floor):
        while elevator_number > 0 or elevator_number < 4:
            destination_floor = self.current_floor + 1
            print(f"Elevator {elevator_number} is now moving to floor {destination_floor}")

    def fire_alarm(self):
        if fire_alarm:
            self.current_floor = self.bottom_floor
            print(f"Fire alarm activated! Elevator is now in floor {self.current_floor}.")


h = Elevator(1, 7)
fire_alarm = False
h.go_to_floor(7)
h.fire_alarm()
h1 = Building(1, 7, 3)


class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, destination_floor):
        if destination_floor > self.current_floor:
            self.floor_up(destination_floor)
        elif destination_floor < self.current_floor:
            self.floor_down(destination_floor)

    def floor_up(self, destination_floor):
        while self.current_floor < destination_floor:
            self.current_floor += 1
            print(f"Elevator is on floor {self.current_floor}")

    def floor_down(self, destination_floor):
        while self.current_floor > destination_floor:
            self.current_floor -= 1
            print(f"Elevator is on floor {self.current_floor}")

# Testing the Elevator class
elevator = Elevator(1, 10)
elevator.go_to_floor(5)
elevator.go_to_floor(1)
"""

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, destination_floor):
        if self.bottom_floor <= destination_floor <= self.top_floor:
            while self.current_floor != destination_floor:
                if self.current_floor < destination_floor:
                    self.floor_up()
                else:
                    self.floor_down()
        else:
            print("Invalid floor!")

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is on floor {self.current_floor}")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print(f"Elevator {elevator_number} does not exist in the building.")

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)
            print("Fire alarm triggered. Elevators are at the bottom floor.")

# Example usage:
building = Building(1, 7, 3)
building.run_elevator(0, 5)
building.fire_alarm()
"""