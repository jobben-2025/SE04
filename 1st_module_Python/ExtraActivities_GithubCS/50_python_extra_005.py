#Lists: Looping through lists

#Using `for` Loop with Lists

### Step 1:
students = ["Max", "Umi",  "Rud", "Ben", "Waqar", "Nedim"]
students.sort()

#1.  Loop through each student in the `students` list and print: `"Hello [student_name]"`.
for each in students:
    print(f"Hello {each}")
    
#2.  Create a list named `students_upper` and store in it a copy of the `students` list but with all items in uppercase.
students_upper = students.copy()
students_upper = [each.upper() for each in students_upper]
        
#3.  Print the `students_upper` list.
print(students_upper)
    
#4.  Use a for loop to remove all the instances of `"Nedim"` form the `students` list.
for student in students:
    if student == 'Nedim':
        students.remove(student)
print(students)    

### Step 2:
#1.  Create a list named `fruits_With_A` and store in it a copy of the `fruits` list and lowercase those that have an `"a"` in the name.
fruits = ["Iii", "Apple", "Banana", "Pear", "Grape", "Coconut"]
print("Fruits: ", fruits)

fruits_With_A = []

for fruit in fruits:
    #print(fruit)
    if "a" in fruit.lower(): fruits_With_A.append(fruit.lower());
    else: fruits_With_A.append(fruit);

#2.  Print the `fruits_With_A`.
print("Fruits with A: ", fruits_With_A)

#3.  Loop through each fruit in the `fruits` list and print: `"I like [fruit]"`.
for fruit in fruits: print(f"I like {fruit}")
    
#4.  Use a loop to append each item on the `fruits` list to the `healthy_food` list.
healthy_food = ["sausage", "cheese", "chocolate", "pralines"]
for fruit in fruits: healthy_food.append(fruit)
    
#5.  Print the updated list.
print("Healthy food: ",  healthy_food)