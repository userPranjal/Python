# Program to count the total number of words in a file

def main():
    filename = input("Enter the file name: ")

    try:
        file = open(filename, "r")
        count = 0

        for line in file:
            words = line.split()
            count = count + len(words)

        file.close()

        print("Total number of words in", filename, ":", count)

    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    main()