# Display information of if it is running

import psutil
import sys

def DisplayProcess(ProcessName):
    Border = "-" * 50
    Found = False

    print(Border)
    print("Process Information")
    print(Border)

    for process in psutil.process_iter(['pid','name','username']):
        try:
            if process.info['name'] == ProcessName:
                Found = True

                print("Process ID : ",process.info['pid'])
                print("Process Name : ",process.info['name'])
                print("Username : ",process.info['username'])
                print(Border)

        except:
            pass

    if Found == False:
        print("Process is not running...")


def main():
    Border = "-" * 50

    print(Border)
    print("Automation Script")
    print(Border)

    if len(sys.argv) != 2:
        print("Usage : python ProcInfo.py ProcessName.exe")
        return

    DisplayProcess(sys.argv[1])


if __name__ == "__main__":
    main()