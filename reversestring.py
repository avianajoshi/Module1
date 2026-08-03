string = input("Please enter your own string: ")

string2 = ('')

for i in string:
    string2 = i + string2

print("\nThe Oringinal String = ", string)
print("The Reversed String = ", string2)