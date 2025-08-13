# Simple if
number = 10 # Change the value of 10 to see how the conditions behave
if number > 5:
    print("Number is greater than 5")

# if...else
if number % 2:
    print("Number is odd")
else:
    print("Number is even")

# if, elif, else
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or below")

# Shorthand if...else (ternary operator)
#A compact way to assign a value or execute a simple expression based on a condition.
#result = value_if_true if condition else value_if_false
result = "odd" if number % 2 else "even"
print("The number is", result)

# The following block will throw an error if uncommented
#if number > 0:
#print("Positive number")