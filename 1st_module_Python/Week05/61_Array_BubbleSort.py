###Bubble Sort (loop, swap = biggest no. at end, each run)

##How It Works

#Pass Through the Array: Start at the beginning of the array.
#Compare Adjacent Elements: Compare each pair of adjacent elements.
#Swap if Necessary: If the first element is greater than the second, swap them.
#Repeat: Move to the next pair and continue the process until the end of the array is reached.
#Multiple Passes: After each pass, the largest unsorted element “bubbles up” to its correct position at the end of the array.
#Optimization: If no swaps are made during a pass, the array is already sorted, and the algorithm can terminate early.


#Key Points:

#Nested Loops: Bubble Sort typically uses two nested loops—the outer loop for the number of 
# passes and the inner loop for comparing and swapping elements.
#Early Termination: An optimization can be added to stop the algorithm if a pass completes 
# without any swaps, indicating that the list is already sorted.
#Stability: Bubble Sort is a stable sort, meaning that it preserves the relative order of 
# equal elements.


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

unsorted_list = [5, 1, 4, 2, 8]
sorted_list = bubble_sort(unsorted_list.copy())
print("Original List:", unsorted_list) # Original List: [5, 1, 4, 2, 8]
print("Sorted List:", sorted_list) # Sorted List: [1, 2, 4, 5, 8]




## Big O Analysis

#Worst Case:  (Reversed Array) - O(n2)
#Explanation: When the array is in descending order, every element must be swapped in each pass.
#Swaps: Every element gets swapped to its correct place, so the number of swaps is also O(n2)


#Best Case:  (Sorted Array) - O(n)
#Explanation: When the array is already sorted, Bubble Sort detects this and terminates after one full pass.
#Swaps: Zero swaps are performed because the array is already in order


import random

def bubble_sort_with_operations(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1  # Count the comparison
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1 # Count the swap
                swapped = True
        if not swapped:
            break
    return comparisons, swaps, swaps + comparisons

# Test Cases: Best, Worst and Average
# Change the number of elements in the array
# ⚠️ A large enough value WILL crash your browser 💥
num_elements = 100
best_case_array = list(range(1, num_elements + 1 ))
average_case_array = random.sample(best_case_array, len(best_case_array))
worst_case_array = best_case_array[::-1]

# Run sorting function
best_comparisons, best_swaps, best_operations = bubble_sort_with_operations(best_case_array.copy())
avg_comparisons, avg_swaps, avg_operations = bubble_sort_with_operations(average_case_array.copy())
worst_comparisons, worst_swaps, worst_operations = bubble_sort_with_operations(worst_case_array.copy())

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


