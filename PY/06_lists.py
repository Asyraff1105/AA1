# List in Python 
car = ["Toyota", "Honda", "Ford"]
country = ["Japan", "France", "Brazil"]
colour = ["Red", "Blue", "Green", "Yellow", "Black", "White"]

print(car[2])  # Output: Ford
print (country[-1])  # Output: Brazil
print (colour[3:5])  # Output: Yellow, Black #Start index 3 sampai sebelum index 4
print (country[:2])  # Output: Japan, France #Semua sebelum index 2
print (colour[2:])  # Output: Green, Yellow, Black, White #Semua selepas index 2

car.append("Nissan")  # Add an item to the end of the list
colour.insert(0, "Purple")  # Insert an item at a specific index
popped = country.pop()  # Remove and return the last item from the list
country.sort()  # Sort the list in ascending order
colour.reverse()  # Reverse the order of the list

print(car)  # Output: ['Toyota', 'Honda', 'Ford', 'Nissan']
print(country)  # Output: ['France', 'Japan']
print(colour)   

#Exercise
#Create a grocery list and perform various operations

grocery = ["Milk", "Eggs", "Bread", "Butter", "Cheese"]

grocery.append("Fruits")  
grocery.insert(2, "Vegetables")  
grocery.remove("Butter")
grocery.sort()

len(grocery)
"Eggs" in grocery
grocery + ["Juice", "Cereal"]  
grocery * 2 

print(grocery)

numbers = [5, 2, 9, 1, 7]

print("Largest number in the list:", max(numbers))  # Output: 9
print("Smallest number in the list:", min(numbers))  # Output: 1
