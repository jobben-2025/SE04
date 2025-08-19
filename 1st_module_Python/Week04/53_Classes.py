# objects contain properties/attributes = characteristics, car color, model, speed
# and also behaviour/methods = describe capabilities, car drive brakeor honk

#__init__(self, ...):
#This method initializes the newly created object.
#It is called immediately after __new__ returns a new instance.
#It sets up the initial state of the object, assigning values to attributes or performing setup tasks.
#Unlike __new__, __init__ does not return anything; its purpose is to configure the instance.

#attributes (variables in class), describe objects
#methods (functions in class), actions object can perform

#classes always Capitalize !

class Car:
    # The __init__ method initializes a new Car object with given attributes
    def __init__(self, make, color):
        self.make = make    # Property: make of the car
        self.color = color    # Property: color of the car
        self.speed = 0        # Default speed property
    
    # Method to simulate accelerating the car
    def accelerate(self, increase):
        self.speed += increase
        print(f"The {self.color} {self.make} accelerates to {self.speed} mph.")
    
    # Method to simulate braking the car
    def brake(self, decrease):
        self.speed = max(0, self.speed - decrease)
        print(f"The {self.color} {self.make} slows down to {self.speed} mph.")
    
    # Method to display the car's current status
    def status(self):
        print(f"{self.color.capitalize()} {self.make} is moving at {self.speed} mph.")

# Creating an object (instance) of the Car class
my_car = Car(make="Toyota", color="red")

# Accessing object properties and methods
my_car.status()           # Display initial status
my_car.accelerate(30)     # Increase speed
my_car.brake(10)          # Decrease speed
my_car.status()           # Display updated status

print(type(my_car))


