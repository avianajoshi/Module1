temp = int(input("What's the temperature today? Just write the number and nothing else. "))

if (temp < 20):
    print("Great day to have fun inside. Outside must be cold!")
elif (temp > 20 or temp == 20):
    print("Magnificent day to cool yourselves with some icecream outside. Don't run alot though and remember your suncream!")
else:
    print("Keep yourselves safe by the sun or snow")

rain = input("Is it raining today? Yes or no. ")

if (rain == "yes" or rain == "Yes"):
    print("Reminder: Keep an umbrella with you whenever it's raining.")
elif (rain == "no" or rain == "No"):
    print("Tip: If you see clouds and it's not raining, carry an umbrella.")
else:
    print("Please check for any errors in your spelling and only write, yes or no.")

homework_time = int(input("How long is your homework for? Answer in minutes. Example: 30 "))

if (homework_time == 10 or homework_time < 10):
    print("No need for a break.")
elif (homework_time > 50):
    print("Have a rest between your homework.\n")
    print("Don't give up! Have a 10 minutes rest.")

free_time = int(input("How long is your freetime for? Answer in minutes. Example: 20 minutes "))

if (free_time > 12):
    print("You got enough time to practice your favourite things and plan your day ahead.")
else:
    print("Try planning your day ahead and if you got spare time, you could use it for free time.")

print("This is your plan for the day.")
print()
print(temp,"\n", rain,"\n", homework_time,"\n", free_time)
