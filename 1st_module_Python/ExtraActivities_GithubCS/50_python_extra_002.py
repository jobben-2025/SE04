#Lists: Shopping list

#Create a Shopping List

#*   Create a list named `shopping_list` with the items `milk`, `oranges`, `coffee`, `sugar` and `butter`.
shopping_list = ["milk",  "oranges", "coffee", "sugar", "butter"]
    
#*   Output the whole list.
print(shopping_list)

#*   Add `honey` at the end of the list.
shopping_list.append("honey")
print(shopping_list)
    
#*   Remove `milk` by passing its value.
shopping_list.remove("milk")
print(shopping_list)

#*   Add  `soy sauce` in the list as the third item.
shopping_list.insert(2, "soy sauce")
print(shopping_list)

#*   Remove the last item of the list.
shopping_list.pop()
print(shopping_list)

#*   Create a second list named `last_minute_items` with the items `blueberries`, `potatos` and `chicken`.
last_minute_items = ["blueberries", "potatoes", "chicken"]

#*   Add the items in `last_minute_items` to `shopping_list`.
shopping_list += last_minute_items
print(shopping_list)

#*   Remove all the items in both lists.
shopping_list.clear()
print(shopping_list)