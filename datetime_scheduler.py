import schedule
import time
import datetime

def File():
    file = open("Marvellous.txt", "a")

    file.write(f"{datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")}\n")
    file.close()

def main():
    print("Automation Script Started")

    schedule.every(5).minutes.do(File)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()