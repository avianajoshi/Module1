print("Library Visit Planner")
print("Answer 3 quick questions and I'll plan your library visit!\n")

day = input("What day is it? (Monday to Sunday):").lower()
weather = input("What is the weather? (Sunny / rainy / cloudy)").lower()
book_due = input("Do you have a book to return? (Yes or no)").lower()

if day in ("saturday", "sunday"):
    print("Today is the weekend! Nice day to chill out in the library.")
elif day == "monday":
    print("Its a start of the week")
elif day in ("tuesday","wednesday","thursday"):
    print("Today is a school day. Suggest you to have a short time in the library")
elif day == "friday":
    print("Its the end of the week. please ensure to return any books")
else:
    print("Unrecognised day. Please check for any errors in your spelling.")

if weather == "sunny" and book_due == "yes":
    print("Library Tip: Best day to go to the library.")
elif weather == "rainy" or "cloudy":
    print("Weather Tip: Remember to keep an umbrella whilst taking a short trip to the library.")
elif not (book_due == "yes"):
    print("No books to return. Just get a book from the library if you want.")
else:
    print("Please answer correctly.")


if book_due == "yes"  and weather == "sunny" and day not in ("saturday", "sunday"):
    print("Best plan: please return your book after school time")
elif weather in ("rainy", "cloudy") and book_due == "yes":
    print("Best plan: Keep you library books safe and return carefully")
elif weather == "sunny" and day in ("saturday", "sunday"):
    print("Best plan: Extend your time in library to read more books")
else:
    print("Best plan: Think of the day that is best to go to the library and return book on time")