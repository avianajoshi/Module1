# First ask for the number
power_num = int(input("Enter a number. "))
print()

# Ask user for the power number and use f"
power = int(input(f"Enter a number that you want to know for the power of {power_num}? "))

answer = 1

# Use for loop to figure out the answer to the users question
for i in range(power):
    answer = answer * power_num
print(f"The {power} number power of {power_num} is", answer )
