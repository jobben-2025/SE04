#Lists: Access and change

#Access and Change

### Step 1:

#1.  Create a list `colors = ["red", "green", "blue"]`
colors = ["red", "green", "blue"]
    
#2.  Print the first item using indexing.
print(colors[0])

#3.  Change "green" to "yellow".
colors[1] = "yellow"
    
#4.  Add `"green"`, `"purple"` and `"red"`.
colors += ["green", "purple", "red"]

#5.  Print the updated list.
print(colors)

### Step 2:

#1.  Slice `"red"`, `"yellow"` and `"blue"` and store them into the variable `primary_colors`.
primary_colors = colors[0:3]
    
#2.  Print the new list.
print(primary_colors)

# 3.  Slice `"purple"` and `"red"` and store them into the variable `warm_colors`.
warm_colors = colors[4:6]
    
#4.  Print the new list.
print(warm_colors)

#5.  Slice `"blue"` and `"green"` and store them into the variable `cold_colors`.
cold_colors = colors[2:4]
    
#6.  Print the new list.
print(cold_colors)    


### Step 3:

#1.  Concatenate the list `primary_colors` to `warm_colors`.
warm_colors = primary_colors + warm_colors
    
#2.  Print `warm_colors`.
print(warm_colors)
    
#3.  Find the index of any color that is not warm.
for item in warm_colors:
    if item in cold_colors:
        result = warm_colors.index(item)
        print("", result)          #blue is item no.3 = index 2

#4.  Using the index you find out in the last step, update the items to warm colors.
del warm_colors[result]             #delete item found before, using index position stored in variable 'result'
print(warm_colors)

