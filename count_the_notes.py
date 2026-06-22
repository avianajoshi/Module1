amount =int(input("Please enter amount for withdraw :"))

note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10

print("Notes of 100 rupee", note_1)
print("Notes of 50 rupee", note_2)
print("Notes of 10 rupee", note_3)