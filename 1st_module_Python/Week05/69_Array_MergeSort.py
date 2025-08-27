#Merge Sort 
# is a divide-and-conquer algorithm that sorts an array by splitting it into two halves, recursively sorting each half, and then merging the two sorted halves into a single, sorted array. It guarantees a worst-case performance of , making it one of the more efficient general-purpose sorting algorithms.

#How It Works
#Divide the Array: Split the array (or subarray) into two halves until each subarray has at most one element.
#Conquer (Recursive Sorting): Sort each half recursively using the same procedure.
#Merge: Take the two sorted halves and merge them back together into a single, sorted array

#Breakdown

#Divide: Recursively splits the array into halves until subarrays of size 1 or 0 are reached.
#Conquer: Each sub-subarray (size 1 or 0) is trivially sorted.
#Merge: Combine sorted sub-subarrays by comparing elements in order and building a merged, sorted array

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
    return arr

def merge(arr, left, mid, right):
    # Create temporary arrays
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2
    
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    
    # Merge step
    i = 0
    j = 0
    k = left
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # Copy remaining elements
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Example usage
my_array = [38, 27, 43, 3, 9, 82, 10]
sorted_array = merge_sort(my_array.copy(), 0, len(my_array) - 1)
print("Original Array:", my_array)
print("Sorted Array:", sorted_array)

#Merge Sort’s predictable performance in all cases makes it a good choice for reliably handling 
# large datasets. However, it requires extra memory (for the temporary subarrays), which might 
# be a consideration in memory-constrained environments. Otherwise, its stable nature (if implemented 
# carefully) and worst-case O(n logn) performance make it a widely used sorting algorithm in practice





