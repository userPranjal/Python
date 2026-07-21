def main():
    filename = input("Enter the file name: ")

    try:
        fobj = open(filename,"r")

        for line in fobj:
            print(line,end="")
        
        fobj.close()
        
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()