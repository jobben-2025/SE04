# Step 1: Create and Print a List
#Create a list of 5 items (e.g., your favorite fruits, numbers, or any objects you like).
listA = [2,4,6,8,10]
#Print the list to the screen.
print("Either all in one: " + str(listA))
print("")
print("First element: " + str(listA[0]))
print("Second element: " + str(listA[1]))
print("Third element: " + str(listA[2]))
print("Fourth element: " + str(listA[3]))
print("Fifth element: " + str(listA[4]))
print("")



# Step 2: Access Elements by Index and Negative Index
#Print the first item, the last item, and at least one item using a negative index (for example, my_list[-2]).
print("First item: " + str(listA[0]))
print("Last item: " + str(listA[-1]))


# Step: 3 Slice a List
#Print a subset of the list (for example, items from index 1 to 3).
print("Items index 1 to 3: " + str(listA[1:4]))

#Print everything from the beginning up to index 2, and from index 2 to the end.
print("Items index 0 to 2: " + str(listA[:3]))
print("Items index 2 to 4: " + str(listA[2:]))


# Step 4: Check if an Item Exists
#Use the "in" keyword (for example, if "apple" in my_list:) to check if a certain item is in the list.
#Print a message indicating whether the item is found.
if 6 in listA: print("6 is inside my list")

# Step 5: Add Items
#Use append() to add a new item to the end of the list.
#Use insert() to add an item at a specific index.
listA.append(7)
print("Added number 7 to list using append: " + str(listA))
#print("Added item to list index 0: ", listA[0])
listA.insert(0, 3)
print("Added number 3 to list using insert at index0: " + str(listA))


# Step 6: Change Items
#Update the value of a specific element by index.
print("Before change index 3 is: " + str(listA[3]))
listA[3] = 9
print("After index 3 is: " + str(listA[3]))

#Change multiple items at once by assigning to a slice (for example, my_list[1:3] = ["new1", "new2"]).
print("Before changing multiples, index 2-3 are: " + str(listA[2:4]))
listA[2:4] = [1,5]
print("Before changing multiples, index 2-3 are: " + str(listA[2:4]))
  

# Step 7: Remove items
#Remove a specific item by value using remove().
print("Actual list before removing item: " + str(listA))
listA.remove(7)
print("Actual list after removing item: " + str(listA))


#Remove an item at a specific index using pop().
listA.pop(4)
print("Actual list after removing item using pop at index 4=position 5: " + str(listA))

#Clear the entire list with clear() (or demonstrate using a temporary list).
listTemp = [1, 2, 3, 4, 5, 6]
print(f"Temporary list created: {listTemp}")
listTemp.clear()
print(f"Temporary list contents after using clear: {listTemp}")

# Step 8: Copy a list
#Create a copy of your list using list.copy() or slicing ([:]).
listB = listA.copy()
#listB = listA.copy[:]

print(f"This is copied list B from A: {str(listB)}")
#Modify the original list afterward, then print both lists to verify they are independent
listA[2] = 8
print("List A, changed index2: " + str(listA))
print("List B, unmodified:     " + str(listB))

# Step 9: Concatenate and Extend
#Using the + operator (e.g., list_a + list_b).
print("Content of listA before concatenation: " + str(listA))
listA = listA + listB
print("New listA+listB together in listA: " + str(listA))

#Using extend() (e.g., list_a.extend(list_b)).
print("Content of listA before using extend with another listA: " + str(listA))
listA.extend(listA)
print("Content of listA: " + str(listA))


# Step 10: Sort and Reverse
#Sort the list using sort().
print("Sorted listA: " + str(sorted(listA)))
#Reverse the sorted list using reverse().
print("Sorted listA: " + str(sorted(listA, reverse=True)))

#(Optional) Use sorted() to create a new sorted list without modifying the original
newlist = sorted(listA)
print("Created newlist with sorted listA: " + str(newlist))

# Count and Index
#Use count() to find how many times a particular value appears in the list.
result = newlist.count(5)
print("Counted 5's in the list are: " + str(result))
#Use index() to find the position of a specific value in the list.
#newlist.index(8)
print("Index position of searched value no.8: " + str(newlist.index(8)))

# List comprehension
#Create a new list that transforms or filters your existing list (for example, convert strings to uppercase if they meet a certain condition).
#Use the syntax [expression for item in my_list if condition].







