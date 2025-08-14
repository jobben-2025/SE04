# https://playground.wbscod.in/python/python-control-structures/1
#Conditionals: Part 1

#Activity 1: Checking the Age
#Create the variable age and give it a value.
age = 17
#Check age:
#If it is 18 or older, print "You are an adult".
if age >= 18: print("1. You are an adult")

#Activity 2: If–Else Practice
#Update the value of age.
age = 22

#Check age again but this time:
#If it is 18 or older, print "You are an adult".
#Otherwise, print "You are a minor".
if age >= 18: print("2. You are an adult")
else: print("You are a minor")


#Activity 2: Ternary Refractor
#Create the variable status and use a ternary to give it the value
# of "minor" or "adult" conditionally depending on the age.
#Print status.
status = "adult" if age >= 18 else "minor"
print("You are a(n): ", status)


#Activity 3: If–Elif–Else Practice
#Update age once again, this time with a negative number or a number bigger than 100.
age = 23

#Check age once again, this time accounting for invalid ages:
#If age is bigger than 100, print "Are you Yoda?"
#If it is 18 or older, print "You are an adult".
#If it is between 0 and 17, print "You are a minor".
#Otherwise, print "You haven't been born yet. Wait 9 months and try again."

if age > 100: print("Are you Yoda?")
elif age > 18: print("You are an adult.")
elif age > -1: print("You are a minor.")
elif age < 0: print("You have not been born yet. Wait 9 months and try again.")
else: print("Error detected, you entered something unrecognizable.")


