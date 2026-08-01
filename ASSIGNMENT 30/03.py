import schedule
import time
import datetime

def Message():
    print("Coding Kar...",datetime.datetime.now())

def main():
    print(" AUTOMATION SCRIPT STARTED ".center(50,"="))

    schedule.every(30).minutes.do(Message)

    while(True):
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
     main()


