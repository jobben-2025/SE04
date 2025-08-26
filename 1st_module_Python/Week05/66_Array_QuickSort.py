#QuickSort
#Quick Sort is a divide-and-conquer sorting algorithm that achieves, on average, a time complexity of . It works by partitioning the array around a chosen pivot, placing elements lower than the pivot to its left and higher elements to its right, then recursively sorting the resulting subarrays.

#How It Works

#Choose a Pivot: Pick a value in the array to be the pivot element.
#Partition: Rearrange the array so that all values lower than the pivot are on the left, and all values greater than the pivot are on the right.
#Swap Pivot: Swap the pivot element with the first element in the higher-values subarray so that the pivot lands in its correct position.
#Recursively Sort: Recursively apply the same operations to the left subarray (lower values) and the right subarray (higher values) until the entire array is sorted.


#Breakdown

#Divide and Conquer
#Quick Sort partitions the array into two subarrays around the pivot.
#Recursive Sorting
#Sort the left subarray (all elements smaller than pivot).
#Sort the right subarray (all elements larger than pivot).
#Partitioning Strategy
#Implementation can differ (e.g., choosing first, last, or a random pivot).
#This choice affects performance but not the overall approach.


#Quick Sort’s performance heavily depends on the pivot selection and the distribution of array values. In practice, choosing a random pivot or using techniques like median-of-three can avoid consistently bad pivots and maintain O(n logn) average performance



def quick_sort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)
    return arr

def partition(arr, left, right):
    pivot_value = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # Place the pivot in its final position
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

# Example usage
my_array = [10, 7, 8, 9, 1, 5]
sorted_array = quick_sort(my_array.copy(), 0, len(my_array) - 1)
print("Original Array:", my_array)   # [10, 7, 8, 9, 1, 5]
print("Sorted Array:", sorted_array) # [1, 5, 7, 8, 9, 10]








