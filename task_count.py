print("========================")
print("    Homework Checker    ")
print("========================")
print()
total_homework = 4
orignal_count = total_homework
completed_count = 0
task_num = 1

while (task_num <= total_homework):
    if task_num == 1:
        next_task = "Maths Homework"
    elif task_num == 2:
        next_task = "English Homework"
    elif task_num == 2:
        next_task = "Science Homework"
    else:
        next_task = "Reading Homework"

    answer = input(f"Have you finished: {next_task}? (yes/no) ")

    if answer == "yes":
        completed_count += 1
        task_num += 1
        print("Good job for finishing your homework!")
    else:
        print("Finish it and try again.")
    print("You got", total_homework - completed_count)

print("Let's safely look at a infinite loop.")
test_value = 0
safety_counter = 0
while test_value <= 0:
    print("This condition doesn't change, so this would run forever!")
    safety_counter += 1
    if safety_counter == 3:
        print("(Stopping here on purpose - a real infinite loop never stops on its own!)")
        break
