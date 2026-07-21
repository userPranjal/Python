def main():

    count = 0

    filename = input("Enter file name : ")
    word = input("Enter string to check frequency : ")

    try:
        file = open(filename, "r")

        data = file.read()
        file.close()

        count = data.count(word)

        print("Frequency of", word, "is", count)

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()