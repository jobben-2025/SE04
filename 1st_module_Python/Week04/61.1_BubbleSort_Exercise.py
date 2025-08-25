#Bubble Sort

#Activity 1: Sorting Scores
#👉 Goal: Write a Python program that takes a list of exam scores from the user 
# and sorts them in ascending order using Bubble Sort.

#👉 Example Input: [56, 89, 34, 100, 77]
#👉 Expected Output: [34, 56, 77, 89, 100]

user_list = [56, 89, 34, 100, 77]
print("Original list: ", user_list)

n=len(user_list)
for i in range(n):
    swap = False
    for j in range(n-i-1):
        #print(range(n-i-1))
        if user_list[j] > user_list[j+1]:       
            user_list[j], user_list[j+1] = user_list[j+1], user_list[j]
            swap = True
    if swap == False:
        break

print("Bubble sorted list: ", user_list)


#Activity 2: Sorting Scores Reversed
#👉 Goal: Modify the code from activity 1 to sort in descending order.

#👉 Example Input: [56, 89, 34, 100, 77]
#👉 Expected Output: [100, 89, 77, 56, 34]

#   if user_list[j] < user_list[j+1]:       ## only the comparator '<' needs to change


#Activity 3: Sorting Names
#👉 Goal: Write a program that promts the user to enter a list of names 
# (e.g., "John, Alice, Bob") and sorts them alphabetically using bubble sort.

names_list = []
names = input("Please enter a few names, separated by comma each: ")
names_list = names.split(",")

#names_list = ['Sarah', 'Ben', 'John']   #for qick test!
print(names_list)

n=len(names_list)
#print(n)

for i in range(n):
    swap = False
    for j in range(n-i-1):
        if names_list[j] > names_list[j+1]:
            names_list[j], names_list[j+1] = names_list[j+1], names_list[j]
            swap = True
    if swap == False:
        break

print(names_list)


#Activity 4: Sorting Names Reversed
#👉 Goal: Modify the program to sort in reverse alphabetical order.

#if names_list[j] < names_list[j+1]:        #same change as before used, reverses the order

