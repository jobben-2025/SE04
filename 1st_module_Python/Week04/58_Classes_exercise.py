# Book class
#Create a Book Class
#Define a class named Book.
#The Book class should have an __init__() method that takes parameters for the book’s name, author, and 
# release_date.
#Store these parameters as attributes of the instance.
#Optionally, include a boolean attribute read initialized to False to track if the book has been read.

class Book:

    ADD_TAX = 1.19      #capitalize for constants inside class,
                        #define before any 'def' to be accessable

    def __init__(self, name, author, release_date, price):
        self.name = name
        self.author = author
        self.release_date = release_date
        self.read_status = False        #optional
        self.price = price

    def __str__(self):
        return f"{self.name} was written by {self.author} and published in {self.release_date}"
    
    def print_bookname(self):
         print(f"Bookname is {self.name}")

    def get_price(self):
         return self.price
    
    def get_tax_price(self):
         return self.price * self.ADD_TAX   #access constant


MyBook = Book("Hackelberry", "Moongoose", 1988, price=18.99) #create MyBook as instance
MyBook2 = Book("Cookbook", "Cooker", 1948, price=16.50) #create MyBook as instance
MyBook3 = Book("Sportbook", "Trainer", 1998, 33.20) #create MyBook as instance

#print(type(MyBook))
print(MyBook)           #accessing STR to print strings
print(MyBook2)
MyBook3.print_bookname() #calling method to print only bookname

print(f"The price of Book2 is {MyBook2.get_price()}")
print(f"The same book price, for end customers is {MyBook2.get_tax_price()}")

### teacher:
class Book:
    def __init__(self, name, author, release_date):
        self.name = name
        self.author = author
        self.release_date = release_date
        #self.read = False           #give attribute 'read' to object

    def __str__(self):
        return f"Title: {self.name}, Author: {self.author}, Release year: {self.release_date}" #linebreak n for returns

new_book = Book("Harry Potter and ...", "J.K.Rowling", 1998)  #new_book is new object
print(new_book)
print(new_book.name)
#new_book will always be updated by new values everytime, save new_book somewhere else

########isinstance(new_book, Book)      #check if an object is part of the class Book



# Book collection class
#Create a BookCollection Class
#Define a class named BookCollection.
#In the __init__() method, initialize the books to a list of books passed to the constructor or an empty list.
#If you pass a list, verify its elements are indeed instances of a Book otherwise, raise and exception.

#class BookCollection:
#    def __init__(self, books, Book):
#        if Book.name != None:
#            self.books.append(books)
#        else: self.books = []

#    def add_book(self, books):
#        self.books.append((Book))

#MyBookCollection1 = BookCollection.add_book(MyBook)
#MyBookCollection2 = BookCollection(MyBook2, MyBook3)
#print(MyBookCollection1)


### teacher:
class BookCollection:
    def __init__(self, books=None):     #default value of books is empty
        #self.books = []  #books collection will reset each time (no None)!!!
        if books == None:
            books = []
        if not all(isinstance(book, Book) for book in books): #check if a book of books is part of class 'Book'        
        #for book in books:
            #isinstance(book, Book)
            raise TypeError("All elements must be instances of Book.")
        #actual value creation follows:
        self.books = books


# 3. Add Books to the Collection
#Within the BookCollection class, create a method add_book(self, book) that takes a Book object as a 
# parameter and adds it to the collection (self.books).
#Verify every new entry is indeed an instance of Book otherwise, 
# raise and exception.

### teacher:                #always check errors/probems before writing function!!!
    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added.") #created by 'Book' class
        self.books.append(book)
        

# 4. Mark Books as Read
#In the BookCollection class, implement a method mark_as_read(self, book_name) that:
#Searches for a book by its name in the collection.
#If found, sets its read attribute to True.
#If not found, optionally prints a message indicating the book isn’t in the collection.
    #def mark_as_read(self, book_name):
    #    if Book.name in BookCollection:
    #        Book.read_status=True
    #    else: print("Book not in collection")

###teacher:
    def mark_as_read(self, book_name):
        for book in self.books:
            if book.name == book_name:
                book.read = True
                return
        print(f"Book '{book_name}' not found in the collection")

    def mark_as_unread(self, book_name):
        for book in self.books:
            if book.name == book_name:
                book.read = False
                return
        print(f"Book '{book_name}' not found in the collection")




# 5. Display Collection Status
#Optionally, add a method list_books(self) in BookCollection that prints out all the books with their details and read status.
    #def list_books(self):
    #    print(BookCollection)

# Test your code
#BookCollection.list_books(Book)


###teacher:
    def list_books(self):
        for book in self.books:
            if hasattr(book, "read"):
                status = "Read" if book.read else "Unread";
            else:
                status = "Unkown"
            print(f"Title: {book.name}\nAuthor: {book.author}\nRelease year: {book.release_date}\nStatus: {status}\n")


new_book_collection = BookCollection();
print(new_book_collection)



new_book_collection.add_book(Book("Harry Potter", "J.K. Rowling", 1998));
new_book_collection.add_book(Book("Bible", "Unkown", -1000));
new_book_collection.add_book(Book("The Hobbit", "J.R.R. Tolkien", 1937));

new_book_collection.mark_as_read("Harry Potter");
new_book_collection.mark_as_unread("Bible");

new_book_collection.list_books()

