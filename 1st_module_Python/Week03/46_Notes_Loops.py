
#will print count till it reaches 3 (prints 0-2), then closing the loop
count = 0
while count < 3:
    print(count)
    count += 1



#creates 0-4 and cycle through these, printing each no. ##for item in sequence
for i in range(5):
    print(i)


#check if a given number is in a certain range:
number = 10
is_in_range = number in range(1, 21)
print(is_in_range)



if 10000 <= number <= 30000:
    pass


#index in loops
for i in range(1,4):    #1 to 3
    for j in range(1,4):     #1 to 3
        print(i*j, end=" ")
    print() #move to next line

#break
for i in range(5):
    if i == 3:
        break       #reaching no.3 then break the condition and jump out
    print(i)



#Continue

for i in range(5):
    if i == 3:
        continue    #reaching no.3 will continue and print i
    print(i)


#pass
for i in range(5):
    if i==3:
        pass        #filler/placeholder for later code
    print(i)


#match pattern


day = 3
match day:
    case 1:
        print("Mon")
    case 2:
        print("Tue")



    case 6 | 7:                     # | represents OR
        print("Weekend")
    case _:
        print("Invalid day")












