# Step 1: Arithmetic Operators
#Create two variables: a and b, and assign them the values 15 and 4.
a = 15
b = 4

# Perform arithmetic operations
#Perform and print the result of each of the following operations: addition, subtraction, 
# multiplication, division, floor division, modulus, and exponentiation.
result = a+b
print("addition: " + str(result))

result = a-b
print("subtraction: " + str(result))

result = a*b
print("multiplication: " + str(result))

result = a/b
print("division: " + str(result))

result = a//b
print("floor division: " + str(result))


result = a%b
print("modulus: " + str(result))

result = a**b
print("exponentiation: " + str(result))


# Step 2: Assignment Operators
#Start with a variable x = 10.
x = 10

# Modify x using assignment operators
#Use the +=, -=, *=, and /= operators to modify the value of x. Print the result after each operation
x += 5          #x = x+4
print("changed to +=: " + str(x))

x -= 3          #x = x-6
print("changed to -=: " + str(x))

x *= 2          #x = x*3
print("changed to *=: " + str(x))

x /= 4          #x = x/3
print("changed to /=: " + str(x))


# Step 3: Comparison Operators
# Compare a and b
#Compare a and b using ==, !=, >, <, >=, and <=. Print the results of each comparison
a = 15
b = 10
print(f"starting with a={a} and b={b}")

result = a==b
print(f"Is a==b : {result}")

result = a!=b
print(f"Is a!=b : {result}")

result = a>b
print(f"Is a>b : {result}")

result = a<b
print(f"Is a<b : {result}")

result = a>=b
print(f"Is a>=b : {result}")

result = a<=b
print(f"Is a<=b : {result}")
#print("is a<=b:", a<=b)        #teacher solution, much shorter, more efficient


# Step 4: Logical Operators
#Create two Boolean variables: is_python_fun = True and is_java_fun = False.
is_python_fun = True
is_java_fun = False

# Combine Boolean variables
#Use the and, or, and not operators to combine or negate these values. Print the results
state = is_python_fun and is_java_fun
print(f"python and java: {state}")

state = is_python_fun or is_java_fun
print(f"python or java: {state}")

state = is_python_fun and not is_java_fun
print(f"python and not java: {state}")

state = not is_python_fun or is_java_fun
print(f"not python or java: {state}")


# Step 5: Identity Operators
# Check identities
#Create two lists: list1 = [1, 2, 3] and list2 = list1.
list1 = [1, 2, 3]
list2 = list1

#Check if list1 is list2 and if list1 is not list2.
check_list = (list1==list2)
print(f"List1==list2: {check_list}")        
print(f"List1==list2:", list1 is list2)        #alternative from teacher

check_list = (list1!=list2)
print(f"List1!=list2: {check_list}")

# Check if list1 is list3
#Create a third list list3 = [1, 2, 3]. Check if list1 is list3
list3 = [1, 2, 3]
check_list = (list1==list3)
print(f"List1==list3: {check_list}")        

# Step 6: Membership Operators
#Create a string text = "Python programming is fun!"
textblob = "Python programming is fun!"

# Check membership
#Check if the word "Python" is in the string.
#Check if the word "Java" is not in the string
if "Python" in textblob: print("Text string contains Python")
if "Java" not in textblob: print("Text string contains no Java")

    
# Step 7: Bitwise Operators (Bonus)
# Perform bitwise operations
#Perform the following operations with a = 5 and b = 3:
a=5
b=3
print(f"Starting with a={a} and b={b}")
#Bitwise AND (&)
new_result = a & b
print(f"Result of a & b: " + str(new_result))

#Bitwise OR (|)
new_result = a | b
print(f"Result of a | b: " + str(new_result))

#Bitwise XOR (^)
new_result = a ^ b
print(f"Result of a ^ b: " + str(new_result))

#Bitwise left shift (<<) for a by 1
new_result = a << b
print(f"Result of a << b: " + str(new_result))

#Bitwise right shift (>>) for b by 1
new_result = a >> b
print(f"Result of a >> b: " + str(new_result))


# Step 8: Operator Precedence
# Write expressions with precedence
#Write an expression combining +, *, and ** operators. Use parentheses to change the order of operations.
a = 7
b = 9
c = 2
d = -3

new_result = (a + b)**c-d
print(f"Started with a={a}, b={b}, c={c}, d={d}")
print(f"Calculated (a+b)**c-d = " + str(new_result))




#Evaluate the expression with and without parentheses to see how precedence works
a = 7
b = 9
c = 2
d = -3

new_result = a + b**c-d
print(f"Started with a={a}, b={b}, c={c}, d={d}")
print(f"Calculated a+b**c-d = " + str(new_result))





