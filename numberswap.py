a = int(input("Enter any 1 number "))
print("a =", a)
b = int(input("Enter the next number "))
print("b =", b)
c = int(input("Enter the last number "))
print("c =", c)

d = a
a = c
c = b
b = d


print ("After the numbers swapped... \n")
print("a =", a)
print("b =", b)
print("c =", c)
