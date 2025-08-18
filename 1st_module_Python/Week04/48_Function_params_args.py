#Parameter: A variable listed in the function’s definition that acts as a placeholder for an argument.
#Argument: The actual value passed to a function when calling it.



def add(a, b):
    return a + b
try:
    add(1)  # Raises TypeError due to missing argument
    #When calling a function, the number of provided arguments must match the number of required parameters (unless defaults or arbitrary arguments are used). Mismatches result in a TypeError.
except Exception as e:
    print(e)

def square(x): 
    return x * x    #A function can use the return statement to output a value, which can then be used by the caller. If no return is specified, it returns None by default.
result = square(4)  # result will be 16

def greet(name, greeting): 
    print(f"{greeting}, {name}!")
greet("Reagan", "Howdy")  # Positional arguments. Prints: Howdy, Reagan! 
greet(greeting="Hi", name="Alice")  # Keyword arguments. Prints: Hi, Alice!
greet(name="Bob", greeting="Hello")  # Keyword arguments. Prints: Hello, Bob!
#When calling a function, arguments must be passed to it in the order in which the parameters are specified in the function definition, however, keyword arguments allow you to pass values to parameters by explicitly naming them, enhancing code readability and order flexibility.

def greet(name, greeting="Hello"):      #Parameters can have default values. If no argument is provided for such parameters, the default is used.
    print(f"{greeting}, {name}!")
greet("Bob")  # Prints: Hello, Bob! using the default greeting
greet(name="Bob", greeting="Howdy")  # Prints: Howdy, Bob!

#Arbitrary Positional Parameters with *args
#*args collects extra positional arguments into a tuple, allowing functions to accept an arbitrary number of arguments. You can of course use anything else beside *args
def collect_with_args(*my_arbitrary_args):
    print(type(my_arbitrary_args))
    print(my_arbitrary_args)

collect_with_args(1, 2, 3)  # Prints: <class 'tuple'> (1, 2, 3)

#Arbitrary Keyword Parameters with **kwargs
#**kwargs collects extra keyword arguments into a dictionary, enabling dynamic parameter lists with keys. You can of course use anything else beside **kwargs
def collect_with_kwargs(**kwargs): 
    print(type(kwargs))
    print(kwargs)

collect_with_kwargs(a=1, b=2)  # Prints: <class 'dict'> {'a': 1, 'b': 2}

#Positional-Only and Keyword-Only Arguments
#Using / and * in function definitions, you can enforce parameters to be passed only positionally or only by keyword, respectively.
def only_positional(a, b, /): 
    return (a, b)
print(only_positional(1, 2))
#print(onlyPositional(a=1, b=2)) # Raises an error

def only_keyword(*, x):
  return x

print(only_keyword(x = 3))
#print(onlyKeyword(3)) # Raises an error

def combined_args(a, b, c, /, *, d): 
    return (a, b, c, d)
print(combined_args(1, 2 , 3, d=4)) 
# print(combined_args(1, 2 , 3, 4)) #Raises an error because d is keyword only



