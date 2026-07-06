# Basic class definition
class Person:
    # Class atribute (shared by all instances)
    species = "Homo sapiens"

    # Constructor method 
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

    # Method with parameters
    def have_birthday(self):
        self.age += 1
        return f" Happy birthday! {self.name} is now {self.age}."

    # Creating objects (instances)
    person1 = Person("Alice", 25)
    person2 = Person("Bob", 30)

    # Accessing attributes
    print(person1.name) # "Alice"
    print(person1.age) # 25

    # Calling methods
    print(person1.introduce())
    print(person1.have_birthday())

    # Class attributes
    print(Person.species) # "Homo sapiens"
    print(person1.species) # "Homo sapiens"