### Personal Library Manager
#Goal:
#Build a Python program to manage a small personal library, practicing:

#String manipulation
#Lists, tuples, sets, dictionaries
#Conditionals (if/elif/else)
#Loops (while, for, nested loops)
#Functions (with parameters, return values, and optional arguments)
#Exit confirmation

#📊 Learning Objectives
#Grouping code into functions for better readability.
#Passing and returning data from functions.
#Practicing parameters and arguments.
#Working with multiple data structures in one program.
#Using loops and nested loops inside functions.
#Exit confirmation logic.

#📌 Features to Implement
#Add a Book – Store title, author, year, and genres.
#View All Books – Display every book in the library.
#Search Books by Title – Case-insensitive match.
#Show Statistics – Number of books, unique authors, genres count.
#Exit – Ask for confirmation before quitting.

#📂 Data Structures
#Book stored as a dictionary:        {
#                  "title": "The Hobbit",
#                  "author": "J.R.R. Tolkien",
#                  "year": 1937,
#                 "genres": ("fantasy", "adventure")
#      }
#List → stores all books.
#Set → stores all unique authors.
#Set → stores all unique genres.

#📜 Menu System
#The program should output 5 options to the user:
#               1. Add a Book
#               2. View All Books
#               3. Search Books by Title
#               4. Show Statistics
#               5. Exit
#Then, it has to:
#Ask the user to enter the number of the action it wishes to carry out.
#If the number is not in the range 1 to 5, send and error message and ask for a correct 
# option and keep looping this action until the user chooses an option in the list.
#If the number is in the range 1 to 5 redirect them to the correct block of code.

#🛠 Functions to Create
#add_book(library, authors, genres)
#Ask for book details.
#Format title & author using .title().
#Validate year as a number.
#Split genres by commas and store as a tuple.
#Add to library list.
#Update authors and genres sets.
#view_books(library)
#Loop and print all books in a formatted style.
#search_books(library, search_title)
#Convert search query to lowercase.
#Check all books for a match.
#Print details if found; otherwise, "No book found."
#show_statistics(library, authors, genres)
#Print total number of books.
#Print all unique authors.
#Nested loop to count how many books per genre.
#confirm_exit()
#Ask "Are you sure you want to exit? (yes/no)".
#Return True if yes, otherwise False.





