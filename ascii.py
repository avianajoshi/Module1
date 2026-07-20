char = input("Type one character ")

if type(char) == str and len(char) == 1:
    print("Valid single character!")
    ascii_character = ord(char)
    print("ascii value of", char, "is equal to ", ascii_character)
else:
    print("Please enter single character and try again!")
