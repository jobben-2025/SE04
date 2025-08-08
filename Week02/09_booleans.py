# Examples of values that evaluate to True
print("Truthy Values:")
print(True)           # The value True -> True
print(bool("Hello"))  # Non-empty string -> True
print(bool(123))      # Non-zero integer -> True
print(bool(3.14))     # Non-zero float -> True
print(bool([1, 2, 3]))  # Non-empty list -> True
print(bool({"a": 1}))  # Non-empty dictionary -> True

# Examples of values that evaluate to False
print("\nFalsy Values:")
print(False)          # The value False -> False
print(bool(""))       # Empty string -> False
print(bool(0))        # Zero -> False
print(bool(0.0))      # Float zero -> False
print(bool(0j))       # Complex zero -> False
print(bool([]))       # Empty list -> False
print(bool(()))       # Empty tuple -> False
print(bool({}))       # Empty dictionary -> False
print(bool(None))     # None -> False

# Truthy and Falsy check with conditionals
print("\nTruthy/Falsy Checks:")
is_list_empty = [] # We know an emtpy list will evaluate to False
if is_list_empty:
    print("The list is not empty")
else:
    print("The list is empty")  # Empty list -> False

is_string_empty = "Python" # We know an non-empty string will evaluate to True
if is_string_empty:
    print("The string is not empty")  # Non-empty string -> True
else:
    print("The string is empty")