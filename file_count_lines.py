# Program to count the number of lines in a file

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        count = 0
        for line in file:
            count += 1

    print("Total number of lines in", filename, ":",count)

except FileNotFoundError:
    print("File not found")