def greet_customer():
    print("=== Welcome to the arts supplies store ===")
    print("Here you'll find the arts suplies you need!")
    print("==========================================\n")

greet_customer()

price_per_art_item = float(input("What's the price per art item in dollars? "))
item_num_bought = int(input("How many items have you bought? "))

def calculate_total(price,items):
    total_price = price * price_per_art_item
    return total_price

price_total = calculate_total(price_per_art_item, item_num_bought)
round_total = round(price_total, 2)

def calculate_change(paid, total):
    change = total - paid
    return change


def thankyou_message(items):
    if items >= 4:
        return "You chose some great art supplies! Thank you for stopping by!"
    else:
        return "Thank you for visiting us."

thankyou_message_ending = thankyou_message(item_num_bought)

print()
print("====== Art Supplies Store reciept =====")
print("Price Per Item:", price_per_art_item )
print(" Items bought:", item_num_bought )
print("Total Cost:", round_total )
amount_paid = float(input("Please enter total amount paid."))
return_change = calculate_change(amount_paid, round_total)

print("Amount Paid:", amount_paid )
print("Change Due:", return_change )
print(thankyou_message_ending)
print("=======================================")