name = "Python programming"

print (name[0]) # (first character)
print (name[-1]) # (last character)
print (name[0:6]) # (slice 0 to 5)
print (name[:6]) # (from start to 5)
print (name[7:]) # (7 to end)


name2 = "  michael jackson "

print(len(name2)) # Length
print(name2.strip()) # Remove whitespace
print(name2.upper()) # Uppercase
print(name2.lower()) # Lowercase
print(name2.title()) # Title case
print(name2.replace("Michael", "Joe")) # Replace


name3 = "James Bond"
age = 99

message_1 = f"My name is {name3} and I am {age} years old." # f-strings
message_2 = "My name is {} and I am {} years old.".format(name3, age) # str.format()
message_3 = "My name is %s and I am %d years old." % (name3, age) # %-formatting

print(message_1)
print(message_2)
print(message_3)


text = """Python is a powerful programming language. It is easy to learn and versatile! 
You can use Python for web development, data science, and automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike."""

print(text)
