# 1. Sum of List Elements
#Create a function sum_list(numbers) that takes a list of numbers and returns their sum.
#Use a loop to iterate through the list.
#Use a variable to accumulate the total and return it.

numbers = [1,41,4]
sum = 0

def sum_list(numbers):
    for num in numbers:
        global sum
        sum = sum + num
    return sum

result = sum_list(numbers)
print(sum)

#print(result) #returns sum from within function


# 2. Repeated Greeting
#Write a function repeat_greeting(name, times) that prints a greeting to name a specified number of times.
#Use a loop to print the greeting repeatedly.
#Each greeting should be printed on a new line.
def repeat_greeting(name, times):
    while times >0:
        #for times in times:
        print(f"Hello, {name}! Amazing you are here!")
        times = times -1

repeat_greeting("Ben", times=8)

#for i in range(from, to, steps) = (1, times, 2) would go 2,4,6,...
#for i in range(times) - go through loop, by number

# 3. Factorial Calculation
#Define a function factorial(n) that returns the factorial of a given number n.
#Use a loop (such as a for or while loop) to multiply numbers from 1 to n.
#Return the factorial result.

### didn't know. factorials, used wikipedia and example code
def factorial2(n):
    global fact
    fact = 1

    for i in range(1, n+1):
        fact = fact * i
    else: print("Number given is negative.") 

#factorial2(8)
#print("Factorial is: ", fact)

###### solution by teacher ####
def factorial(n):
    result =1
    for i in range(1,n+1):
        result *= i
    return result

fact_result = factorial(5)
print(fact_result)


# 4. Fibonacci Sequence Generator
#Fibonacci Sequence Generator
#Create a function fibonacci(n) that returns a list containing the first n numbers of the Fibonacci sequence.
#Use loops and conditionals to calculate each Fibonacci number.
#Start the sequence with 0 and 1, then build the sequence up to n terms.


### own solution 19.8.25 ###
def fibonacci(n):
    fibo1=0
    fibo2=0
    fibo_result = 0
    
    if n <= 2: 
        fibo_result=1
        print(fibo_result)
    elif n>=3:
         fibo1=1
         fibo2=1
         for i in range(1, n+1, 1):
              fibo1=fibo2
              fibo2=fibo_result
              
              fibo_result = fibo1+fibo2
              print(fibo_result)

fibonacci(5)


############### teacher ###############
def fibonacci3(n):
    fib_sequence = [];
    a, b = 0, 1;
    for _ in range(n):          #for i in range(n): not using i use _
        fib_sequence.append(a);
        a, b = b, a+b;
    return fib_sequence; #return the whole sequence out of the function

print(fibonacci3(10))
############### /teacher ###############


# 5. Maximum of Two Numbers
#Write a function max_of_two(a, b) that returns the larger of two numbers.
#Use an if...else conditional to compare a and b.
#Return the greater value.

def max_of_two(a,b):
    global result           #carry the result as global variable outside
    if a>b: result = a      #change variable to 'return a' as output
    elif a<b: result=b
    elif a==b: result=a
    else:
        print("Unable to compare")
    return result

max_of_two(40,19)
print("Bigger number is: ", result)

print("Using return a: ", max_of_two(40,19))


###teacher:
def max_of_two2(a,  b):
    if a > b:
        return a;
    elif a < b:
        return b;
    else:
        return "a and b are equal"      # f{a} and {b} are equal

print(max_of_two2(6,16))

# 6. Print a Pattern with Nested Loops
#Design a function print_triangle(rows) that prints a right-angled triangle of asterisks (*) with a given number of rows.
#Use nested loops: an outer loop for rows and an inner loop for printing asterisks in each row.
#Each subsequent row should have one more asterisk than the previous row

def print_triangle(number_of_rows):

    lines = number_of_rows+1
    i = 0
    while i < lines:
        #for num in number_of_rows:
        symbol="*"
        print(symbol * i)
        if i != lines: i=i+1

print_triangle(5)

###teacher:
def print_triangle2(rows):
    for i in range(1, rows+1):
        print("*" *i);       #multiply the icon against the no. of row

print(print_triangle2(7))
