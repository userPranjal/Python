# Compare Two Files (Command Line)

import sys

def main():
    try:
        source1 = sys.argv[1]
        source2 = sys.argv[2]

        file1 = open(source1, "r")
        file2 = open(source2, "r")

        data1 = file1.read()
        data2 = file2.read()
        
        file1.close()
        file2.close()

        if data1 == data2 :
            print("Success")
        else:
            print("Failure")

    except FileNotFoundError:
        print("Source file not found")

    except IndexError:
        print("Please provide two file names")

if __name__ == "__main__":
    main()