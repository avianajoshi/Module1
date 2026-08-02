print("===========================================")
print("    Welcome to Holiday Activity Planner    ")
print("===========================================")

print("Choose from:")
print("1 -  Beach Holiday")
print("2 -  Mountain Holiday")

holiday = input("Type 1 or 2 ")

if holiday == "1":
    print("Choose from:")
    print("1 -  Swimming")
    print("2 -  Sandcastle building")
    activity = input("Type 1 or 2 ")
    if activity == "1":
        print("Swimming is really good for your health. If you practice swimming, you will get stronger but remember to not swim if there is a red flag on the beach and don't swim really far unless you are a professional")
    elif activity == "2":
        print("Sandcastle building is really fun when you have friends around but sand is also relaxing if your on your own though.")
    else:
        print("Try typing 1 or 2 and remember 1 - Swimming and 2 - Sandcastle building.")
        exit()

elif holiday == "2":
    print("Choose from:")
    print("1 -  Hiking")
    print("2 -  Camping")
    activity = input("Type 1 or 2 ")
    if activity == "1":
        print("Remember to keep your hiking pole when your hiking!")
    elif activity == "2":
        print("Camping is a great choice but don't try going on a rainy day and remember your sleeping bags.")

else:
    print("Please type 1 or 2")
    exit()


print("=================================================")
print(" Thank you planning on Holiday Activity Planner! ")
print("=================================================")