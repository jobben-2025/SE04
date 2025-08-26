#Selection Sort
#Activity 1: Find the Top 3 Numbers

#👉 Goal: Write a Python program that uses Selection Sort to sort a list of numbers.
#After sorting, prints out the top 3 largest numbers.

#👉 Example Input: [12, 45, 3, 67, 23, 89, 5]
#👉 Expected Output: Top 3: [89, 67, 45]

def selection_sort(liste):    
    n= len(liste)
    for i in range(n-1):                        #7 items, index 0 to 6 == range(n-1) == 0,6
        min_index = i                           #i counts from 0 to 5
        for j in range(i+1,n):                  #i+1 from 1 to 6, end of range 7, j = increase by 1 each step
            if liste[j] < liste[min_index]:
                min_index = j
        if min_index != i:
            liste[i], liste[min_index] = liste[min_index], liste[i]
    return liste

unsorted_list = [12, 45, 3, 67, 23, 89, 5]      
#print(unsorted_list)
print(selection_sort(unsorted_list))

#Activity 2: Find the Top 3 Numbers

#👉 Goal: Rewrite the code above to order and print the top 3 smallest numbers.

#👉 Example Input: [12, 45, 3, 67, 23, 89, 5]
#👉 Expected Output: Top 3: [3, 12, 23]

def selection_sort(liste):    
    n= len(liste)
    for i in range(n-1):                        #7 items, index 0 to 6 == range(n-1) == 0,6
        min_index = i                           #i counts from 0 to 5
        for j in range(i+1,n):                  #i+1 from 1 to 6, end of range 7, j = increase by 1 each step
            if liste[j] < liste[min_index]:
                min_index = j
        if min_index != i:
            liste[i], liste[min_index] = liste[min_index], liste[i]
    #liste = [liste[0] , liste[1] , liste[2]]    #after sorting top3 from the left, rearrange results CHEAPO2
    return liste

unsorted_list = [12, 45, 3, 67, 23, 89, 5]      
print(selection_sort(unsorted_list))

#sorted list, smallest numbers ascending, print first 3 by index CHEAPO1:
#print(selection_sort(unsorted_list)[0])
#print(selection_sort(unsorted_list)[1])
#print(selection_sort(unsorted_list)[2])


#Activity 3: Sorting Cities by Name

#👉 Goal: Write a program that ask the user for a list of cities (e.g., ["Paris", "London", "Berlin", 
# "Rome"]) and sorts them alphabetically using Selection Sort.

#user_cities = input("Please enter city names (comma separated) you want to have sorted: ")
#city_list = list(user_cities.split(","))
city_list = [' London', ' Paris','Berlin',  'Rome']     #TESTING only!

def selection_sort(city_list):    
    
    for i in city_list:                 
        min_index = i                   
        for j in city_list:                  
            if city_list[j] < city_list[min_index]:
                min_index = j
        if min_index != i:
            city_list[i], city_list[min_index] = city_list[min_index], city_list[i]
    return city_list

print(city_list)
print(selection_sort(city_list))

#Activity 4: Sorting Cities By Length

#👉 Goal: Modify the algorithm to sort by string length instead of alphabetically.


