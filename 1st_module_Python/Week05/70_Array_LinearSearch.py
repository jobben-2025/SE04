#Linear Search 
# is the most straightforward way to look for an element within an array. It checks every element 
# from the start of the array until it finds the target or reaches the end of the array.

#How It Works
#Start at the Beginning: Set an index pointer (e.g., i) to 0.
#Compare Each Element: For each index, check if the current element matches the target value.
#Stop If Found: If a match is found, return the index (or the element).
#Continue Until the End: If the target is never found, report that the value does not exist in the 
# array (often -1 or None as a sentinel).
#Because Linear Search does not assume the array is sorted, it always inspects elements in order, 
# making it simple but potentially slow when the array is large.



#Breakdown
#No Pre-sorting Required: Linear Search works on unsorted data.
#Potentially Many Comparisons: In the worst case, you might check every element without finding the 
# target (or finding it at the very end).
#Best Case: The target is located at the first position, requiring only one comparison.
#Easy to Implement: Minimal overhead, straightforward logic.

#PseudoCode
#FUNCTION LinearSearch(array, target)
#    FOR i FROM 0 TO LENGTH(array) - 1
#        IF array[i] == target
#            RETURN i
#        ENDIF
#    ENDFOR
#    RETURN -1  # Not found
#END FUNCTION


def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# Example usage
numbers = [4, 2, 7, 1, 8]
index = linear_search(numbers, 7)

if index != -1:
    print(f"Found 7 at index {index}")
else:
    print("7 not found")

#For small or unsorted datasets, Linear Search is simple and effective. 
# However, if searching is frequent and the dataset is large, more efficient algorithms 
# (like Binary Search, on a sorted array) can be significantly faster.

