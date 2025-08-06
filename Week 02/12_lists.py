# Creating a list using square brackets
my_list = ["apple", "banana", "cherry"]
print("Initial List:", my_list)

# Ordered - values can be accessed by their index
print("\nFirst element: ", my_list[0])
print("\nSecond element: ", my_list[1])
print("\nThird element: ", my_list[2])
# An index value out of range throws an error
#print("\nFourth element: ", my_list[3])

# Changeable - we can change, add or remove items
my_list.append("cucumber")
print("\nAfter adding a new entry: ", my_list)
my_list[1] = "blueberry"
print("\nAfter changing the second item to 'blueberry':", my_list)

my_list.remove("cherry")
print("\nAfter removing 'cherry':", my_list)

# Allow duplicates
my_list.append("apple")

print("\nFinal List:", my_list)

# Order hasn't change even if values were removed
print("\nFirst element: ", my_list[0])
print("\nSecond element: ", my_list[1])
print("\nThird element: ", my_list[2])
print("\nThird element: ", my_list[3])