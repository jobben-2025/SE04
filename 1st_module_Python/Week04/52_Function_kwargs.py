def show_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

show_info(name="Alice", age=30, city="Paris")   #order+position matters



def full_function(a, b=10, *args, **kwargs):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"Extra positional args: {args}")
    print(f"Extra keyword args: {kwargsargs}")

    full_function(1,2,3,4,5, name="Alice", age=25)


    #in this sequence/order:  positionals,   any, keywords
    


#try:    #code that might cause an error ==== IF

#except: #code to run if an error happens ==== ELIF


def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    else:                                       #else and finally optional
        return f"Division finished"             #else met if no errors
    finally:                                    #always at the end
        print("Operation complete")

print(divide(10, 2))
print(divide(10, 0))


