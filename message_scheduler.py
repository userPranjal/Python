import schedule
import time

def Message():
    print("Coding kar...")

def main():
    print("Automation script started")

    schedule.every(30).minutes.do(Message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()