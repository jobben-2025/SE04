# Import the random module
import random

# Integers (int)
int_value1 = 10
int_value2 = -5
int_value3 = 0

print("Integer Examples:")
print("Positive Integer:", int_value1, "Type:", type(int_value1))
print("Negative Integer:", int_value2, "Type:", type(int_value2))
print("Zero:", int_value3, "Type:", type(int_value3))

# Floating-Point Numbers (float)
float_value1 = 3.14
float_value2 = -0.5
float_value3 = 10.0

print("\nFloat Examples:")
print("Positive Float:", float_value1, "Type:", type(float_value1))
print("Negative Float:", float_value2, "Type:", type(float_value2))
print("Whole Number as Float:", float_value3, "Type:", type(float_value3))

# Complex Numbers (complex)
complex_value1 = 2 + 3j
complex_value2 = -1 + 4j
complex_value3 = 0 + 1j

print("\nComplex Number Examples:")
print("Complex Number 1:", complex_value1, "Type:", type(complex_value1))
print("Complex Number 2:", complex_value2, "Type:", type(complex_value2))
print("Purely Imaginary Number:", complex_value3, "Type:", type(complex_value3))

# Accessing Real and Imaginary Parts of a Complex Number
print("\nAccessing Real and Imaginary Parts:")
print("Real Part of", complex_value1, "is", complex_value1.real)
print("Imaginary Part of", complex_value1, "is", complex_value1.imag)

# Random module
print("\nRandom module: 🎲")
# Generate a random integer between 1 and 10
random_int = random.randint(1, 10)
print("Random Integer (1-10):", random_int)

# Generate a random float between 0 and 1
random_float = random.random()
print("Random Float (0.0-1.0):", random_float)

# Generate a random float between two values, including those values
random_uniform = random.uniform(5, 10)
print("Random Float (5-10):", random_uniform)

# Simulate a simple dice roll (1-6)
dice_roll = random.randint(1, 6)
print("Dice Roll:", dice_roll)