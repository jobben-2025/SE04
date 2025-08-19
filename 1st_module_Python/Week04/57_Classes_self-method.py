#self allows methods to access and modify the attributes and other methods of the same object. 
# It distinguishes between different instances of a class and their respective data

class Dog:
    def __init__(self, name):
        # Here, 'self.name' is an attribute attached to this Dog instance
        self.name = name

    def bark(self):
        # 'self' refers to the instance on which bark() is called
        print(f"{self.name} says woof!")

class Cat:
    def __init__(current_object, name):
        # You don't need to use self but it's strongly suggested because ✨convention✨
        current_object.name = name

    def meow(current_object):
        # 'self' refers to the instance on which meow() is called
        print(f"{current_object.name} says meow!")


# Create a Dog instance
my_dog = Dog("Buddy")
# Call the bark method on the instance
my_dog.bark()  # Output: Buddy says woof!
# Create a Cat instance
my_cat = Cat("Mr. Whiskers IV")
# Call the meow method on the instance
my_cat.meow()
