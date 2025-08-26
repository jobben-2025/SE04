#O1 = search item by index no.
#O(n) = scanning unsorted list, double list=double time
#O(log n) = lookup name of list, halfing list for middle detection
#O(n log n) = several splits into half (merge sort, heapsort, quicksort)
#O(n²) = double group, handshakes quadruple
#O(n!) = each item/shirt, add multiple fashion combinations

#nodes = data structures inside structures (tree)

#linked lists = lists in different memory places
#empty node/contains pointer to next item in memory
#1st element is list node
#end of list has node+pointer to next item
#2n list new node

#array is more efficient, but places defined amount in memory,
#new array needs copy and delete original afterwards

### Array:

import sys
 
my_list = [] 
'''
Empty list: 28 bytes in 32bit systems. 56 in 64bit systems
'''
print(f"{sys.getsizeof(my_list)} bytes")
my_list.append(1)
'''
After the first append, space for 4 pointers is allocated, 
pointers are 4 bytes in 32bit systems and 8 bytes in 64bit systems
'''
print(f"{sys.getsizeof(my_list)} bytes")
my_list.append(2)
my_list.append(3)
my_list.append(4)
'''
Expected: 44 bytes in 32bit systems and 88 bytes in 64bit systems
'''
print(f"{sys.getsizeof(my_list)} bytes")
my_list.append(5)
'''
Space for 4 more pointers is allocated. 
Expected 60 bytes in 32bit systems and 120 bytes in 64bit systems
'''
print(f"{sys.getsizeof(my_list)} bytes")



#So, how much memory are we using for a 4 integer list?
import sys
 
my_list = [1, 2, 3, 4]
size = sys.getsizeof(my_list)
 
for x in my_list:
  print(f"{x} is {sys.getsizeof(x)} bytes")
  size += sys.getsizeof(x)
 
print(f"{size} bytes") # 108 bytes in 32bit systems and 200 bytes in 64bit systems.




#1. Comparison-based Sorting Algorithms:
#BUB - Bubble Sort,
#SEL - Selection Sort,
#INS - Insertion Sort,
#MER - Merge Sort (recursive implementation),
#QUI - Quick Sort (recursive implementation),
#R-Q - Random Quick Sort (recursive implementation).

#2. Not Comparison-based Sorting Algorithms:
#COU - Counting Sort,
#RAD - Radix Sort.


#You need to already understand/remember all these:
#-. Logarithm and Exponentiation, e.g., log2(1024) = 10, 210 = 1024
#-. Arithmetic progression, e.g., 1+2+3+4+…+10 = 10*11/2 = 55
#-. Geometric progression, e.g., 1+2+4+8+..+1024 = 1*(1-211)/(1-2) = 2047
#-. Linear/Quadratic/Cubic function, e.g., f1(x) = x+2, f2(x) = x2+x-1, f3(x) = x3+2x2-x+7
#-. Ceiling, Floor, and Absolute function, e.g., ceil(3.1) = 4, floor(3.1) = 3, abs(-7) = 7
