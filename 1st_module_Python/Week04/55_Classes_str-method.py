# This class defines a __str__ method

#__str__ method is a special method in Python that defines how an object is represented as a 
# string for human-readable output. When you pass an object to print() or call str() on it, 
# Python internally calls the object’s __str__ method to determine what string to display. 
# This method should return a string that is descriptive and easy to read, summarizing the object’s 
# important information


class CarWithStr:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

# This class doesn't define a __str__ method
class CarWithoutStr:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Create cars
car1 = CarWithStr("Ford", "Mustang", 1968)
car2 = CarWithoutStr("Toyota", "Corolla", 2020)

# When printing an object, Python calls its __str__ method
print(car1)  # Output: 1968 Ford Mustang
print(car2)  # Output: <__main__.CarWithoutStr object at MEMORY_ADDRESS>

