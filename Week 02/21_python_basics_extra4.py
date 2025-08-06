#Comparison operators - price check

#Starting money
wallet = 20.0
#Prices of items
coffee_price = 3.5
sandwhich_price = 5.75
cookie_price = 1.25

#1. Check if the customer has enough money to buy one cookie; use >=
if wallet >= cookie_price: print("Enough money to buy one cookie.")

#2. Check if two coffees cost more than $7; use > and *
if (2*coffee_price) > 7: print("2 Coffees cost more than $7")
if (2*coffee_price) <= 7: print("2 Coffees cost $7 or less")

#3. Check if the cost of one sandwhich is equal to two cookies; use ==
result = sandwhich_price == (2* cookie_price)
if result == False: print("The cost of one sandwhich is not equal to 2 cookies")
if result == True: print("The cost of one sandwhich is equal to 2 cookies:")


#4. Check if sandwhich is not equal to coffee; use !=
result = sandwhich_price != (2* cookie_price)
print(f"Comparing price of 1 sandwhich is not same as 2 cookies gave {result} as result.")









