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


