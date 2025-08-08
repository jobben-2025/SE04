#  1. Create a Set
#Create a set named fruits containing at least 5 unique items (e.g., names of fruits).
#Print the set.
fruits = {"apple", "date", "kiwi", "mango", "cherry", "strawberry"}
print(f"Fruits in a set: {fruits}")

# 2. Check Membership
#Check if a specific item (e.g., "apple") is in fruits using the in keyword and print a message 
#confirming its presence or absence.
if 'apple' in fruits: print("There is an apple in fruits.")


# 3. Add and Update Items
#Add a new element to fruits using the add() method. Print the set after adding.
fruits.add("donut")
print("Fruits content after adding: ", fruits)

#Create another set more_fruits with at least 3 unique items.
more_fruits = {"orange", "pear", "lemon", "pineapple"}

#Use the update() method to add elements from more_fruits to fruits. Print the updated set
fruits.update(more_fruits)
print(f"Fruits after updating with more fruits: {fruits}")

# 4. Remove Items
#Remove an element from fruits using remove(). Print the set after removal.
fruits.remove("apple")
print(f"Fruits after removing the apple: {fruits}")

#Attempt to remove an element not in the set using discard() and observe that no error occurs.
fruits.discard("coconut")
print(f"Attempted to discard coconut from fruits with no error: {fruits}")

#Use pop() to remove and print an arbitrary element from fruits. Then print the set.
fruits.pop()
print(f"Popped out a random fruit: {fruits}")

#Use clear() to remove all elements from a copy of fruits and print the empty set
fruits2 = fruits.copy()
fruits2.clear()
print(f"Cleared fruits2 copy: {fruits2}")


# 5. Set Operations 
#Create two sets:
#set_a with some overlapping items with fruits.
set_a = {"apple", "banana", "kiwi", "mango", "date", "chinese-pear"}
#set_b with some different items.
set_b = {"car", "boat", "house", "truck", "mango"}


#Perform and print the result of the following operations:
#Union: Use union() to combine set_a and set_b.
union_set = set_a.union(set_b)
print(f"Union of set_a and set_b: {union_set}")

#Intersection: Use intersection() to find common elements between set_a and set_b.
intersected_items = set_a.intersection(set_b)
print("Found common items between set_a and set_b using interection: ", intersected_items)

#Difference: Use difference() to find elements in set_a not in set_b.
different_items = set_a.difference(set_b)
print("Different items in set_a from set_b: ", different_items)

#Symmetric Difference: Use symmetric_difference() to find items in either set_a or set_b, but not present in both.
#Definition WBS Learn platform - sets: methods: symmetric_difference()	^	Returns a new set with elements in either set but not in both.

difference_setab = set_a.symmetric_difference(set_b)         #this will display all unique items across both sets
                                                            #in this example no 'mango' from either side
print("Differences between set_a and set_b, both total: ", difference_setab)

#If I wanted 'difference_setab' to be checked back against set_a and set_b I could remove opposites:
difference_setab2 = difference_setab.copy()
print(difference_setab)
print(difference_setab2)

differences_seta_only = difference_setab.symmetric_difference_update(set_b)      #remove items of set_b; content exclusive set_a
differences_setb_only = difference_setab2.symmetric_difference_update(set_a)      #remove items of set_a; content exclusive set_b

print(difference_setab)
print(difference_setab2)


# 6. In-place Set Operations
#Use difference_update() on a set to remove items that are also in another set. Print the result.
set_b.difference_update(set_a)      #will remove the mango from set_b
print(set_b)

#Use intersection_update() on a set to keep only items common with another set. Print the result.

#Both sets are unique at this point, adding item 'mango' back to both sets to prepare
set_a.add('mango')
set_b.add('mango')
print("Common item in both sets is the mango:")
print(set_a)
print(set_b)

set_b.intersection_update(set_a)
#print(set_a)
print("Used intersection_update on set_b to only retain common items of set_a: ", set_b)


#Use update() to add elements from another set to the current set. Print the result
#new_fruits = {"apricot", "nectarine", "blackberry", "melon"}               #officially using a variable
#set_b.update(new_fruits)

set_b.update({"apricot", "nectarine", "blackberry", "melon"})               #direct also works
print("Updated set_b with apricot, nectarine, blackberry and melon: ", set_b)

# 7. Relational Methods
#Create two sets small_set and large_set such that small_set is a subset of large_set.
small_set = {3, 4, 5}
large_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#Use issubset() to verify that small_set is a subset of large_set and print the result.
print("The small_set is a subset of the large_set: ", small_set.issubset(large_set))

#Use issuperset() to verify that large_set is a superset of small_set and print the result.
print("The small_set is a superset of the large_set: ", small_set.issuperset(large_set))
#print("The large_set is a superset of the small_set: ", large_set.issuperset(small_set))

#Check if two sets are disjoint using isdisjoint() and print the result
print("The small_set is a disjoint of the large_set: ", small_set.isdisjoint(large_set))



