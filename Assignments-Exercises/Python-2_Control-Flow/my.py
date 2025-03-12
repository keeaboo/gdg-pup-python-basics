
try:
    # get age from user
    age = int(input("Please enter your age: "))

    # check age category
    if age < 0:
        print("Invalid input: Age cannot be negative.")
    elif age < 13:
        print("You are categorized as: Child")
    elif age < 20:
        print("You are categorized as: Teenager")
    elif age < 60:
        print("You are categorized as: Adult")
    else:
        print("You are categorizes as: Senior")

except ValueError:
    print("Invalid input: Age cannot be a non-number.")