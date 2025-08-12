#Conversions: Strings, Lists and Tuples

#Convert Between Data Types
### Step 1:
#1.  Create a list of hobbies.
hobbies = ["cycling", "singing", "programming", "writing", "reading", "play computer"]

#2.  Convert it to a tuple.
tuple(hobbies)
    
#3.  Convert it back to a list.
list(hobbies)

#4.  Add one more hobby to the list.
hobbies.append("cooking")

#5.  Transform the list of hobbies into a string.
str(hobbies)
print(hobbies)

### Step 2:
#1.  Create the tuple `person = ("Alice", 30, "New York")`.
person = ("Alice", 30, "New York")
    
#2.  Convert `person` into a list.
person = list(person)
    
#3.  Add the hobbies string as the last item.
person.append("hobbies")
print(person)
    
#4.  Convert it back into a tuple and print it.
person = tuple(person)
print(person)
    

### Step 3:
#1.  Create a tuple called `students = ("Alice", "Louis", "Paris", "Alice", "Sara", "Alex", "Alice")`.
students = ("Alice", "Louis", "Paris", "Alice", "Sara", "Alex", "Alice")
    
#2.  Creacte a variable named `students_with_a` with an empty list as its value.
students_with_a = []
    
#3.  Use a `for` loop to store in the `students_with_a` list all the students with an `"a"` in the name in the tuple `students`.
for student in students:
    if 'a' in student.lower(): students_with_a.append(student)
print(students_with_a)
    
#4.  Print the value and the data type of `students_with_a`.
print(type(students_with_a))
print(students_with_a)
    
#5.  Transform the list `students_with_a` into a tuple and store that new value in a variable named `students_with_a_tuple`.
students_with_a_tuple = tuple(students_with_a)
    
#6.  Print the value and data type of the `students_with_a_tuple`.
print(type(students_with_a_tuple))
print(students_with_a_tuple)


