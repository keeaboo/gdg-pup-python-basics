# for loop
# list of my favorite foods
foods = ["Pizza", "Fried Chicken", "Fried Rice", "Corn", "Cheese", "Crab", "Shrimp"]

# prints my favorite foods
print("A list of my favorite foods: ")
for item in foods:
    print("-", item)
print("\n")

# while loop
# ask the user to input a starting number
try:
    start = int(input("Enter a starting number for the countdown: "))

    if start > 0:  # print the countdown if input is more than 0
        while start > 0:
            print(start)
            start -= 1 # reduce the number by 1 for the next iteration
        print("Countdown Complete!")
    else:
        print("Invalid input: Please enter a number greater than zero.")

except ValueError:
    print("Invalid input: Please enter a valid number.")