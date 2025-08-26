#Insertion Sort is a comparison-based sorting algorithm that builds the sorted array (or subarray) 
# one item at a time. In each pass, it inserts the current element into the appropriate position 
# in the already sorted portion of the array. While it has a worst-case complexity of , it can be 
# much faster for nearly sorted data, sometimes approaching ,

#How It Works

#Consider the first element of the array as already sorted.
#Take the next element (the first unsorted) and compare it with the elements of the sorted 
# subarray from right to left.
#Shift all elements that are greater than this new element one position to the right.
#Insert the new element into the correct position.
#Repeat steps 2–4 for all remaining elements until the entire array is sorted.

#Worst O(n2), approaching O(n) for nearly sorted data.

#Key Points:
#In-place algorithm (requires no additional array).
#Often efficient for small or partially sorted datasets.
#Stable sort (preserves the order of equal elements)


def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        insert_index = i
        current_value = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > current_value:
                arr[j+1] = arr[j]
                insert_index = j
            else:
                break
        arr[insert_index] = current_value
    return arr

unsorted_array = [12, 11, 13, 5, 6]
sorted_array = insertion_sort(unsorted_array.copy())
print("Original Array:", unsorted_array)  # [12, 11, 13, 5, 6]
print("Sorted Array:", sorted_array)      # [5, 6, 11, 12, 13]



#Big O Analysis

#Worst Case:  (Reversed Array) - O(n2)
#Explanation: When the array is in descending order, each new element is smaller than all preceding elements, requiring multiple shifts.
#Comparisons and shifts sum to about:

#Best Case: - O(n)
#Explanation: If the array is already sorted, each new element will be inserted immediately after only one comparison.
#Each element is compared once, resulting in a total of comparions of about:

#Average Case: - O(n2)
#Explanation: Elements usually move several positions for an arbitrary order.

import random

def insertion_sort_with_operations(arr):
    n = len(arr)
    comparisons = 0
    shifts = 0
    for i in range(1,n):
        insert_index = i
        current_value = arr[i]
        for j in range(i-1, -1, -1):
            comparisons += 1 # Count comparison
            if arr[j] > current_value:
                shifts += 1 # Count shifts
                arr[j+1] = arr[j]
                insert_index = j
            else:
                break
        arr[insert_index] = current_value
    return comparisons, shifts, comparisons + shifts

# Test Cases: Best, Worst and Average
num_elements = 100
best_case_array = list(range(1, num_elements + 1))
average_case_array = random.sample(best_case_array, len(best_case_array))
worst_case_array = best_case_array[::-1]

# Run sorting function
best_comparisons, best_shifts, best_operations = insertion_sort_with_operations(best_case_array.copy())
avg_comparisons, avg_shifts, avg_operations = insertion_sort_with_operations(average_case_array.copy())
worst_comparisons, worst_shifts, worst_operations = insertion_sort_with_operations(worst_case_array.copy())

print("Best Case Scenario:")
print("Comparisons:", best_comparisons)
print("Shifts:", best_shifts)
print("Total Operations:", best_operations)

print("\nAverage Case Scenario:")
print("Comparisons:", avg_comparisons)
print("Shifts:", avg_shifts)
print("Total Operations:", avg_operations)

print("\nWorst Case Scenario:")
print("Comparisons:", worst_comparisons)
print("Shifts:", worst_shifts)
print("Total Operations:", worst_operations)



