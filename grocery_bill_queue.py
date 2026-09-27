print("=== Grocery Billing queue ===\n")

# Part 1
low_price_item = 0
medium_price_item = 0
high_price_item = 0

customers_served = 0
total_sales = 0

billing = True

# Part 2
while billing:
    users_name = input("What's your name? ")
    item_count = int(input("How many items do you have? "))
    # part 3
    if item_count <= 0:
        print("Invalid number. Write a number above 0")
        continue

    # Part 4
    customers_total = 0
    item_num = 1
    while item_num <= item_count:
        item_name = input("What's item name? ")
        price = int(input("What's the price of the item? "))
        quantity = int(input("What's the quantity of the item? "))
        # Part 5
        if price <= 0 or quantity <= 0:
            print("Invalid price or quantity.")
            continue
        item_total = price * quantity
        print(item_name, ":", item_total )
        customers_total = customers_total + item_total

        if price <= 50:
            low_price_item += quantity
        elif price <= 100:
            medium_price_item += quantity
        else:
            high_price_item += quantity
        item_num += 1

    # Part 6
    customers_served = customers_served + 1
    total_sales = customers_total + total_sales
    print(f"Total price for {users_name} is {customers_total}")

    billing_2 = input("Next person? Yes/No: ")

    if billing_2 == "No" or billing_2 == "no": 
        billing = False

# Part 7
for slot in range (1,4):
    if slot == 1:
        total = low_price_item

    elif slot == 2:
        total = medium_price_item

    else:
        total = high_price_item

if total > 0:
    print(total)

print(f"Customers served : {customers_served}")
print(f"Total sales : {total_sales}")
print("Grocery Billing closed. Bye!")