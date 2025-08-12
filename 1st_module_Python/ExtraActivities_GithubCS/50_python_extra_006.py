#Tuples: Create and Access Tuples

#Create and Access Tuples

### Step 1:
#1.  Create a tuple called `person = ("Alice", 30, "Paris")`
person = ("Alice", 30, "Paris")
    
#2.  Print each item using indexing.
print("Name: ", person[0])
print("Age: ", person[1])
print("Location: ", person[2])

#3.  Use a `for` loop to print all values.
for item in person: print(item)

### Step 2:
#1.  Create a tuple called `students = ("Alice", "Louis", "Paris", "Alice", "Sara", "Alex", "Alice")`.
students = ("Alice", "Louis", "Paris", "Alice", "Sara", "Alex", "Alice")
    
#2.  Use a `for` loop to print each student in `students` that has an `"s"` in their name.
for student in students:
    if 's' in student: print("Student with 's' in the name:", student)

#3.  Count how many students named `"Alice"` are there in `students`.
print("How many students with name Alice: ", person.count("Alice"))
    
#4.   Slice the three items in the middle of the tuple and assing them as the value of a new tuple named `middle`.
student1, student2, *middle, student6, student7 = students
print(middle)    

#5.  Create a tupled named `concat_tuple` and pass the value of both tuples, `person` and `students`.
concat_tuple = person + students
print("Concatenated tuples of person+students: ", concat_tuple)

### Step 3:
#1.  Create a tuple called `numbers` and add at least 5 numbers inside.
numbers = (1,3,5,7,9)
    
#2.  Print each item using a `for` loop.
for num in numbers: print(num)

#3.  Create a new tuple named `numbers_2` with by concatenating the values of `numbers` as many times as items are inside it.
numbers_2 = (numbers)*5
print(numbers_2)



#4.  Print the item in the middle of the `numbers_2` tuple.
#first, *middle, last = numbers_2
middle_no = len(numbers_2)//2       
middle_no = numbers_2[middle_no]        #no #1 necessary because index no. lower than real no.!

print("The number in the middle is:", middle_no)


