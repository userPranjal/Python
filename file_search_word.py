def main():
    filename = input("Enter file name : ")
    word = input("Enter word to search : ")

    try:
        file1 = open(filename, "r")

        data = file1.read()
        file1.close()

        if word in data:
            print(word, "word is found in", filename)
        else:
            print(word, "word is not found in", filename)

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()