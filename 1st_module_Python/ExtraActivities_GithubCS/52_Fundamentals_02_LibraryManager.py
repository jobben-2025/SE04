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
#Add a Book – Store title, author, year, and genres.                OK
#View All Books – Display every book in the library.                OK
#Search Books by Title – Case-insensitive match.
#Show Statistics – Number of books, unique authors, genres count.
#Exit – Ask for confirmation before quitting.                       OK

#📂 Data Structures
#Book stored as a dictionary:        {                              OK
#                  "title": "The Hobbit",
#                  "author": "J.R.R. Tolkien",
#                  "year": 1937,
#                 "genres": ("fantasy", "adventure")
#      }
#List → stores all books.                                           OK
#Set → stores all unique authors.                                   OK
#Set → stores all unique genres.                                    OK

#📜 Menu System
#The program should output 5 options to the user:
#               1. Add a Book                   as dict
#               2. View All Books               from list
#               3. Search Books by Title
#               4. Show Statistics              authors set
#               5. Exit
#Then, it has to:
#Ask the user to enter the number of the action it wishes to carry out.                     OK
#If the number is not in the range 1 to 5, send and error message and ask for a correct 
# option and keep looping this action until the user chooses an option in the list.
#If the number is in the range 1 to 5 redirect them to the correct block of code.

#🛠 Functions to Create

#add_book(library, authors, genres)                                                 OK
#Ask for book details.                                                              OK
#Format title & author using .title().                                              OK
#Validate year as a number.                                                         OK
#Split genres by commas and store as a tuple.                                       OK
#Add to library list.                                                               OK
#Update authors and genres sets.                                                    OK

#view_books(library)                                                                OK
#Loop and print all books in a formatted style.                                     more style / formats!!

#search_books(library, search_title)
#Convert search query to lowercase.
#Check all books for a match.
#Print details if found; otherwise, "No book found."

#show_statistics(library, authors, genres)                                          
#Print total number of books.                                                       OK                                          
#Print all unique authors.                                                          OK
#Nested loop to count how many books per genre. (set in all_books count)            

#confirm_exit()                                                                     OK              
#Ask "Are you sure you want to exit? (yes/no)".                                     OK
#Return True if yes, otherwise False.                                               OK



global keep_program_running
keep_program_running = 1

global all_books_list
all_books_list = []          #empty to begin with, later filled with some example books
all_books_list = ['Title1', 'Author1', '1999', 'Genre1', 'Title2', 'Author2', '2000', 'Genre1', 'Title3', 'Author3', None, 'Genre3'] #TESTING only!


def add_book():
    print("")
    print("1. Add a Book")
    print("")
    entered_title = input("Enter the book's title: ").title()
    entered_author = input("Enter the author: ").title()
    entered_year = (input("Enter the published year: "))
    if entered_year.isdigit() == False:
        entered_year = None
    entered_genre = input("Enter the genres (comma separated): ")
    entered_genre = tuple(entered_genre.split(","))                 #code per task definition CHECK!
    
    new_book_dict = {"Title": entered_title, "Author": entered_author, "Year": entered_year, "Genre": entered_genre}
    print(f"The new book {entered_title}, published by {entered_author} in {entered_year} is from genre {entered_genre}.")
    #save the book to the all_books_list
    print("Dictionary for this book created: ", new_book_dict)
    global all_books_list
    all_books_list.append(entered_title)
    all_books_list.append(entered_author)
    all_books_list.append(entered_year)
    all_books_list.append(entered_genre)
    print("All books list has been updated with this book.")
    
    #choose if continue to add, if yes set 'continue_adding' True, otherwise false
    continue_adding = True if input("Want to add another book? y/n") == "y" else False
    if continue_adding == True:
        add_book()
    else:
        main_menu()
    
    return

def view_all_books():
    global all_books_list
    print("")
    print("2. View All Books")
    print("")
    global count_items
    count_items = 0
    for book in all_books_list:
        count_items += all_books_list.count(book)
    amount_books = int(count_items/4)
    for i in range(0, count_items, 4):
        print(f"Title: {all_books_list[i]}")
        print(f"Author: {all_books_list[i+1]}")
        print(f"Year: {all_books_list[i+2]}")
        print(f"Genre: {all_books_list[i+3]}")
        print("")
    
    continue_adding = True if input("Want to add a book to library? y/n") == "y" else False
    if continue_adding == True:
        add_book()
    else:
        main_menu()
    
    return
     
        
def show_statistics():
    global all_books_list
    print("")
    print("4. Show Statistics")
    print("")
    #count_items = 0
    #for book in all_books_list:
    #    count_items += all_books_list.count(book)
    amount_items = int(len(all_books_list))
    amount_books = int(len(all_books_list)/4)
    print(f"Currently the library holds {amount_books} books.")
    print("")
    #print("len: ", type(len(all_books_list)))
    #print("count items: ", amount_items)
    author_set = []
    #authors as list to set here: use GLOBAL if needed elsewhere
    for i in range(1, amount_items, 4):
        #print(all_books_list[i])    
        author_set.append(all_books_list[i])
    author_set = set(author_set)                #authors as set
    #print("Unique Authors: ", author_set)
    print("Unique Authors: ")
    for each in author_set:
        print(each)
    print("")

    genre_tuple = []
    for i in range(3, amount_items, 4):    
        genre_tuple.append(all_books_list[i])
    genre_tuple = tuple(genre_tuple)            #genres as tuple
    genre_set = set(genre_tuple)                #genres as set
    #print("Tuple Genre: ", genre_tuple)
    #print("Unique Genres: ", genre_set)
    print("Unique Genres: ")
    for each in genre_set:
        print(each)
    print("")
    #Genre counts
    
    



    



def main_menu():
    global keep_program_running

    if keep_program_running == 1:
        print("")
        print("MAIN MENU:")
        print("")
        print("1. Add a Book")
        print("2. View All Books")
        print("3. Search Books by Title")
        print("4. Show Statistics")
        print("5. Exit")
        print("")
        user_input = int(input("Please select a menu option and press 'enter': "))

        if user_input == 1:
            add_book()
        elif user_input == 2:
            view_all_books()
        elif user_input == 3:
            pass
        elif user_input == 4:
            show_statistics()
        elif user_input == 5:
            user_exit = input("Are you sure you want to quit? Confirm with 'y' only: ")
            if user_exit == "y":
                keep_program_running = 0
                return
            else:
                main_menu()
        else:
            print("Sorry, you need to select an available option between 1-5.")
            main_menu()
    else:
        return
    
    







if keep_program_running == 1:
    main_menu()





