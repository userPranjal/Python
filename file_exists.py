import os

def main():

    filename = input("Enter the file name :")
    
    if(os.path.exists(filename)):
        print("File exists in the current directory")
    else:
        print("File does not exists in the current directory")

if __name__ == "__main__":
    main()