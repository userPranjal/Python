# Accepts number from user and print that number of " * " on screen

def DisplayStars(num):
    for i in range(num):
        print("*", end=" ")

number = int(input("Enter a number: "))
DisplayStars(number)