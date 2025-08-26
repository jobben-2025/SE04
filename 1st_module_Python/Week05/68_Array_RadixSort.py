#Radix Sort 
# is a non-comparison-based sorting algorithm that sorts integers by processing their digits (or characters, if you generalise) one position at a time. When each digit pass is done using a stable subroutine (commonly Counting Sort), Radix Sort can sort in , where:

#'n' is the number of elements.
#'k' is the number of digit positions needed (for example,  in base-10).


#How It Works

#1 Determine the Number of Digit Passes (k)
#Find the maximum element in the array to know how many digits you need to process 
# (e.g., a 3-digit number in base 10 requires k = 3 passes).

#2 Sort by Each Digit
#Least Significant Digit (LSD) first: Sort all elements according to this digit. A stable sort like Counting Sort is used so as not to disrupt the order established in previous passes.
#Move to Next More Significant Digit: Re-sort the entire array, but this time according to the next digit (tens, then hundreds, and so on).

#3 Repeat
#Continue until you have sorted by all k digit positions.
#When finished, the array is fully sorted.

#Breakdown

#Digit-by-Digit: Sorting happens one digit (or character position) at a time.
#Stability Matters: We rely on a stable sort (often Counting Sort) to ensure the relative order from previous passes is preserved.
#k Passes: We do as many passes as there are digit positions in the largest number, leading to k total sorts of n elements.

def get_digit(number, d):
    """Return d-th digit of number, where d=0 is LSD."""
    return (number // 10**d) % 10

def counting_sort_by_digit(arr, d):
    """Stable counting sort of arr by digit d."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for value in arr:
        digit = get_digit(value, d)
        count[digit] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        digit = get_digit(arr[i], d)
        count[digit] -= 1
        new_index = count[digit]
        output[new_index] = arr[i]
    return output

def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    k = 0
    while 10**k <= max_val:
        arr = counting_sort_by_digit(arr, k)
        k += 1
    return arr

my_array = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_array = radix_sort(my_array.copy())
print("Original Array:", my_array)
print("Sorted Array:", sorted_array)
      

#When the maximum digit count is small relative to n, Radix Sort can be very efficient. 
# If the numbers have many digits or k is large, its performance can degrade. Nevertheless, 
# for fixed-width integers (like 32-bit or 64-bit), k is effectively constant, making Radix Sort 
# near linear in n.




