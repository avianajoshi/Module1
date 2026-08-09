rice = 11
print("Rice costs £11 per 1 bag.")
milk = 7
print("Milk costs £7 per bottle.")
fruit = 9
print("2 fruits costs £9.")
family_number = int(input("How many family members are shopping with you? "))
print()
rice_number = int(input("Enter how many bags of rice do you need? "))
milk_number = int(input("Enter how much bottles of milk do you need? "))
fruit_number = int(input("Enter how much packs of 2 for fruits do you need?"))
print()
total_cost = (rice * rice_number ) + (milk * milk_number) + (fruit * fruit_number)
print("Total cost is £",total_cost)
total_cost_family = (total_cost / family_number)
print("After distrubution between your family\n","£",total_cost_family)
total_item = rice_number + milk_number + fruit_number
if (total_item % family_number == 0):
    print("The item are divided equally.")