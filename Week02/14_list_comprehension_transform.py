# 1. Simple transformation
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print("Original numbers:", numbers)
print("Squares:", squares)

# 2. Filtering
even_numbers = [num for num in numbers if num % 2 == 0]
print("\nEven numbers:", even_numbers)

# 3. Data transformation with condition
fruits = ["apple", "banana", "cherry", "date"]
short_fruits = [fruit.upper() for fruit in fruits if len(fruit) <= 5]
print("\nOriginal fruits:", fruits)
print("Short fruits (5 letters or fewer, in uppercase):", short_fruits)

# 4. Using range in list comprehension
multiples_of_three = [x for x in range(1, 20) if x % 3 == 0]
print("\nMultiples of 3 (1-19):", multiples_of_three)

# 5. Nested list comprehension (all pairs of letters)
letters = ["A", "B", "C"]
pairs = [[x, y] for x in letters for y in letters if x != y]
print("\nAll possible distinct pairs:", pairs)
