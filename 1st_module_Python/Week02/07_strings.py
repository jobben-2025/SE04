# Single and Double Quotes
single_quote = 'Hello'
double_quote = "It's a beautiful day"
print(single_quote)
print(double_quote)

# Multi-Line Strings
multiline = """This is
a multi-line 
string."""
print(multiline)

# Strings are Arrays
text = "Python"
print("First character:", text[0])
print("Last character:", text[-1])

# Looping Through a String
for char in text:
    print(char)

# String Length
print("Length of the string:", len(text))

# Check if String Exists
phrase = "Learning Python is fun!"
print("Python" in phrase)
print("fun" not in phrase)

# Slicing Strings
print("Slice 0-6:", text[0:6])
print("Slice from 3:", text[3:])

# Modifying Strings
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Trimmed:", "     Hello     ".strip())
print("Replace:", text.replace("Py", "My"))
print("Split:", text.split("t"))

# Concatenation
first_name = "John"
last_name = "Doe"
print("Full name:", first_name + " " + last_name)

# String Formatting
age = 34
name = "Jorge"
# Format function
print("I am {name} and I'm {age} years old.".format(name = "Jorge", age = 34))
print("I am {name} and I'm {age} years old.".format(name = "Jorge", age = 34))
print("I am {} and I'm {} years old.".format("Jorge", 34))
# f-string
print(f"I am {name} and I'm {age} years old.")

# Escaping Characters
escaped = "He said \"Python is great!\""
print(escaped)

# String Methods
example = " python programming "
print("Capitalized:", example.capitalize())
print("Count of 'p':", example.count('p'))
print("Is alphanumeric:", example.isalnum())
print("Stripped:", example.strip())
print("Replaced 'python':", example.replace("python", "Java"))