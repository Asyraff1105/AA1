math = {"Alice", "Bob", "Charlie"}
science = {"Bob", "Charlie"}
english = {"Alice"}

students1 = (math.union(science))

students2 = (math.intersection(science))

students3 = (english.difference(science))

print(f"Students who take all subjects are {students1}")
print(f"Students who take both Math and Science are {students2}")
print(f"Students who take only English are {students3}")