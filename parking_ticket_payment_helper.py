def calculate_change(paid, price):  
    change_value = price - paid
    return change_value

ticket_price = 30
print(f"Parking ticket payment is {ticket_price} units.")
print("The accepted coins are: 1, 5, 10, 25")

total_inserted = 0
coins_inserted = 0

while True:
    coins = int(input("Enter coins "))
    if coins != 1 and coins != 5 and coins != 10 and coins != 25:
        print("\nInvalid coin, please try again\n")
        continue

    total_inserted = total_inserted + coins
    coins_inserted = coins_inserted + 1

    if total_inserted >= ticket_price:
        print("\nYou have paid enough money.\n")
        break

change_due = calculate_change(total_inserted, ticket_price)

if change_due == 0:
    pass
else:
    print(f"You're change is: {change_due} units")

print("\n=== Payment Receipt ===\n")

print("Ticket Price:", ticket_price)
print("Coins inserted:", coins_inserted)
print("Total Paid:", total_inserted)
print("Change given::", change_due)
print("\n===========================\n")
print("Parking ticket is complete.")