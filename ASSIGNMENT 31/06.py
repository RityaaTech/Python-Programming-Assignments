import schedule
import time

def Monday_Message():
    print("START YOUR WEEKLY GOALS")

def Wednesday_Message():
    print("REVIEW YOUR WEEKLY PROGRESS")

def Friday_Message():
    print("WEEKLY WORK COMPLETED.")


def main():
    print(" AUTOMATION SCRIPT STARTED ".center(50,"="),end = "\n")

    schedule.every().monday.at("09:00").do(Monday_Message)
    schedule.every().monday.at("17:00").do(Wednesday_Message)
    schedule.every().monday.at("18:00").do(Friday_Message)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()