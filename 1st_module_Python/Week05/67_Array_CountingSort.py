#Counting Sort is a non-comparison-based sorting algorithm that sorts elements by counting their occurrences. Unlike comparison-based algorithms such as Quick Sort or Merge Sort, Counting Sort can achieve linear time  under certain conditions—particularly when the range of possible values  is not significantly larger than the number of elements .

#How It Works

#Determine the Range: Identify the minimum and maximum values (or assume a known range) of the input array.
#Create a Count Array: Allocate an array of size k (where k is the range of input values) initialised to zero.
#Count Occurrences: For each element in the original array, increment the count at the corresponding index in the count array.
#Compute Cumulative Counts: Transform the count array such that each position holds the cumulative sum of counts. This helps determine the final positions of each element in the sorted array.
#Place Elements: Iterate over the original array (often from right to left for stability) and place each element into its correct position in an output array, based on the cumulative counts.


#Breakdown

#Non-Comparison: Counting Sort categorises elements by indexing rather than comparing them pairwise.
#Range-Dependent: The algorithm’s efficiency depends on , the range of the input data. If  is large relative to , Counting Sort may be less efficient than  sorts.
#Stability: By iterating from right to left (and placing elements in a stable manner), Counting Sort preserves the input order of identical elements.

def counting_sort(arr, max_val):
    count = [0] * (max_val + 1)
    for x in arr:
        count[x] += 1
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]
    n = len(arr)
    result = [0] * n
    for i in range(n - 1, -1, -1):
        x = arr[i]
        count[x] -= 1
        new_index = count[x]
        result[new_index] = x
    return result

unsorted_array = [4, 2, 2, 8, 3, 3, 1]
max_value = max(unsorted_array)  # 8
sorted_array = counting_sort(unsorted_array, max_value)
print("Original Array:", unsorted_array)
print("Sorted Array:", sorted_array)


#Counting Sort can be extremely efficient when 'k' is much less than 'n', often outperforming 
# comparison-based sorts. However, if 'k' is comparable to or much larger than 'n', it may be less practical in terms of memory usage and overall speed.



