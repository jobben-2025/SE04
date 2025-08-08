#Arithmetic operators

#you help a local café build a simple price calculator:

#Prices of items
coffee_price = 3.5
sandwhich_price = 5.75
cookie_price = 1.25

#Number of items a customer wants
coffees = 2
sandwhiches = 1
cookies = 3


#1. Calculate the total cost of all items purchased; use + and *
coffee_sold = coffee_price * coffees
sandwhich_sold = sandwhich_price * sandwhiches
cookie_sold = cookie_price * cookies
total = coffee_sold + sandwhich_sold + cookie_sold
print(f"Total cost of all sold items purchased is {total}")


#2. Calculate the average price of the items bought; use / and ()
average_price_items = total / (coffees+sandwhiches+cookies)
print("Average item price derived (total cost / total amount sold):", average_price_items)

#3. Check how many cookies one can buy with $10; use // ###the floor division // rounds the result down to the nearest whole number
given_money = 10
affordable_amount_cookies = given_money // cookie_price
print("With 10$ you can afford (cookies):", affordable_amount_cookies)

#4. Find the leftover money if a customer buys as many cookies as possible with $10; use %
change_money = given_money - (affordable_amount_cookies * cookie_price)
print("You receive change:", change_money)

#check_amount = affordable_amount_cookies*cookie_price
#print(check_amount)                    #8*1.25=10





