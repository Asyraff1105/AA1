name = str(input("Enter your name: "))
height = float(input("Enter your height: ")) # Convert to float 

# Input validation

while True:
    try:
        age = int(input("Enter your age: "))
        if age > 0:
            break
        else:
            print("Age must be a positive integer. Please try again.")
    except ValueError:
        print("Please enter a valid number!")

# Output validation
print(f"Hello, {name}!")
print(f"You are {age} years old and {height} feet tall.")


number_1 = int(input("Enter 1st positive integer for calculation: "))
number_2 = int(input("Enter 2nd positive integer for calculation: "))
Operation = input("Enter the operation you want to perform (+, -, *, /): ")

# Input validation

while True:

    result = 0
    if Operation in ['+', '-', '*', '/']:
        break
    else:
        print("Invalid operation. Please enter one of the following: +, -, *, /")
        Operation = input("Enter the operation you want to perform (+, -, *, /): ")

# Output validation
if Operation == '+':
    result = number_1 + number_2
elif Operation == '-':
    result = number_1 - number_2
elif Operation == '*':
    result = number_1 * number_2
elif Operation == '/':
    if number_2 != 0:
        result = number_1 / number_2
    else:
        print("Error: Division by zero is not allowed.")
        result = None


if result is not None:
    print(f"The result of {number_1} {Operation} {number_2} is: {result}")
