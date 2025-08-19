# Class representing a person with name and age

#__init__() method can accept parameters, allowing you to initialize the object with specific data upon creation. This means that for a given class of Person , when calling its constructor, e.g. Person('Reagan', 42) those arguments will be passed to the __init__() method for you to assign to the new object properties

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

# Class representing a rectangle with width and height
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Class representing a dog with a name and a breed, with a default breed value
class Dog:
    def __init__(self, name, breed="Unknown"):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

# Class representing a book with title, author, and year
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def summary(self):
        print(f"'{self.title}' by {self.author}, published in {self.year}.")

# Creating instances and using their methods
alice = Person("Alice", 30)
alice.introduce()  # Output: Hi, I'm Alice and I'm 30 years old.

reagan = Person("Reagan", 42)
reagan.introduce() # Output: Hi, I'm Reagan and I'm 42 years old.

rect = Rectangle(5, 10)
print("Rectangle area:", rect.area())  # Output: Rectangle area: 50

dog1 = Dog("Buddy")
dog2 = Dog("Max", breed="Labrador")
dog1.bark()  # Output: Buddy says woof!
dog2.bark()  # Output: Max says woof!

book1 = Book("1984", "George Orwell", 1949)
book1.summary()  # Output: '1984' by George Orwell, published in 1949.


book2 = Book("The Hobbit", "John Ronald Reuel Tolkien", 1937)
book2.summary()  # Output: 'The Hobbit' by John Ronald Reuel Tolkien, published in 1937.
