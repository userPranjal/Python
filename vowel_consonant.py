#Accepts one character and checks whether it is vowel or consonant

def ChkCharacter(char2):
    if char2 in ('a','e','i','o','u','A','E','I','O','U'):
        print("It is a Vowel")
    else:
        print("It is a Consonant")

def main():
    char1 = input("Enter a character : ")

    ChkCharacter(char1)

if __name__ == "__main__":
    main()