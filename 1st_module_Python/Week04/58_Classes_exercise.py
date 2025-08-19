# Book class
#Create a Book Class
#Define a class named Book.
#The Book class should have an __init__() method that takes parameters for the book’s name, author, and 
# release_date.
#Store these parameters as attributes of the instance.
#Optionally, include a boolean attribute read initialized to False to track if the book has been read.

class Book:
    def __init__(self, name, author, release_date):
        self.name = name
        self.author = author
        self.release_date = release_date
        self.read_status = False        #optional

    def __str__(self, name, author, release_date):
        print(f"{Book.name} was written by {Book.author} and published in {Book.release_date}")


Book("Hackelberry", "Moongoose", "1988")
MyBook = Book("Hackel", "Goose", 1988)
print(type(MyBook))


# Book collection class
#Create a BookCollection Class
#Define a class named BookCollection.
#In the __init__() method, initialize the books to a list of books passed to the constructor or an empty list.
#If you pass a list, verify its elements are indeed instances of a Book otherwise, raise and exception.

class BookCollection:
    def __init__(self, books):
        self.books = [Book.name, Book.author, Book.release_date]

    def add_book(self, book):
        self.book = self.books.append

    

# 3. Add Books to the Collection
#Within the BookCollection class, create a method add_book(self, book) that takes a Book object as a 
# parameter and adds it to the collection (self.books).
#Verify every new entry is indeed an instance of Book otherwise, raise and exception.



# 4. Mark Books as Read
#In the BookCollection class, implement a method mark_as_read(self, book_name) that:
#Searches for a book by its name in the collection.
#If found, sets its read attribute to True.
#If not found, optionally prints a message indicating the book isn’t in the collection.
    def mark_as_read(self, book_name):
        if Book.name in BookCollection:
            Book.read_status=True
        else: print("Book not in collection")

# 5. Display Collection Status
#Optionally, add a method list_books(self) in BookCollection that prints out all the books with their details and read status.
    def list_books(self):
        print(BookCollection.books)

# Test your code

BookCollection.list_books(Book)






