# Step 1: Create Strings
#Create two strings: first_name and last_name with your first and last name.
#Create a multi-line string called bio describing yourself in two sentences.
first_name = str("Ben")
last_name = str("Becht")

bio = str("""My name is Ben, I do
          live in Germany and my newest interest
          lies within studying programming Python""")

print(bio)

# Step 2: Access Characters and Slice Strings
#Print the first character of first_name and the last character of last_name.
#Slice bio to print only the first 10 characters.

print("first name: " + first_name[:-2])
print("last name: " + last_name[4:])
print("bio: " + bio[:10])


# Step 3: Loop Through a String
#Use a for loop to print each character in your first_name on a new line
for i in first_name:     
    print (i)



# Step 4: String Length
#Print the length of bio using the len() function
counted_chars = len(bio)
print("bio contains: " + str(counted_chars) + " characters")

# Step 5: Check Substrings
#Check if the word "Python" is in the string bio and print the result.
#Check if the word "Java" is not in the string bio and print the result.
if 'Python' in str(bio): print("Python is contained in bio")
else: print("No Python in the bio found")

if 'Java' in str(bio): print("Python is contained in bio")
else: print("No Java in the bio found")



# Step 6: Modify Strings
#Convert first_name to uppercase and last_name to lowercase.
#Remove extra spaces from bio and replace any occurrence of "Python" with "coding".
#Split bio into a list of words and print the result.



# Step 7: Concatenate Strings
#Combine first_name and last_name into a single string full_name with a space in between.
#Print the full name


# Step 8: String Formatting
#Use an f-string to print:
#"Hello, my name is {full_name} and I love Python!"
#Use the format() method to print:
#"My full name is {} and I am {} years old." where {} are placeholders for full_name and your age



# Step 9: Escape Characters
#Create a string that includes a double quote and a single quote. Example:
#He said, "Python's great!"



# Bonus: Use String Methods
#The bio string centered within 50 characters.
#The count of the letter "a" in your full_name





