number = 1
n = int(input("Enter the numbers of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(number , end=" ")
        number = number + 1
    print()