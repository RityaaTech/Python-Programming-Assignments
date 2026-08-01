import schedule
import time 
import datetime

def Display():
    print("Jay Ganesh...",datetime.datetime.now())

def main():
    print("AUTOMATION SCRIPT STARTED ".center(50,"="))

    schedule.every(2).seconds.do(Display)

    while(True):
        schedule.run_pending()
        time.sleep(1)

    print(" END OF THE AUTOMATION SCRIPT ".center(50,"="))

if __name__ == "__main__":
    main()
