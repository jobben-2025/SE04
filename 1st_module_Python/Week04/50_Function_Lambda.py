#functions can be:

#- Assigned to variables: You can assign a function to a variable name.
#- Passed as arguments: Functions can be passed as arguments to other functions.
#- Returned from functions: Functions can be created and returned by other functions.
#- Stored in data structures: Functions can be stored in lists, dictionaries, etc.

#Being first-class enables higher-order programming patterns such as callbacks, decorators, and, importantly 
# for our discussion, the use of lambda functions.


#=======================#
#A lambda function is a concise, anonymous function defined with the lambda keyword. It is a quick way to 
# create a function without formally defining it using def. Lambdas are often used for simple operations, 
# especially as arguments to higher-order functions due to their brevity (Kürze/Kurzform).

#Syntax:

# lambda arguments: expression
    #arguments: A comma-separated list of parameters.
    #expression: A single expression that is evaluated and returned.



# Functions can be passed as arguments
def my_func(func):
    print('This is the first function')
    func()

def another_func():
    print('This is another function')

my_func(another_func)


# Functions can be returned from another function and stored in variables
def multiply_by_n(multiplier):
    def multiply(number):
        print(multiplier * number) 
    return multiply

multiply_by_two = multiply_by_n(2)
multiply_by_three = multiply_by_n(3)

multiply_by_two(4)
multiply_by_three(4)
print()

# Assigning a lambda function to a variable
square = lambda x: x * x
print(square(5))  # Output: 25
print()

# Refactor our multiply_by_n example
def multiply_by_n_lambda(multiplier):
    return lambda number: print(multiplier * number)

multiply_by_five = multiply_by_n(5)
multiply_by_six = multiply_by_n(6)

multiply_by_five(4)
multiply_by_six(4)


           
