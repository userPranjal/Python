# Program to count the number of lines in a file

def main():
    filename = input("Enter file name: ")

    try:
        file = open(filename, "r")

        count = 0
        for line in file:
            count = count + 1

        file.close()

        print("Total number of lines in", filename, ":", count)

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()