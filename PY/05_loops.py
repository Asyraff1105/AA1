
for i in range(5): 
    print (i) 

for i in range(1, 6):
    print(i)

for i in range(0, 10, 2):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1  

for i in range (10):
    if i == 3:
        continue   # Skip this iteration
    if i == 7:
        break      # Exit the loop
    print(i)

for i in range(2):
        for j in range(3):
            print(f"({i}, {j})")


# Multiplication table
num= int(input("Enter a number to print its multiplication table: "))
for i in range(1, 13):
    print(f"{num} x {i} = {num * i}")   

# Prime number up to 20
for num in range(2, 21):    #2 to 20
    count = 0
    for i in range(1, num + 1): 
        if num % i == 0: # % tu nak check ada baki ke tak 
            count = count + 1 # Tambah 1 ke count 
    if count == 2:
        print(f"{num} is a prime number.")

