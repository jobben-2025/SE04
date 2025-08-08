# Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Assignment Operators
x = 5
x += 3  # Same as x = x + 3
print("\nAssignment Operators:")
print("x after += 3:", x)

# Comparison Operators
print("\nComparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a <= b:", a <= b)

# Logical Operators
print("\nLogical Operators:")
print("True and False:", True and False)
print("True or False:", True or False)
print("not True:", not True)

# Identity Operators
print("\nIdentity Operators:")
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y)  # True (same memory location)
print("x is z:", x is z)  # False (different memory locations)

# Membership Operators
print("\nMembership Operators:")
print("2 in x:", 2 in x)
print("4 not in x:", 4 not in x)

# Bitwise Operators
print("\nBitwise Operators:")

# Bitwise AND: Compares each bit of two numbers. The result has a 1 in each position where both operands have 1s.
# Example: 5 -> 0101, 3 -> 0011, result -> 0001 (1 in decimal)
print("5 & 3:", 5 & 3)

# Bitwise OR: Compares each bit of two numbers. The result has a 1 in each position where at least one operand has a 1.
# Example: 5 -> 0101, 3 -> 0011, result -> 0111 (7 in decimal)
print("5 | 3:", 5 | 3)

# Bitwise XOR: Compares each bit of two numbers. The result has a 1 in each position where the bits of the operands are different.
# Example: 5 -> 0101, 3 -> 0011, result -> 0110 (6 in decimal)
print("5 ^ 3:", 5 ^ 3)

# Bitwise NOT: Inverts each bit of the number. Flips 0s to 1s and 1s to 0s.
# Example: 5 -> 0101, result -> 1010 (in 2's complement, it's -6 in decimal)
print("~5:", ~5)

# Bitwise Left Shift: Shifts the bits of the number to the left by the specified number of positions.
# Each left shift is equivalent to multiplying the number by 2.
# Example: 5 -> 0101, result after shifting 1 position -> 1010 (10 in decimal)
print("5 << 1:", 5 << 1)

# Bitwise Right Shift: Shifts the bits of the number to the right by the specified number of positions.
# Each right shift is equivalent to dividing the number by 2 (ignoring the remainder).
# Example: 5 -> 0101, result after shifting 1 position -> 0010 (2 in decimal)
print("5 >> 1:", 5 >> 1)

# Operator Precedence Example
print("\nOperator Precedence Example:")
print("3 + 5 * 2 ** 2:", 3 + 5 * 2 ** 2)  # Evaluates to 23