CAMERA = 2
MICROPHONE = 4
STORAGE = 6
LOCATION = 8

approved_app = [
    "maths app",
    "english app",
    "quiz app",
    "code app"
]

restricted_app = [
    "games app",
    "social media app",
    "shopping app"
]

student_name = input("What's your name? ")
requested_app = input("Enter the app you want to access. ").lower()

print("\n     Identity Operator Check     \n")

if type (student_name) is str and (requested_app) is not int:
    print(f"{student_name} is a string.")
    print("The app you want to access is not a number.")

print("\n     Membership Operator Check     \n")

if (requested_app in approved_app) and (requested_app not in restricted_app):
    print(f"{requested_app} is not in restricted app.")
    print(f"{requested_app} is a approved app.")

else:
    print(f"{requested_app} is a restricted app. You are not allowed to access that app")

print("\n     Permission Setting     \n")

permission = CAMERA | MICROPHONE | STORAGE

print(f"The permission number is {permission}.")
print("The permission bit is", bin(permission))

if permission & CAMERA:
    print("Camera is enabled")
else: 
    print("Camera is desabled")
if permission & MICROPHONE:
    print("Microphone is enabled")
else: 
    print("Microphone is desabled")
if permission & STORAGE:
    print("Storage is enabled")

if permission & LOCATION:
    print("Location is enabled")
else: 
    print("Location is  disabled")

bit_shift = CAMERA << 1
print(f"Camera bit is {bit_shift}")

bit_shift = STORAGE >> 1
print(f"Storage bit is {bit_shift}")

if requested_app in approved_app and requested_app not in restricted_app:
    print(f"{requested_app} is an approved app")

else:
    print(f"{requested_app} is a restricted app")

print("=======   =======")
print()
print("=======   =======")