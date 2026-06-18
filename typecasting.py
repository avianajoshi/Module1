name = "penguin"
age = 15
is_student = True
weight = 38.5

print("Data Type of Name is", type(name))

print("Data Type of Age is", type(age))

print("Data Type of Is_student is", type(is_student))

print("Data Type of Weight is", type(weight))

print("\n After Type Casting...")
age = str(age)
print(age)
print("Data Type of Age is", type(age))
weight = int(weight)
print(weight)
print("Data Type of Weight is", type(weight))