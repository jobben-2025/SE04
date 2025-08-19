
#Custom object methods in Python follow the same rules as regular functions, with one important 
# distinction: they automatically receive a special first parameter, conventionally named self.

#This parameter represents the instance of the class on which the method is being called, allowing 
# access to the object’s attributes and other methods.


import random

class Airplane:
    def __init__(self, airline, capacity):
        self.airline = airline
        self.capacity = capacity
        self.fuel = 0
        self.is_flying = False 

    def __str__(self):
        return f"{self.airline} (Capacity: {self.capacity}, Fuel: {self.fuel}, Flying: {self.is_flying})"

    def refuel(self, amount):
        self.fuel += amount
        print(f"Refueled {amount} units. Total fuel: {self.fuel}")

    def fly(self, distance):
        # Calculate the fuel needed for the given distance
        fuel_needed = distance * 1 
        # Check if there's enough fuel to start flying
        if self.fuel <= 0:
            print("Cannot start flying. No fuel!")
            return
        # Check if the plane has enough fuel for the desired distance
        if fuel_needed > self.fuel:
            print(f"Not enough fuel to fly that distance! Missing: {fuel_needed - self.fuel} units of fuel")
            return
        # Start flying if not already in the air
        if not self.is_flying:
            self.is_flying = True
        # Perform the flight
        self.fuel -= fuel_needed
        print(f"Flying {distance} km. Fuel consumed: {fuel_needed}, Fuel remaining: {self.fuel}")

    def land(self):
        # Can't land if not currently flying
        if not self.is_flying:
            print("Cannot land because the plane is not flying.")
            return
        self.is_flying = False
        print(f"The {self.airline} airplane has landed.")

    def status(self):
        print(self)


# Example usage:
plane = Airplane("AirPython", 180)
plane.status()            # Check initial status

plane.refuel(250)         # Refuel the airplane
plane.fly(200)            # Attempt to fly 200 km
plane.land()              # Land the airplane
plane.status()            # Check status after flying
plane.fly(250)            # Attempt to fly 250 km
plane.refuel(250)         # Refuel the airplane
plane.fly(250)            # Attempt to fly 250 km
plane.land()              # Land the airplane
plane.status()            # Check final status
