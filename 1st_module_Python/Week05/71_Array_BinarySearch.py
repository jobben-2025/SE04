#Binary Search 
# is a divide-and-conquer algorithm used for finding an element in a sorted array. 
# It works by repeatedly splitting the search interval in half, comparing the middle element 
# to the target, and discarding one half of the array each time until the element is found or 
# the array has been fully searched.

#How It Works
#Requires a Sorted Array: Before starting, ensure the array is sorted in ascending (or descending) 
# order.
#Check the Middle: Compare the middle element of the current subarray to the target.
#Discard Half:
#If the target is smaller than the middle element, discard the right half.
#If the target is larger, discard the left half.
#Repeat: Keep reducing the search space by half until the element is found or the subarray size 
# reaches zero

#Breakdown

#Must Be Sorted: Binary Search only works if the array is sorted.
#Halving the Array: Each comparison eliminates half of the array from further consideration.
#Efficient: This repeated halving yields a worst-case O(log2 n) time complexity. 
# We are using base 2 since the array is always halved

#PseudoCode
#FUNCTION BinarySearch(array, target)
#    left = 0
#    right = LENGTH(array) - 1
# 
#    WHILE left &lt;= right
#        mid = (left + right) // 2
#        IF array[mid] == target
#            RETURN mid
#        ELSE IF array[mid] &lt; target
#            left = mid + 1
#        ELSE
#            right = mid - 1
#        ENDIF
#    ENDWHILE
#    RETURN -1  # Not found
#END FUNCTION

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found

# Example usage
sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15]
index = binary_search(sorted_numbers, 11)

if index != -1:
    print(f"Found 11 at index {index}")
else:
    print("11 not found")

#Binary Search is significantly faster than Linear Search for large, sorted datasets. 
# However, sorting an unsorted array initially costs additional time (O(log2 n)), so Binary Search is 
# best used for data that either comes pre-sorted or is infrequently updated and searched 
# multiple times.


