# Automation script to create a log file of all running processes
# in the specified directory

import psutil
import sys
import os

def ProcessLog(DirectoryPath):
    Border = "-" * 50

    Ret = os.path.exists(DirectoryPath)

    if Ret == False:
        print("Automation Error : There is no such Directory with name", DirectoryPath)
        return

    Ret = os.path.isdir(DirectoryPath)

    if Ret == False:
        print("Automation Error : It is not a Directory with name", DirectoryPath)
        return

    LogFileName = os.path.join(DirectoryPath, "ProcessInfo.log")

    print("Log file gets created with name :", LogFileName)

    fobj = open(LogFileName, "w")

    fobj.write(Border + "\n")
    fobj.write("Automation Script\n")
    fobj.write(Border + "\n\n")

    fobj.write("Information of Running Processes\n")
    fobj.write(Border + "\n")

    for process in psutil.process_iter(['pid', 'name', 'username']):
        try:
            fobj.write("Process Name : " + process.info['name'] + "\n")
            fobj.write("Process ID   : " + str(process.info['pid']) + "\n")
            fobj.write("Username     : " + str(process.info['username']) + "\n")
            fobj.write(Border + "\n")
        except:
            pass

    fobj.close()

    print("Process information stored successfully.")


def main():
    Border = "-" * 50

    print(Border)
    print("Automation Script")
    print(Border)

    if len(sys.argv) == 2:

        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This automation script creates a log file of all running processes.")
            print("Use --u for usage.")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Usage : python ProcInfoLog.py DirectoryName")

        else:
            ProcessLog(sys.argv[1])

    else:
        print("Invalid number of arguments.")
        print("Please use --h or --u for more information.")

    print(Border)
    print("Thank you for using Automation Script")
    print(Border)


if __name__ == "__main__":
    main()