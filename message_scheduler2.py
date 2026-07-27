import time
import schedule

def DisplayMessage(message):
    print(message)

def main():
    message = input("Enter message: ")

    schedule.every(5).seconds.do(DisplayMessage, message)

    print("Message scheduler started. Press Ctrl + C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()