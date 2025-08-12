#Lists: Sorting, Counting & Reversing

#Sorting, Counting & Reversing

### Step 1:

#1.  Create a list of numbers.
numbers = [1,2,6,6,3,5,6,8,9,4,7]
    
#2.  Sort it in ascending order.
numbers.sort()
print(numbers)

#3.  Count how many times a specific number appears.
print("How often was no.6 in the list: ", numbers.count(6))

#4.  Print the maximum and minimum number.
print("Minimum no.: ", numbers[0])
print("Maximum no.: ", numbers[10])    

### Step 2:

#1.  Create a list with the names of the students in your class named `students`.
students = ["Max", "Umi",  "Rud", "Ben", "Waqar", "Nedim"]
    
#2.  Print `students`.
print(students)

#3.  Create a sorted copy of the list inside the variable `sorted_students`.
sorted_students = sorted(students)
    
#4.  Print `sorted_students`.
print("Sorted students: ", sorted_students)

#5.  Reverse the order of the original `students` list.
rev_sorted_students = sorted(students, reverse=True)
    
#6.  Print `students`.
print("Sorted reverse students: ", rev_sorted_students)

#7.  Create a reversed copy of the `sorted_students` and store it into a variable named `sort_reversed`.
sort_reversed = sorted_students.copy()
    
#8.  Print `sort_reversed`.
print(sort_reversed)