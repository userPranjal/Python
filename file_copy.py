def main():
    source = input("Enter existing file name: ")
    destination = input("Enter new file name: ")

    try:
        file1 = open(source, "r")
        file2 = open(destination, "w")

        data = file1.read()
        file2.write(data)

        file1.close()
        file2.close()

        print("Contents copied successfully...")

        file2 = open(destination, "r")
        print("\nContents of", destination, "are:")
        print(file2.read())
        file2.close()

    except FileNotFoundError:
        print("Source file not found")

if __name__ == "__main__":
    main()