print(" Star pyramid \n")

row_num = int(input("Enter the number of rows for a star pyramid. "))

for i in range (row_num):
    for j in range(i+1):
        print("* ", end="")
    print()

print(" Floyds triangle \n")

row_num1 = int(input("Enter the number of rows for a floyds triangle. "))
number = 1

for i in range (1, row_num1 + 1):
    for j in range(i+1):
        print(number, end=" ")
        number += 1
    print()

print("Diamond")

row_size = int(input("Enter the number of rows size for a diamond. "))

if row_size % 2 == 0:
    half_rows = row_size // 2
   
else:
    half_rows = row_size // 2  + 1

space = half_rows - 1

for i in range (1, half_rows + 1):
    for j in range(1,  space + 1):
        print (" ", end = "")

    space -=1
    number = 1
    
    for j in range (2 * i - 1):
        print (number, end="")
        number += 1

    print()

space = 1

for i in range (1, half_rows):
    for j in range(1,  space + 1):
        print (" ", end = "")

    space +=1
    number = 1
    
    for j in range (1, 2 * (half_rows - i) ):
        print (number, end="")
        number += 1

    print()
