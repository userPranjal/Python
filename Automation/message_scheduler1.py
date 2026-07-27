import time

def main():
    message = input("Enter message: ")
    interval = int(input("Enter interval in seconds: "))

    if interval <= 0:
        print("Error: Interval must be greater than zero.")
    else:
        print(f'\nDisplaying "{message}" every {interval} seconds...\n')

    try:
        while True:
            print(message)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nScheduler stopped.")

if __name__ == "__main__":
    main()
