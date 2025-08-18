#Error handling in Python is managed using try...except blocks, which allow you to catch and handle exceptions (errors) gracefully without crashing the program. By anticipating potential errors in a block of code, you can ensure your program continues to run or provides informative feedback when unexpected events occur.

#The code inside the try block is executed first.
#If an exception occurs, Python stops executing the try block and jumps to the matching except block.
#The except block can catch specific exceptions or all exceptions, allowing tailored responses to different error types.
#Additional Clauses:

#else clause: Executes if no exceptions were raised in the try block.
#finally clause: Executes no matter what, whether an exception was raised or not, often used for cleanup actions.

def divide_10_by_n(number):
    try:
        result = 10 / number
    except TypeError:
        print("That's not a valid number!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print(f"10 divided by {number} is {result}")
    finally:
        print("Execution of try...except block is complete.\n")

divide_10_by_n('hi')
divide_10_by_n(0)
divide_10_by_n(2)
divide_10_by_n(3)
