#https://playground.wbscod.in/python/python-lists/1
#Lists
#Activity 1: Build a Grocery List

#Create a list called groceries with 5 items.
groceries = ["butter", "milk", "sugar", "chocolate", "ham", "sausages", "cheese"]

#Add one more item at the end of the list.
groceries.append("meat")

#Remove an item using the value of said item.
groceries.remove("milk")

#Print the list.
print("Groceries: ", groceries)

#Activity 2: Favorite Numbers
#Create a list with at least 7 numbers.
listing = [1,2,3,4,5,6,7,8]

#Print:
print(listing)

#First 3 numbers using slicing.
print(listing[0:3])

#The list sorted in reverse without modifying the original list.
rev_listing = sorted(listing, reverse=True)
print(rev_listing)
print(listing)

#A copy of the 'reversed list' using indexing. ###Probably means slicing and not "indexing"?
#listing_rev_copy = listing.index(2)
#print(listing_rev_copy)
#Slicing would be easy with:
new_rev_list = rev_listing[:]
print(new_rev_list)

#The bigger (biggest?) number of the list.
searchfor = 0
for char in new_rev_list:
    if char > searchfor: searchfor = char
print(searchfor)

#The smallest number of the list.
searchfor = 100
for char in new_rev_list:
    if char < searchfor: searchfor = char
print(searchfor)

#A sum of all the numbers in the list.
result = sum(new_rev_list)
print("Sum of list: ", result)

#Activity 3: Movie List Analyzer
#Create a movies variable and store a list of your favorite movies.
movies = ["terminator", "rambo 1", "taxi taxi", "fast & furious", "Rambo 2"]

#Create a copy of the list in a second variable named favorite_movies updating each item to have the 
# first letter of each word capitalize.
favorite_movies = []
for word in movies:
    favorite_movies.append(word.title())

#Print the list favorite_movies.
print(favorite_movies)

#Sort the movies original list in descending order.
favorite_movies.sort()      #correcting original order to ascending, ABC...
#print(favorite_movies)
favorite_movies.sort(reverse=True)  #list in descending order

#Print movies.
print(favorite_movies)


