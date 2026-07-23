# Hourly File Backup Automation
# Copies a file every hour, adds a timestamp to the
# backup filename, and logs the backup details.

import schedule
import time
import shutil
import os
import datetime

def BackupFile(source, destination):

    filename = os.path.basename(source)

    index = filename.rfind(".")

    timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")

    backupfilename = filename[:index] + "_" + timestamp + filename[index:]

    destinationpath = os.path.join(destination, backupfilename)

    shutil.copy(source, destinationpath)

    file = open("backup_log.txt", "a")
    file.write("Backup completed successfully at : ")
    file.write(datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p\n"))
    file.close()

    print("Backup completed successfully.")

def main():

    print("Automation Script Started")

    source = input("Enter source file path : ")
    destination = input("Enter destination directory path : ")

    #schedule.every().hour.do(BackupFile, source, destination)

    schedule.every(1).seconds.do(BackupFile, source, destination)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()