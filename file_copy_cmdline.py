import sys

def main():
    try:
        source = sys.argv[1]

        file1 = open(source, "r")
        file2 = open("Demo1.txt", "w")

        data = file1.read()
        file2.write(data)

        file1.close()
        file2.close()

        print("Created Demo1.txt and copied contents of", source, "into Demo1.txt")

    except FileNotFoundError:
        print("Source file not found")

    except IndexError:
        print("Please provide the source file name...")

if __name__ == "__main__":
    main()