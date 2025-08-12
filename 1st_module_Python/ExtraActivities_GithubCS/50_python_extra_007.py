#Tuples: Unpacking

#Tuple Unpacking
### Step 1:
#1.  Use the `person` tuple from the previouse activity.
person = ("Alice", 30, "Paris")

#2.  Unpack it into three variables: `name`, `age`, `city`.
name, age, city = person
    
#3.  Print a sentence: `"Alice is 30 years old and lives in Paris."`
print(f"{name} is {age} old and lives in {city}.")

### Step 2: 
#1.  Create the tuple `book = ("Harry Potter And The Chamber Of Secrets", 245, "England", 1998)`.
book = ("Harry Potter And The Chamber Of Secrets", 245, "England", 1998)
    
#2.  Unpack only the values of `book` necesary to create a new variable named `message` with 
# the sentence: `'Alice favorite book is "Harry Potter and the Chamber of Secrets" which was published in the year 1998.'`.
booktitle, *middle, publish_year = book
message = name+" favorite book is '"+booktitle+"' which was published. in the year "+str(publish_year)+"."

#3.  Print the `message`.
print(message)

