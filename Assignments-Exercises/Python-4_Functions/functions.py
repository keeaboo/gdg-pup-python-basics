# function that returns the greeting message and takes in name as parameter
def create_greeting(name):
    return f"Hello, {name}!, welcome to the GDG Web Development Team! You're doing great, and I truly believe that someday you'll be an amazing developer. Life may feel challenging right now, and programming can be overwhelming at times, but remember, all your hard work will pay off in the end. Keep pushing forward, you're on the right path!"

# try:

# get user's name
name = input("Enter your name: ")
# print the return value of create_greeting function
print(create_greeting(name))

# except ValueError:    # input() function always returns a string
#     print("Invalid input: Please enter a valid name.")