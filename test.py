secret = 53
hearts = 5
while range(1,6):
    answer = int(input("What number do you think i have thought of? "))
    if answer == secret:
        print("Correct answer!")
        print("You won! Woohoo!!!")
        break
    elif answer >= secret:
        print("Your answer is too big.")
        hearts = hearts - 1
        print(f"You have {hearts} hearts left.")
        if hearts == 0:
            print(f"Sorry! You lose the answer was, {secret}.")
    else:
        print("Your answer was too low.")
        hearts = hearts - 1
        print(f"You have {hearts} hearts left.")
        if hearts == 0:
            print(f"Sorry! You lose the answer was, {secret}.")

print(f"Good job! You won with {hearts} hearts left!")