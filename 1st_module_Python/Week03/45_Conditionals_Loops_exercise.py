# 1. Basic If Condition
#Basic If Condition Write a block that checks if a number is positive, negative, or zero 
#using simple if, elif, and else. You must declare any necessary variable(s).
number = 0
if number == 0: print(f"Number is {number}")
elif number < 0: print(f"Number is negative.")
else: print(f"Number is positive.")

# 2. Grade Calculator
#Given a score between 0 and 100, use if, elif, and else to determine and 
#print the corresponding grade (A, B, C, D, or F).
given_score = 82

#GPA grading system for U.S.A. (percentage): A=4.0GPA - B=3.0GPA - D=1.0GPA - F=0.0GPA      ## copied from Wikipedia
#A = 90-100
#B = 80-89
#C = 70-79
#D = 60-69
#F = 0-59

if given_score > 89: print(f"Given score of {given_score} equals to grade: 'A'");
elif given_score > 79:  print(f"Given score of {given_score} equals to grade: 'B'");
elif given_score > 69:  print(f"Given score of {given_score} equals to grade: 'C'");
elif given_score > 59:  print(f"Given score of {given_score} equals to grade: 'D'");
else: print(f"Your score equals to: 'F' like failed!")


# 3. Ternary Operator Practice
#Use a ternary operator to set a variable status to "adult" if age
#is 18 or older, and "minor" otherwise.
age = 18
status = "adult" if age >= 18 else "minor"
print("This person is a(n): ", status)


# 4. For Loop over a List
#Iterate over a list of vehicles using a for loop and print an
#f-string with each vehicle
vehicles = ["sportscar", "truck", "weekendcar"]
for each in vehicles: print(f"I love my {each}!")


# 5. For Loop with Conditions
#Loop over numbers 1 to 10 using a for loop and print only the 
#even numbers, skipping the odds using continue.



# 6. While Loop Summation
#While Loop Summation Use a while loop to sum all numbers from 1 to 100. Print the total
# sum at the end


# 7. Break out of a Loop
#Iterate over a list of words and break out of the loop as soon as 
# a word with more than 5 letters is found. Print that word.

# 8. Nested Loops
# Create a list of people and a list of pets. Loop over the lists in order 
# to print all the possible combinations of persons and a respective pet


# 9. Loop with Else Clause
# Use a for loop to search for a specific value in a list. If the value
# is found, print a success message and break out of the loop. Otherwise, after the loop finishes,
# use an else clause to print that the value was not found


# 10. Pass Statement Usage
# Create an empty loop over a list of items using pass to practice structure 
# without executing any code


# 11. Pattern matching
#Create three lists: fruits, veggies, meat

#Add different food items to each list

#Create a match expression to determine if a given item in a variable item is a fruit, a veggie, a meat product or anything else.

#Remember you can create guards with if statements





