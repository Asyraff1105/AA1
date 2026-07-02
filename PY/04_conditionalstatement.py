

age = int(input("Enter your age: "))

if age >= 18:
        print("You are eligible to vote.")  
else:
        print("You are not eligible to vote yet.")

score = int(input("Enter your score: "))

if score >= 90:
        print("You got an A grade.")
elif score >= 80:
        print("You got a B grade.")
elif score >= 70:
        print("You got a C grade.")
elif score >= 60:
        print("You got a D grade.")
else:
        print("You got an F grade.")

user_age = int(input("Enter your age: "))
has_license = input("Do you have a driving license? (yes/no): ").strip().lower()

if user_age >= 18 and has_license == "yes":
        print("You are eligible to drive.")
else:
        print("You are not eligible to drive.")

day = str(input("What day is today? ")).strip().lower()

if day == "saturday" or day == "sunday":
        print("It's the weekend!")
else:
        print("It's a weekday.")

weather = str(input("How's the weather today? (sunny/rainy): ")).strip().lower()
temperature = int(input("Enter the temperature: "))

if weather == "sunny":
        if temperature > 30:
                print("It's a hot sunny day.")
        else:
                print("It's a pleasant sunny day.")
elif weather == "rainy":
        if temperature < 20:
                print("It's a cold rainy day.")
        else:
                print("It's a warm rainy day.")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
        category = "You are underweight."
elif 18.5 <= bmi < 24.9:
        category = "You have a normal weight."
elif 25 <= bmi < 29.9:
        category = "You are overweight."
else:
        category = "You are obese."

print(f"bmi = {bmi:.2f}. You are {category}")
