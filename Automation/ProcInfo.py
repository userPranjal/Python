# Automation script to display information(name, pid, username) of running processes

import psutil

def DisplayProcess():
    Border = "-" * 50

    LogFileName = "ProcessInfo.log"

    print("Log file gets created with name :", LogFileName)

    fobj = open(LogFileName, "w")

    fobj.write(Border + "\n")
    fobj.write("Automation Script\n")
    fobj.write(Border + "\n")

    fobj.write("Information of Running Processes\n")
    fobj.write(Border + "\n")

    for process in psutil.process_iter():
        try:
            fobj.write("Process Name : " + process.name() + "\n")
            fobj.write("Process ID   : " + str(process.pid) + "\n")
            fobj.write("Username     : " + process.username() + "\n")
            fobj.write(Border + "\n")

        except:
            pass

    fobj.close()

    print("Process information stored successfully...")


def main():
    Border = "-" * 50

    print(Border)
    print("Automation Script")
    print(Border)

    DisplayProcess()

    print(Border)

if __name__ == "__main__":
    main()