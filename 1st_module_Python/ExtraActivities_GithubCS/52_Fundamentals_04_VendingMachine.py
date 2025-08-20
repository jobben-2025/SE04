### Vending Machine Simulator
#Goal:
#Simulate a simple vending machine, allowing users to practice:

#Strings, lists, tuples, sets, dictionaries
#Conditionals (if/elif/else)
#Loops (while, for, nested loops)
#Functions (with parameters and return values)
#Classes and objects
#Exit confirmation

#📊 Learning Objectives
#Model real-world objects with classes and methods.
#Use lists and sets to organize data.
#Handle loops, nested loops, and conditionals.
#Modularize code with functions.
#Implement menu-driven programs with exit confirmation.
#Track sales and stock levels dynamically.

#📌 Features to Implement
#Create Product – Store id, name, price, stock and sales of the product
#Add Product – Store product name, price, and stock quantity.
#View All Products – Display all available products with prices and stock.
#Purchase Product – Select a product, check if stock is available, deduct stock, and handle payment.
#Restock Product – Increase the stock quantity for a product.
#Show Statistics – Total products, total stock, total sales.
#Exit – Ask for confirmation before quitting.

#📂 Data Structures
#Class Product → creates the Product objects.
#List → stores all Product objects.

#📜 Menu System
#The program should output 6 options to the user:
#               1. Add Product
#               2. View All Products
#               3. Purchase Product
#               4. Restock Product
#               5. Show Statistics
#               6. Exit

#Then, it has to:
#Ask the user to enter the number of the action it wishes to carry out.
#If the number is not in the range 1 to 6, send and error message and ask for a correct option and 
# keep looping this action until the user chooses an option in the list.
#If the number is in the range 1 to 6 redirect them to the correct block of code.

#🛠 Classes and Functions to Create
#Class Product
#Attributes: product_id, name, price, stock and sales.
#Methods:
#purchase(quantity) → checks if there is enough stock for sale
#restock(amount) → adds more product
#display() → prints product info
#add_product(products_list, product_names_set)
#Ask for name, price, and stock.
#Validate inputs (price and stock must be numbers).
#Create a unique product_id.
#Add Product object to products_list.
#Add product name to product_names_set.
#view_products(products_list)
#Loop through all products and call display().
#purchase_product(products_list)
#Ask for product ID and quantity.
#Check stock and call purchase() method.
#Inform user if the purchase was successful or stock is insufficient.
#restock_product(products_list)
#Ask for product ID and quantity.
#Call restock() method of the corresponding Product.
#show_statistics(products_list)
#Total products (len(products_list)).
#Total stock (sum of all stock quantities).
#Total sales (sum of all sales attributes).
#confirm_exit()
#Ask "Are you sure you want to exit? (yes/no)".
#Return True if yes, otherwise False.










