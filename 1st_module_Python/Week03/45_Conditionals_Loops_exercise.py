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
given_score = 55

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
#elif given_score == 0-59:  print(f"Given score of {given_score} equals to grade: 'F'"); #NOT WORK!!!
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

for i in range(1,11):
    if i /2 == int(i/2):    #check if result is an integer,  uneven no. always has decimal
        print(i)

#just print the above generated values, showing the decimals:
#for i in range(1,11):
#        print(i/2)
#        print(int(i/2))

        
# 6. While Loop Summation
#While Loop Summation Use a while loop to sum all numbers from 1 to 100. Print the total
# sum at the end
result = 0
for i in range(1, 100):
    result = result+i

print("Sum of all no. from 1 to 100: ", result)

# 7. Break out of a Loop
#Iterate over a list of words and break out of the loop as soon as 
# a word with more than 5 letters is found. Print that word.
wordlist = ["first", "second", "third", "fourth",  "fifth"]

for word in wordlist:
    if len(word) > 5: 
        print("This word is longer than 5 letters: ", word)
        break


# 8. Nested Loops
# Create a list of people and a list of pets. Loop over the lists in order 
# to print all the possible combinations of persons and a respective pet
people = ["Alice", "Bernadette", "Chris", "John", "Timothy", "Helga"]
pets = ["cat", "dog", "cow"]

for person in people:
    for pet in pets:
        print("Combination of ", person +" & "+ pet)


# 9. Loop with Else Clause
# Use a 'for' loop to search for a specific value in a list. If the value
# is found, print a success message and break out of the loop. Otherwise, 
# after the loop finishes, use an else clause to print that the value was 
# not found
people = ["Alice", "Bernadette", "Chris", "John", "Timothy", "Helga"]
searchfor = "Timothy"

#if searchfor > "":             #would be necessary for outer ELSE....
for person in people:
    if person == searchfor:
        status = "found"
        print(f"Found person", searchfor)
        break        
else:
    print("Message only if no break occurs")
#if status != "found": print(f"Sorry, no value found.")
#using ELSE in inner IF statement would print message 'not found' for each 
# person, using it with unnecessary encapsulation before for-loop would
#print it whether the inner loop was broken out of (found) or not.


# 10. Pass Statement Usage
# Create an empty loop over a list of items using pass to practice structure 
# without executing any code
items = ["phone", "book", "letter", "pen"]

for item in items:
    pass

# 11. Pattern matching
#Create three lists: fruits, veggies, meat
fruits = []
veggies = []
meats = []

#Add different food items to each list
fruits.append("orange")
fruits.append("apple")
fruits.append("pear")
veggies.append("carrot")
veggies.append("potatoe")
veggies.append("tomatoe")
meats = ["chicken", "beef", "swine"]

#print(fruits)
#print(veggies)
#print(meats)

#Create a match expression to determine if a given item in a variable 
# item is a fruit, a veggie, a meat product or anything else.
#Remember you can create guards with if statements

given_item = "carrot"
status = ""

if status == "":
    for fruit in fruits:
        if given_item == fruit:
            status = fruits
            print("It is a fruit.")
            break
    for meat in meats:
        if given_item == meat:
            status = meats
            print("It is a meat.")
    for veggie in veggies:
        if given_item == veggie:
            status = veggies
            print("It is a veggie.")
else:
    print("error, status was set before")

if status == "": print("Item could not be found, check spelling or item not in list.")







