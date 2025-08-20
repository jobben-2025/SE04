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


# Book collection class
#Create a BookCollection Class
#Define a class named BookCollection.
#In the __init__() method, initialize the books to a list of books passed to the constructor or an empty list.
#If you pass a list, verify its elements are indeed instances of a Book otherwise, raise and exception.

class BookCollection:
    def __init__(self, books, Book):
        if Book.name != None:
            self.books.append(books)
        else: self.books = []

    def add_book(self, books):
        self.books.append((Book))

MyBookCollection1 = BookCollection.add_book(MyBook)
MyBookCollection2 = BookCollection(MyBook2, MyBook3)
print(MyBookCollection1)

# 3. Add Books to the Collection
#Within the BookCollection class, create a method add_book(self, book) that takes a Book object as a 
# parameter and adds it to the collection (self.books).
#Verify every new entry is indeed an instance of Book otherwise, 
# raise and exception.



# 4. Mark Books as Read
#In the BookCollection class, implement a method mark_as_read(self, book_name) that:
#Searches for a book by its name in the collection.
#If found, sets its read attribute to True.
#If not found, optionally prints a message indicating the book isn’t in the collection.
    #def mark_as_read(self, book_name):
    #    if Book.name in BookCollection:
    #        Book.read_status=True
    #    else: print("Book not in collection")

# 5. Display Collection Status
#Optionally, add a method list_books(self) in BookCollection that prints out all the books with their details and read status.
    #def list_books(self):
    #    print(BookCollection)

# Test your code

#BookCollection.list_books(Book)






