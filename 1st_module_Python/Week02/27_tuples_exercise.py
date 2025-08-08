# 1. Create a Tuple
#Create a variable named my_tuple and assign it a tuple containing at least 5 items (they can be strings, numbers, or a mix).
my_tuple = ("apple", "juice", "wine", "beer", "42", "§31", "$20")
other_tuple = (22, 23, 25, 29, 31, 33)

# 2. Print the Tuple
#Use the print() function to display the contents of my_tuple.
print("Contents of my_tuple: ", my_tuple)


# 3. Access Tuple Items
#Print the first item of the tuple using an index of 0.
print("First item: ", my_tuple[0])

#Print the last item of the tuple using a negative index.
print("Last item: ", my_tuple[-1])


# 4. Slice the Tuple
#Print a slice of the tuple that includes some middle items
print("Tuples from index 3-5: ", my_tuple[3:6])

#Print a slice that goes from the start of the tuple up to a certain index
print("Tuples till index 3: ", my_tuple[:4])

#Print a slice that starts at a certain index and goes to the end
print("Tuples from index 3: ", my_tuple[3:])


# 5. Check if an Item Exists
#Use the in keyword to check if a certain item exists in my_tuple.
#if "apple" in my_tuple: print("We have an apple here!")            #first solution
if "apple" in my_tuple: check_var = 1                               #2nd solution according to follow-up question

#Print a message indicating whether the item is found
if check_var == 1: print("Found apple!")


# 6. Count and Index
#Use the count() method to find how many times a specific value appears in my_tuple. >>only works single digits!!!
other_tuple = (2, 3, 2, 9, 3, 3)
print("Setup tuple with only numbers: ", other_tuple)
tuples_count = other_tuple.count(2)
print("Result of counted single digit numbers inside tuple: ", tuples_count)

#To sort out single numbers from longer numbers or even a character from strings; 
#conversion to string necessary+looping: code from GPT
count_2 = 0
for num in my_tuple:
    count_2 += str(num).count('e')
print("Result of counted char e using for loop and string conversion: ", count_2)

#Use the index() method to find the position of the first occurrence of that value
result = other_tuple.index(2)
print("Index position of first found no.2: ", result)


# 7. Packing and Unpacking
#Packing: You’ve already packed the tuple by assigning multiple values to my_tuple.
#Unpacking: Unpack my_tuple into separate variables so that each variable corresponds to an item in the tuple 
item1, item2, item3, item4, item5, item6, item7 = my_tuple
print("unpacked: ", item1, item2, item3, item4, item5, item6, item7)

#Use the asterisk (*) in another unpacking scenario 
(itemA, itemB, itemC, *RemainingItems) = my_tuple
print("unpacked using asterisk: ", itemA, itemB, itemC, RemainingItems)


# 8. Joining Tuples
#Create another tuple named another_tuple with a few items.
another_tuple = ("house", "boat", "bicycle", "Road66", "22 potatoes", "87", "29")

#Concatenate my_tuple and another_tuple using the + operator. Print the result.
result = my_tuple + another_tuple
print("my_tuple and another_tuple joined by +: ", result)

#Multiply one of your tuples by an integer and print the result to see the repeated items.
result = other_tuple[3]*4
print("Multiplied other_tuples index 3 with 4: ", result)




