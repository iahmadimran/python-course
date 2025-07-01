# Write first ever python program.
# print('Hello world')

message = "Hello World."

# Printing the stored message variable.
# print(message)

# Checking the length of the string using len() method
# print(len(message))

# Using indexes on the string 
# print(message[6:13])

# Lowering the string using lower() method
# print(message.lower())

# Capitalizing the string using upper() method
# print(message.upper())

# Finding the character using find() method
# print(message.find('World'))

# Replacing the character using replace() method
# print(message.replace("World", "Universe"))

# Checking all the methods in the string
# print(dir(str))

# Checking all the ways to combine the string
greeting = "Hello"
name = "Ahmad"

# my_message = greeting + ", " + name + ". Welcome!"

my_message = f"{greeting}, {name}. Welcome!" # f string

# print(my_message)

# Exercises

# str = 'Thirty' + ' ' + 'Days ' + "of" + " Python"
# str_2 = "Coding " + 'for ' + 'all'
# print(str_2)

company = 'Facebook, Google, Amazon, Microsoft, Apple, IBM, Oracle'
print(company[0:16])
