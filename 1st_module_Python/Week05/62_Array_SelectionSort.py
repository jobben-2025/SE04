#How It Works

#Find the Lowest Value: Traverse the array (or subarray) to locate the smallest element among the 
# unsorted portion.
#Swap to the Front: Swap this smallest element with the first element of the unsorted portion.
#Repeat: Narrow the unsorted portion by one, moving the boundary of the sorted portion forward. 
# Continue until all elements are in their correct positions.

#ensures each lowest element in the remaining unsorted portion is placed at the start of that 
# subarray, gradually building a fully sorted array.

#Breakdown

#Idea: During each pass, Selection Sort picks the lowest element of the unsorted subarray and 
# places it in its correct position by swapping.
#No Early Termination: Even if the array becomes sorted earlier, Selection Sort will still 
# continue until it completes all passes for each element.
#Swaps Count: At most n−1 swaps occur because you perform exactly one swap per pass (unless 
# the smallest element is already in place).

#====== compare 1st + 2nd, swap if needed = 1st no. is sorted, compare 2nd to 3rd etc.

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

unsorted_array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(unsorted_array.copy())

print("Original Array:", unsorted_array) # Original Array: [64, 25, 12, 22, 11]
print("Sorted Array:", sorted_array) # Sorted Array: [11, 12, 22, 25, 64]


#Big O Analysis

#Worst Case:  (Reversed Array) - (On2)
#Explanation: When the array is in descending order, you need to find the lowest and require 
# a swap on every pass.

#Best Case:  - (On2) !!!
#Explanation: Even if the array is already sorted, Selection Sort still checks every element 
# in the unsorted subarray. No early termination.
#Swaps: No swaps needed.

#Average Case:  - (On2)
#Explanation: On average, each pass scans the entire remaining subarray to find the minimum.
#Swaps: Up n-1 swaps since every pass potentially requires a swap.

import random

def selection_sort_with_operations(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1  # Count the comparison
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1  # Count the swap
    return comparisons, swaps, swaps + comparisons

# Test Cases: Best, Worst and Average
# Change the number of elements in the array
# ⚠️ A large enough value WILL crash your browser 💥
num_elements = 100
best_case_array = list(range(1, num_elements + 1 ))
average_case_array = random.sample(best_case_array, len(best_case_array))
worst_case_array = best_case_array[::-1]

# Run sorting function
best_comparisons, best_swaps, best_operations = selection_sort_with_operations(best_case_array.copy())
avg_comparisons, avg_swaps, avg_operations = selection_sort_with_operations(average_case_array.copy())
worst_comparisons, worst_swaps, worst_operations = selection_sort_with_operations(worst_case_array.copy())

# Print results
print("Best Case Scenario:")
print("Comparisons:", best_comparisons)
print("Swaps:", best_swaps)
print("Total Operations:", best_operations)

print("\nAverage Case Scenario:")
print("Comparisons:", avg_comparisons)
print("Swaps:", avg_swaps)
print("Total Operations:", avg_operations)

print("\nWorst Case Scenario:")
print("Comparisons:", worst_comparisons)
print("Swaps:", worst_swaps)
print("Total Operations:", worst_operations)




